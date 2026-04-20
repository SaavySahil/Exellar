import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import styles from './Dashboard.module.css'

function useCount(url) {
  return useQuery({
    queryKey: [url],
    queryFn: () => client.get(url).then(r => r.data.length),
  })
}

export default function Dashboard() {
  const projects     = useCount('/api/admin/projects')
  const jobs         = useCount('/api/admin/jobs')
  const applications = useCount('/api/admin/applications')

  const cards = [
    { label: 'Projects',     value: projects.data,     to: '/projects' },
    { label: 'Job Listings', value: jobs.data,         to: '/jobs' },
    { label: 'Applications', value: applications.data, to: '/applications' },
  ]

  return (
    <div>
      <h1 className={styles.heading}>Dashboard</h1>
      <div className={styles.grid}>
        {cards.map(c => (
          <Link key={c.label} to={c.to} className={styles.card}>
            <span className={styles.count}>
              {c.value ?? '—'}
            </span>
            <span className={styles.cardLabel}>{c.label}</span>
          </Link>
        ))}
      </div>

      <div className={styles.links}>
        <h2 className={styles.sub}>Quick Actions</h2>
        <div className={styles.btnRow}>
          <Link to="/projects/new" className={styles.action}>+ New Project</Link>
          <Link to="/jobs/new"     className={styles.action}>+ New Job</Link>
        </div>
      </div>
    </div>
  )
}
