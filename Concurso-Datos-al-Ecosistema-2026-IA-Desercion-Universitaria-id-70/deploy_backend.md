# Despliegue del backend FastAPI

## 1. Usar Railway / Render / Heroku

### Opción recomendada: Railway
1. Crea una cuenta en https://railway.app/
2. Conecta tu repositorio GitHub: `melissa992/Concurso-Datos-al-Ecosistema-2026-IA-Desercion-Universitaria-id-70`
3. Selecciona el proyecto y el directorio raíz del repo.
4. Configura el servicio:
   - Framework: Python
   - Comando de instalación: `pip install -r requirements.txt`
   - Comando de inicio: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
5. Define variables de entorno si las necesitas.

### Opción alternativa: Render
1. Crea cuenta en https://render.com/
2. New -> Web Service -> Connect GitHub repo.
3. Root Directory: deja la raíz del repo.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`

### Opción alternativa: Heroku
1. Crea cuenta en https://heroku.com/
2. Crea app nueva.
3. Conecta GitHub al repo.
4. Asegúrate de que exista `Procfile` con:
   `web: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
5. Buildpacks: Python.

## 2. Configurar Vercel frontend con backend remoto
1. En Vercel, abre el proyecto del frontend.
2. Ve a Settings -> Environment Variables.
3. Crea variable:
   - Key: `VITE_API_URL`
   - Value: `https://<TU_BACKEND_URL>/api`
   - Environment: Production
4. Guarda y redeploy.

## 3. Probar
a. Frontend: `https://concurso-datos-al-ecosistema-2026-i-seven.vercel.app`
b. Backend: `https://<TU_BACKEND_URL>/api/health`

## 4. Notas
- El frontend ya usa `import.meta.env.VITE_API_URL || "http://localhost:8000/api"`.
- En producción, Vercel usará la URL del backend remoto.
