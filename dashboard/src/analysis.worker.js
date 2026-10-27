import { analyze } from './network'

// Runs the analysis off the main thread so the loading animation keeps moving.
self.onmessage = ({ data }) => {
  try { self.postMessage({ ok: true, result: analyze(data) }) }
  catch (error) { self.postMessage({ ok: false, error: error.message }) }
}
