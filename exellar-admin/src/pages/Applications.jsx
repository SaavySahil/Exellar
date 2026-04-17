import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import client from '../api/client.js'
import ConfirmModal from '../components/ConfirmModal.jsx'
import Toast from '../components/Toast.jsx'
import styles from './Applications.module.css'

export default function Applications() {
  const qc = useQueryClient()
  const [selected, setSelected] = useState(null)
  const [deleteTarget, setDeleteTarget] = useState(null)
  const [toast, setToast] = useState(null)

  const { data: applications = [], isLoading } = useQuery({
    queryKey: ['admin-applications'],
    queryFn: () => client.get('/api/admin/applications').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/applications/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-applications'])
      setToast({ message: 'Application deleted', type: 'success' })
      if (selected?.id === deleteTarget?.id) setSelected(null)
    },
    onError: () => setToast({ message: 'Delete failed', type: 'error' }),
  })

  function downloadResume(app) {
    const token = localStorage.getItem('exellar_token')
    const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'
    window.open(`${API_BASE}/api/admin/applications/${app.id}/resume?token=${token}`, '_blank')
  }

  return (
    <div className={styles.shell}>
      <div className={styles.listPane}>
        <h1 className={styles.heading}>Applications</h1>

        {isLoading ? <p className={styles.muted}>Loading…</p> : (
          <div className={styles.list}>
            {applications.map(a => (
              <div
                key={a.id}
                className={`${styles.item} ${selected?.id === a.id ? styles.itemActive : ''}`}
                onClick={() => setSelected(a)}
              >
                <p className={styles.name}>{a.applicant_name}</p>
                <p className={styles.meta}>{a.job_title || 'General Enquiry'} &nbsp;·&nbsp; {fmtDate(a.applied_at)}</p>
              </div>
            ))}
            {applications.length === 0 && <p className={styles.muted}>No applications yet.</p>}
          </div>
        )}
      </div>

      <div className={styles.detailPane}>
        {selected ? (
          <>
            <div className={styles.detailHeader}>
              <div>
                <h2 className={styles.detailName}>{selected.applicant_name}</h2>
                <p className={styles.detailMeta}>{selected.email}
                  {selected.phone && ` · ${selected.phone}`}
                </p>
              </div>
              <div className={styles.detailActions}>
                {selected.has_resume && (
                  <button className={styles.resumeBtn} onClick={() => downloadResume(selected)}>
                    Download Resume
                  </button>
                )}
                <button className={styles.delBtn} onClick={() => setDeleteTarget(selected)}>
                  Delete
                </button>
              </div>
            </div>

            <div className={styles.detailBody}>
              <Row label="Applied For" value={selected.job_title || 'General Enquiry'} />
              <Row label="Date" value={fmtDate(selected.applied_at)} />
              {selected.cover_note && (
                <div className={styles.section}>
                  <p className={styles.sectionLabel}>Cover Letter</p>
                  <p className={styles.sectionText}>{selected.cover_note}</p>
                </div>
              )}
            </div>
          </>
        ) : (
          <p className={styles.placeholder}>Select an application to view details</p>
        )}
      </div>

      {deleteTarget && (
        <ConfirmModal
          message={`Delete application from "${deleteTarget.applicant_name}"?`}
          onConfirm={() => { deleteMutation.mutate(deleteTarget.id); setDeleteTarget(null) }}
          onCancel={() => setDeleteTarget(null)}
        />
      )}
      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}

function Row({ label, value }) {
  return (
    <div style={{ marginBottom: '12px' }}>
      <p style={{ fontSize: '11px', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '2px' }}>{label}</p>
      <p style={{ fontSize: '14px' }}>{value}</p>
    </div>
  )
}

function fmtDate(iso) {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}
