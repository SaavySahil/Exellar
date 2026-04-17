import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import StatusBadge from '../components/StatusBadge.jsx'
import ConfirmModal from '../components/ConfirmModal.jsx'
import Toast from '../components/Toast.jsx'
import styles from './ListPage.module.css'

export default function Articles() {
  const qc = useQueryClient()
  const [deleteTarget, setDeleteTarget] = useState(null)
  const [toast, setToast] = useState(null)

  const { data: articles = [], isLoading } = useQuery({
    queryKey: ['admin-articles'],
    queryFn: () => client.get('/api/admin/articles').then(r => r.data),
  })

  const deleteMutation = useMutation({
    mutationFn: id => client.delete(`/api/admin/articles/${id}`),
    onSuccess: () => {
      qc.invalidateQueries(['admin-articles'])
      setToast({ message: 'Article deleted', type: 'success' })
    },
    onError: () => setToast({ message: 'Delete failed', type: 'error' }),
  })

  return (
    <div>
      <div className={styles.header}>
        <h1 className={styles.heading}>Blog Articles</h1>
        <Link to="/articles/new" className={styles.addBtn}>+ New Article</Link>
      </div>

      {isLoading ? (
        <p className={styles.loading}>Loading…</p>
      ) : (
        <div className={styles.table}>
          <div className={`${styles.row} ${styles.thead}`}>
            <span>Title</span><span>Category</span><span>Author</span><span>Status</span><span>Published</span><span>Actions</span>
          </div>
          {articles.map(a => (
            <div key={a.id} className={styles.row}>
              <span className={styles.title}>{a.title}</span>
              <span className={styles.muted}>{a.category || '—'}</span>
              <span className={styles.muted}>{a.author}</span>
              <span><StatusBadge value={a.is_published ? 'published' : 'draft'} /></span>
              <span className={styles.muted}>{a.published_at ? fmtDate(a.published_at) : '—'}</span>
              <span className={styles.actions}>
                <Link to={`/articles/${a.id}/edit`} className={styles.edit}>Edit</Link>
                <button className={styles.del} onClick={() => setDeleteTarget(a)}>Delete</button>
              </span>
            </div>
          ))}
          {articles.length === 0 && (
            <p className={styles.loading}>No articles yet. Create your first one.</p>
          )}
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

function fmtDate(iso) {
  return new Date(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}
