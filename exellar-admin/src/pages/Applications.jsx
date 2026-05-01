import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import client from '../api/client.js'
import ConfirmModal from '../components/ConfirmModal.jsx'
import { useToast } from '../context/ToastContext.jsx'
import styles from './Applications.module.css'

export default function Applications() {
  const qc = useQueryClient()
  const addToast = useToast()
  const [selected, setSelected] = useState(null)
  const [deleteTarget, setDeleteTarget] = useState(null)

  const { data: applications = [], isLoading } = useQuery({
    queryKey: ['admin-applications'],
    queryFn: () => client.get('/api/admin/applications').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/applications/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-applications'])
      addToast('Application deleted', 'success')
      if (selected?.id === deleteTarget?.id) setSelected(null)
    },
    onError: () => addToast('Delete failed', 'error'),
  })

  async function downloadResume(app) {
    try {
      const res = await client.get(`/api/admin/applications/${app.id}/resume`, { responseType: 'blob' })
      const url = URL.createObjectURL(res.data)
      const a = document.createElement('a')
      a.href = url
      a.download = `resume-${app.applicant_name.replace(/\s+/g, '-')}.pdf`
      a.click()
      URL.revokeObjectURL(url)
    } catch {
      addToast('Failed to download resume', 'error')
    }
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
    </div>
  )
}

function Row({ label, value }) {
  return (
    <div className={styles.rowItem}>
      <p className={styles.rowLabel}>{label}</p>
      <p className={styles.rowValue}>{value}</p>
    </div>
  )
}

function fmtDate(iso) {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}
