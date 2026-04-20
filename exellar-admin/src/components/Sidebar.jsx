import { NavLink, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'
import styles from './Sidebar.module.css'

const NAV = [
  { to: '/dashboard',    label: 'Dashboard',     icon: '□' },
  { to: '/projects',     label: 'Projects',       icon: '○' },
  { to: '/jobs',         label: 'Jobs',           icon: '◇' },
  { to: '/applications', label: 'Applications',   icon: '▤' },
  { to: '/articles',     label: 'Blog Articles',  icon: '✎' },
]

export default function Sidebar({ onClose }) {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  function handleLogout() {
    logout()
    navigate('/login')
  }

  function handleNavClick() {
    if (onClose) onClose()
  }

  return (
    <aside className={styles.sidebar}>
      <div className={styles.brand}>
        <div className={styles.brandTop}>
          <img
            src="/exellar-logo.png"
            alt="Exellar Construction LLP"
            className={styles.brandLogo}
          />
          {onClose && (
            <button className={styles.closeBtn} onClick={onClose}>×</button>
          )}
        </div>
      </div>

      <nav className={styles.nav}>
        {NAV.map(({ to, label, icon }) => (
          <NavLink
            key={to}
            to={to}
            onClick={handleNavClick}
            className={({ isActive }) =>
              `${styles.link} ${isActive ? styles.active : ''}`
            }
          >
            <span className={styles.icon}>{icon}</span>
            {label}
          </NavLink>
        ))}
      </nav>

      <div className={styles.footer}>
        <p className={styles.userEmail}>{user?.email}</p>
        <button className={styles.logout} onClick={handleLogout}>
          Logout
        </button>
      </div>
    </aside>
  )
}
