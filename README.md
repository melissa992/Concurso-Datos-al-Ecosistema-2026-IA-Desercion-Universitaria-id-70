# CM IA

## Observatorio Inteligente para el Análisis y Predicción de la Deserción Universitaria

CM IA es una plataforma desarrollada para el concurso **Datos al Ecosistema 2026 – IA para Colombia**, en la categoría **Educación – Nivel Intermedio**.

La solución integra datos abiertos del portal **datos.gov.co**, análisis estadístico y modelos de Inteligencia Artificial para apoyar la detección temprana de riesgo de deserción universitaria.

---

## Estructura del proyecto

- `frontend/` - aplicación web con React y Vite.
- `backend/` - API con FastAPI y Uvicorn.
- `README.md` - documentación del proyecto.

---

## Tecnologías principales

- React 18
- Vite
- React Router
- FastAPI
- Uvicorn
- Python 3

---

## Cómo ejecutar el proyecto

### 1. Instalar dependencias

Desde la carpeta raíz:

```powershell
cd "c:\Users\melyocoro\Desktop\Concurso Datos abiertos grupo 70\Concurso-Datos-al-Ecosistema-2026-IA-Desercion-Universitaria-id-70\frontend"
npm install
```

Desde `backend`:

```powershell
cd "c:\Users\melyocoro\Desktop\Concurso Datos abiertos grupo 70\Concurso-Datos-al-Ecosistema-2026-IA-Desercion-Universitaria-id-70\backend"
pip install -r requirements.txt
```

### 2. Ejecutar el frontend

```powershell
cd frontend
npm run dev
```

Visita `http://localhost:5173`.

### 3. Ejecutar el backend

```powershell
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visita `http://localhost:8000/docs` para la documentación de la API.

---

## Componentes del proyecto

- Interfaz web para visualizar y consultar información sobre deserción.
- Endpoint REST para servir datos y modelos desde FastAPI.
- Diseño enfocado en educación, análisis e inteligencia artificial.

---

## Conjuntos de datos utilizados

Datos abiertos consultados desde `datos.gov.co`, incluyendo información de deserción académica y no académica para educación superior.

- DESERCION ACADEMICA PREGRADO Y POSGRADO
- Deserción no académica 1-2019
- Deserción no académica 2-2019

---

## Estado actual

- ✅ Frontend inicial con homepage y formulario
- ✅ Backend básico con FastAPI
- 🚧 Proyecto en desarrollo

---

## Notas importantes

- El proyecto se puede ampliar con conexión a base de datos y carga de modelos de Machine Learning.
- Asegúrate de ejecutar `npm install` en `frontend` y `pip install -r requirements.txt` en `backend` antes de iniciar.
