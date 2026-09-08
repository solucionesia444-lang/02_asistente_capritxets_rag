import {useState} from 'react'
import './App.css'

function App() {
  const [ query, setQuery] = useState('')

  const [messages, setMessages] = useState([])

  const handleSubmit = async (event) => {
  event.preventDefault()

  if (!query.trim()) {
    return
  }
  
  setMessages([...messages, { role: 'user', content: query }])
  setQuery('')
  
  const response = await fetch('http://127.0.0.1:8000/rag', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query }),
  })

  const data = await response.json()
  
setMessages((currentMessages) => [
  ...currentMessages,
  { role: 'assistant', content: data.answer },
])
  console.log(data)

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
          </section>

        <form className="chat-form" onSubmit={handleSubmit}>
          <input
              type="text"
              placeholder="Escribe tu pregunta..."
              aria-label="Escribe tu pregunta"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
            />
          <button type="submit">Enviar</button>
        </form>
      </section>
    </main>
  )
}

export default App