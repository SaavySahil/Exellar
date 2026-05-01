import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import StatusBadge from '../components/StatusBadge.jsx'
import { SkeletonRow } from '../components/Skeleton.jsx'
import ConfirmModal from '../components/ConfirmModal.jsx'
import { useToast } from '../context/ToastContext.jsx'
import styles from './ListPage.module.css'

export default function Jobs() {
  const qc = useQueryClient()
  const addToast = useToast()
  const [deleteTarget, setDeleteTarget] = useState(null)
  const [search, setSearch] = useState('')

  const { data: jobs = [], isLoading } = useQuery({
    queryKey: ['admin-jobs'],
    queryFn: () => client.get('/api/admin/jobs').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/jobs/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-jobs'])
      addToast('Job deleted', 'success')
    },
    onError: () => addToast('Delete failed', 'error'),
  })

  const q = search.toLowerCase()
  const filtered = jobs.filter(j =>
    j.title?.toLowerCase().includes(q) || j.department?.toLowerCase().includes(q)
  )

  return (
    <div>
      <div className={styles.header}>
        <h1 className={styles.heading}>Job Listings</h1>
        <Link to="/jobs/new" className={styles.addBtn}>+ Add Job</Link>
      </div>

      <div className={styles.toolbar}>
        <input
          className={styles.search}
          placeholder="Search jobs…"
          value={search}
          onChange={e => setSearch(e.target.value)}
          aria-label="Search jobs"
        />
        {search && <span className={styles.searchCount}>{filtered.length} result{filtered.length !== 1 ? 's' : ''}</span>}
      </div>

      {isLoading ? (
        <div className={styles.table}>
          {Array.from({ length: 5 }).map((_, i) => <SkeletonRow key={i} cols={5} />)}
        </div>
      ) : (
        <div className={styles.table}>
          <div className={`${styles.row} ${styles.thead}`}>
            <span className={styles.title}>Title</span><span>Department</span><span>Type</span><span>Status</span><span className={styles.actions}>Actions</span>
          </div>
          {filtered.map(j => (
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
          {filtered.length === 0 && <p className={styles.empty}>{search ? 'No results found.' : 'No job listings yet.'}</p>}
        </div>
      )}

      {deleteTarget && (
        <ConfirmModal
          message={`Delete "${deleteTarget.title}"?`}
          onConfirm={() => { deleteMutation.mutate(deleteTarget.id); setDeleteTarget(null) }}
          onCancel={() => setDeleteTarget(null)}
        />
      )}
    </div>
  )
}
