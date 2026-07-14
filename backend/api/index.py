import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
backend_path = ROOT / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

from app.main import app  # noqa: E402,F401
