import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import client from '../api/client.js'
import Toast from '../components/Toast.jsx'
import styles from './Form.module.css'

const INITIAL = {
  title: '',
  summary: '',
  body: '',
  thumbnail: '',
  category: '',
  author: 'Exellar Team',
  is_published: false,
}

const CATEGORIES = ['Construction', 'Innovation', 'Sustainability', 'Safety', 'Company News', 'Projects']

export default function ArticleForm() {
  const { id } = useParams()
  const navigate = useNavigate()
  const qc = useQueryClient()
  const isEdit = Boolean(id)
  const [form, setForm] = useState(INITIAL)
  const [uploading, setUploading] = useState(false)
  const [toast, setToast] = useState(null)

  const { data: existing } = useQuery({
    queryKey: ['admin-article', id],
    queryFn: () => client.get('/api/admin/articles').then(r => r.data.find(a => a.id === id)),
    enabled: isEdit,
  })

  useEffect(() => {
    if (existing) setForm({ ...INITIAL, ...existing })
  }, [existing])

  function set(key, val) { setForm(prev => ({ ...prev, [key]: val })) }

  async function handleThumbnailChange(e) {
    const file = e.target.files[0]
    if (!file) return
    setUploading(true)
    try {
      const fd = new FormData()
      fd.append('image', file)
      const res = await client.post('/api/admin/upload', fd)
      set('thumbnail', res.data.filename)
    } catch { setToast({ message: 'Upload failed', type: 'error' }) }
    finally { setUploading(false) }
  }

  const saveMutation = useMutation({
    mutationFn: () => isEdit
      ? client.put(`/api/admin/articles/${id}`, form)
      : client.post('/api/admin/articles', form),
    onSuccess: () => {
      qc.invalidateQueries(['admin-articles'])
      navigate('/articles')
    },
    onError: () => setToast({ message: 'Save failed', type: 'error' }),
  })

  return (
    <div className={styles.shell}>
      <h1 className={styles.heading}>{isEdit ? 'Edit Article' : 'New Article'}</h1>

      <div className={styles.form}>
        <label className={styles.label}>Title *</label>
        <input className={styles.input} value={form.title} onChange={e => set('title', e.target.value)} placeholder="Article title" />

        <label className={styles.label}>Category</label>
        <select className={styles.input} value={form.category} onChange={e => set('category', e.target.value)}>
          <option value="">— Select category —</option>
          {CATEGORIES.map(c => <option key={c} value={c}>{c}</option>)}
        </select>

        <label className={styles.label}>Author</label>
        <input className={styles.input} value={form.author} onChange={e => set('author', e.target.value)} placeholder="Author name" />

        <label className={styles.label}>Summary</label>
        <textarea className={styles.textarea} rows={3} value={form.summary} onChange={e => set('summary', e.target.value)} placeholder="Short description shown on the articles listing page" />

        <label className={styles.label}>Body (HTML or plain text)</label>
        <textarea className={styles.textarea} rows={14} value={form.body} onChange={e => set('body', e.target.value)} placeholder="Full article content..." />

        <label className={styles.label}>Thumbnail</label>
        <input type="file" accept="image/*" onChange={handleThumbnailChange} className={styles.input} />
        {uploading && <p className={styles.hint}>Uploading…</p>}
        {form.thumbnail && (
          <img
            src={`${import.meta.env.VITE_API_BASE || 'http://localhost:5000'}/api/uploads/images/${form.thumbnail}`}
            alt="thumbnail preview"
            style={{ maxWidth: 220, marginTop: 8, borderRadius: 6 }}
          />
        )}

        <label className={styles.label} style={{ display: 'flex', alignItems: 'center', gap: 10, cursor: 'pointer' }}>
          <input type="checkbox" checked={form.is_published} onChange={e => set('is_published', e.target.checked)} />
          Publish immediately
        </label>

        <div className={styles.btnRow}>
          <button className={styles.save} onClick={() => saveMutation.mutate()} disabled={saveMutation.isPending || !form.title}>
            {saveMutation.isPending ? 'Saving…' : isEdit ? 'Save Changes' : 'Create Article'}
          </button>
          <button className={styles.cancel} onClick={() => navigate('/articles')}>Cancel</button>
        </div>
      </div>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
