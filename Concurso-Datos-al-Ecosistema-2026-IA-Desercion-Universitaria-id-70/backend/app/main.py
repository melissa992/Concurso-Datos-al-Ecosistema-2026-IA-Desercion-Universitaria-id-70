import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api import router as api_router

app = FastAPI(
    title="EduPredict IA API",
    version="0.1.0",
    description="API base para futuras funcionalidades de predicción educativa",
)

# La URL de producción se puede fijar por variable de entorno (FRONTEND_URL)
# para no tener que tocar código cada vez que cambia el dominio de Vercel.
# También se acepta cualquier preview de Vercel del proyecto (*.vercel.app)
# a través de allow_origin_regex.
_extra_origin = os.getenv("FRONTEND_URL")
_allow_origins = [
    "https://concurso-datos-al-ecosistema-2026-i-seven.vercel.app",
    "https://concurso-datos-al-ecosistema-2026-i-sigma.vercel.app",
    "http://localhost:5173",
]
if _extra_origin and _extra_origin not in _allow_origins:
    _allow_origins.append(_extra_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allow_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok", "message": "EduPredict IA Backend funcionando"}


@app.get("/api")
def api_root():
    return {"status": "ok", "message": "API root"}


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend listo para expandirse"}