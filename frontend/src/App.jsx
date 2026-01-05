import { useState, useEffect } from 'react'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setMessage(data.status))
      .catch(err => console.error(err))
  }, [])

  return (
    <div>
      <h1>Cosmo Frontend</h1>
      <p>Backend status: {message}</p>
    </div>
  )
}

export default App
