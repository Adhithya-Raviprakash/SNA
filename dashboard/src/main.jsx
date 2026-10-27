import { Component } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './styles.css'

// Shows the error instead of a blank page if rendering ever fails.
class ErrorBoundary extends Component {
  state = { error: null }
  static getDerivedStateFromError(error) { return { error } }
  render() {
    if (!this.state.error) return this.props.children
    return <div className="crash" role="alert"><h2>Something went wrong</h2><p>The dashboard hit an error while drawing this network.</p><pre>{this.state.error.message}</pre><button className="primary" onClick={() => location.reload()}>Reload dashboard</button></div>
  }
}

createRoot(document.getElementById('root')).render(<ErrorBoundary><App /></ErrorBoundary>)
