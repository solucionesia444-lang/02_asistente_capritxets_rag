import './App.css'

function App() {
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
        </section>

        <form className="chat-form">
          <input
            type="text"
            placeholder="Escribe tu pregunta..."
            aria-label="Escribe tu pregunta"
          />
          <button type="submit">Enviar</button>
        </form>
      </section>
    </main>
  )
}

export default App