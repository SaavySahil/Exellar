import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import StatusBadge from '../components/StatusBadge.jsx'
import ConfirmModal from '../components/ConfirmModal.jsx'
import Toast from '../components/Toast.jsx'
import styles from './ListPage.module.css'

export default function Projects() {
  const qc = useQueryClient()
  const [deleteTarget, setDeleteTarget] = useState(null)
  const [toast, setToast] = useState(null)

  const { data: projects = [], isLoading } = useQuery({
    queryKey: ['admin-projects'],
    queryFn: () => client.get('/api/admin/projects').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/projects/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-projects'])
      setToast({ message: 'Project deleted', type: 'success' })
    },
    onError: () => setToast({ message: 'Delete failed', type: 'error' }),
  })

  function confirmDelete(project) { setDeleteTarget(project) }
  function handleDelete() {
    deleteMutation.mutate(deleteTarget.id)
    setDeleteTarget(null)
  }

  return (
    <div>
      <div className={styles.header}>
        <h1 className={styles.heading}>Projects</h1>
        <Link to="/projects/new" className={styles.addBtn}>+ Add Project</Link>
      </div>

      {isLoading ? (
        <p className={styles.loading}>Loading…</p>
      ) : (
        <div className={styles.table}>
          <div className={`${styles.row} ${styles.thead}`}>
            <span className={styles.title}>Title</span><span>Category</span><span>Status</span><span>Featured</span><span className={styles.actions}>Actions</span>
          </div>
          {projects.map(p => (
            <div key={p.id} className={styles.row}>
              <span className={styles.title}>{p.title}</span>
              <span className={styles.muted}>{p.category || '—'}</span>
              <span><StatusBadge value={p.status} /></span>
              <span>{p.is_featured ? '★' : ''}</span>
              <span className={styles.actions}>
                <Link to={`/projects/${p.id}/edit`} className={styles.edit}>Edit</Link>
                <button className={styles.del} onClick={() => confirmDelete(p)}>Delete</button>
              </span>
            </div>
          ))}
          {projects.length === 0 && <p className={styles.empty}>No projects yet.</p>}
        </div>
      )}

      {deleteTarget && (
        <ConfirmModal
          message={`Delete "${deleteTarget.title}"? This cannot be undone.`}
          onConfirm={handleDelete}
          onCancel={() => setDeleteTarget(null)}
        />
      )}
      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
