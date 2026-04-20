import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import StatusBadge from '../components/StatusBadge.jsx'
import ConfirmModal from '../components/ConfirmModal.jsx'
import Toast from '../components/Toast.jsx'
import styles from './ListPage.module.css'

export default function Jobs() {
  const qc = useQueryClient()
  const [deleteTarget, setDeleteTarget] = useState(null)
  const [toast, setToast] = useState(null)

  const { data: jobs = [], isLoading } = useQuery({
    queryKey: ['admin-jobs'],
    queryFn: () => client.get('/api/admin/jobs').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/jobs/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-jobs'])
      setToast({ message: 'Job deleted', type: 'success' })
    },
    onError: () => setToast({ message: 'Delete failed', type: 'error' }),
  })

  return (
    <div>
      <div className={styles.header}>
        <h1 className={styles.heading}>Job Listings</h1>
        <Link to="/jobs/new" className={styles.addBtn}>+ Add Job</Link>
      </div>

      {isLoading ? (
        <p className={styles.loading}>Loading…</p>
      ) : (
        <div className={styles.table}>
          <div className={`${styles.row} ${styles.thead}`}>
            <span className={styles.title}>Title</span><span>Department</span><span>Type</span><span>Status</span><span className={styles.actions}>Actions</span>
          </div>
          {jobs.map(j => (
            <div key={j.id} className={styles.row}>
              <span className={styles.title}>{j.title}</span>
              <span className={styles.muted}>{j.department || '—'}</span>
              <span><StatusBadge value={j.type} /></span>
              <span><StatusBadge value={j.is_active ? 'active' : 'inactive'} /></span>
              <span className={styles.actions}>
                <Link to={`/jobs/${j.id}/edit`} className={styles.edit}>Edit</Link>
                <button className={styles.del} onClick={() => setDeleteTarget(j)}>Delete</button>
              </span>
            </div>
          ))}
          {jobs.length === 0 && <p className={styles.empty}>No job listings yet.</p>}
        </div>
      )}

      {deleteTarget && (
        <ConfirmModal
          message={`Delete "${deleteTarget.title}"?`}
          onConfirm={() => { deleteMutation.mutate(deleteTarget.id); setDeleteTarget(null) }}
          onCancel={() => setDeleteTarget(null)}
        />
      )}
      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
