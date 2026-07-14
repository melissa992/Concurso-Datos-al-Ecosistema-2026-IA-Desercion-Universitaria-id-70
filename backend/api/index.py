import sys
from pathlib import Path

# En Vercel, el root del proyecto es la raíz del repositorio
# backend/api/index.py -> subimos 3 niveles para llegar a la raíz
BASE_DIR = Path(__file__).resolve().parents[2]

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# También agregamos backend/ al path
BACKEND_DIR = Path(__file__).resolve().parent.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.main import app