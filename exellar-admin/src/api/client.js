import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

const client = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
})

// Attach JWT token from localStorage
client.interceptors.request.use((config) => {
  const token = localStorage.getItem('exellar_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Auto logout on 401
client.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem('exellar_token')
      localStorage.removeItem('exellar_user')
      window.location.href = '/login'
    }
    return Promise.reject(err)
  },
)

export default client
