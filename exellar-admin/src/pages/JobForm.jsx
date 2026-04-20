import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import client from '../api/client.js'
import Toast from '../components/Toast.jsx'
import styles from './Form.module.css'

const INITIAL = {
  title: '', department: '', location: '',
  type: 'full-time', description: '', requirements: '', is_active: true,
}

export default function JobForm() {
  const { id } = useParams()
  const navigate = useNavigate()
  const qc = useQueryClient()
  const isEdit = Boolean(id)
  const [form, setForm] = useState(INITIAL)
  const [toast, setToast] = useState(null)

  const { data: existing } = useQuery({
    queryKey: ['job', id],
    queryFn: () => client.get('/api/admin/jobs').then(r => r.data.find(j => j.id === id)),
    enabled: isEdit,
  })

  useEffect(() => {
    if (existing) {
      const sanitized = { ...INITIAL }
      Object.keys(INITIAL).forEach(key => {
        sanitized[key] = existing[key] ?? INITIAL[key]
      })
      setForm(sanitized)
    }
  }, [existing])

  function set(key, val) { 
    const safeVal = val ?? ''
    setForm(prev => ({ ...prev, [key]: safeVal })) 
  }

  const saveMutation = useMutation({
    mutationFn: () => isEdit
      ? client.put(`/api/admin/jobs/${id}`, form)
      : client.post('/api/admin/jobs', form),
    onSuccess: () => {
      qc.invalidateQueries(['admin-jobs'])
      navigate('/jobs')
    },
    onError: err => setToast({ message: err.response?.data?.error || 'Save failed', type: 'error' }),
  })

  return (
    <div>
      <h1 className={styles.heading}>{isEdit ? 'Edit Job' : 'New Job'}</h1>
      <div className={styles.form}>

        <div className={styles.row2}>
          <div className={styles.field}>
            <label className={styles.label}>Title *</label>
            <input className={styles.input} value={form.title}
              onChange={e => set('title', e.target.value)} required />
          </div>
          <div className={styles.field}>
            <label className={styles.label}>Department</label>
            <input className={styles.input} value={form.department}
              onChange={e => set('department', e.target.value)} placeholder="e.g. Engineering" />
          </div>
        </div>

        <div className={styles.row2}>
          <div className={styles.field}>
            <label className={styles.label}>Location</label>
            <input className={styles.input} value={form.location}
              onChange={e => set('location', e.target.value)} placeholder="e.g. Mumbai" />
          </div>
          <div className={styles.field}>
            <label className={styles.label}>Type</label>
            <select className={styles.input} value={form.type}
              onChange={e => set('type', e.target.value)}>
              <option value="full-time">Full-Time</option>
              <option value="part-time">Part-Time</option>
              <option value="contract">Contract</option>
            </select>
          </div>
        </div>

        <div className={styles.field}>
          <label className={styles.label}>Description</label>
          <textarea className={styles.textarea} rows={5} value={form.description}
            onChange={e => set('description', e.target.value)}
            placeholder="Describe the role and responsibilities…" />
        </div>

        <div className={styles.field}>
          <label className={styles.label}>Requirements</label>
          <textarea className={styles.textarea} rows={4} value={form.requirements}
            onChange={e => set('requirements', e.target.value)}
            placeholder="List qualifications and skills…" />
        </div>

        <div className={styles.checkRow}>
          <input type="checkbox" id="active" checked={form.is_active}
            onChange={e => set('is_active', e.target.checked)} />
          <label htmlFor="active" className={styles.checkLabel}>Active (visible on Careers page)</label>
        </div>

        <div className={styles.formActions}>
          <button type="button" className={styles.cancel}
            onClick={() => navigate('/jobs')}>Cancel</button>
          <button type="button" className={styles.save}
            onClick={() => saveMutation.mutate()}
            disabled={saveMutation.isPending}>
            {saveMutation.isPending ? 'Saving…' : 'Save Job'}
          </button>
        </div>
      </div>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
