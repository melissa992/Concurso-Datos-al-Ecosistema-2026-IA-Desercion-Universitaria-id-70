import { Link } from "react-router-dom";

function FormPage() {
  return (
    <main className="form-page">
      <section className="form-card">
        <div className="form-header">
          <p className="eyebrow">Próxima etapa</p>
          <h2>Registro de información del estudiante</h2>
          <p>
            Este formulario está listo para recibir datos en futuras iteraciones
            del proyecto.
          </p>
        </div>

        <form className="student-form">
          <div className="field-group">
            <label htmlFor="name">Nombre completo</label>
            <input
              id="name"
              name="name"
              type="text"
              placeholder="Ej. Ana María López"
            />
          </div>
          <div className="field-group">
            <label htmlFor="program">Programa académico</label>
            <input
              id="program"
              name="program"
              type="text"
              placeholder="Ej. Ingeniería de Sistemas"
            />
          </div>
          <div className="field-group">
            <label htmlFor="notes">Observaciones</label>
            <textarea
              id="notes"
              name="notes"
              rows="4"
              placeholder="Agrega información relevante para el análisis futuro."
            />
          </div>
        </form>

        <div className="actions">
          <Link to="/" className="secondary-btn">
            Volver
          </Link>
          <button type="button" className="primary-btn" disabled>
            Guardar (próximamente)
          </button>
        </div>
      </section>
    </main>
  );
}

export default FormPage;
