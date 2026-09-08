import {useEffect, useRef, useState} from 'react'
import './App.css'
const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'

function App() {
  const [ query, setQuery] = useState('')

  const [messages, setMessages] = useState([])

  const [isLoading, setIsLoading] = useState(false)

  const [error, setError] = useState(null)

  const messagesEndRef = useRef(null)

  const inputRef = useRef(null)

  useEffect(() => {
  messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading, error])

  const handleSubmit = async (event) => {
  event.preventDefault()

  if (!query.trim() || isLoading) {
    return
  }
  
  setIsLoading(true)
  setError('')
  setMessages([...messages, { role: 'user', content: query }])
  setQuery('')

  try { 
  const response = await fetch(`${API_URL}/rag`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query }),
  })

  if (!response.ok) {
    throw new Error('Error al consultar el asistente')
  }

  const data = await response.json()

setMessages((currentMessages) => [
  ...currentMessages,
  { role: 'assistant', content: data.answer },
])
}

catch {
  setError('No hemos podido obtener una respuesta. Inténtalo de nuevo.')
} finally {
  setIsLoading(false)
  inputRef.current?.focus()
}
  console.log('Consulta enviada:', query)
}

  return (
    <main className="app-shell">
      <section className="chat-card">
        <header className="chat-header">
          <h1>Asistente Capritxets</h1>
          <p>Pregúntame sobre productos, horarios, pedidos o alérgenos.</p>
        </header>

        <section className="chat-messages">
            <article className="message assistant-message">
              Hola, soy tu asistente virtual de Capritxets. ¿En qué puedo ayudarte?
            </article>

            {messages.map((message, index) => (
              <article
                key={index}
                className={`message ${
                  message.role === 'user' ? 'user-message' : 'assistant-message'
                }`}
              >
                {message.content}
              </article>
            ))}

            {isLoading && (
              <article className="message assistant-message">
                 Escribiendo...
                </article>
                )}

            {error && (
              <article className="message error-message">
                {error}
              </article>
            )}
          <div ref={messagesEndRef} />  
          </section>

        <form className="chat-form" onSubmit={handleSubmit}>
          <input
              ref={inputRef}
              type="text"
              placeholder="Escribe tu pregunta..."
              aria-label="Escribe tu pregunta"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              disabled={isLoading}
            />
          <button type="submit" disabled={isLoading || !query.trim()}>
            {isLoading ? 'Enviando...' : 'Enviar'}
          </button>
        </form>
      </section>
    </main>
  )
}

export default App