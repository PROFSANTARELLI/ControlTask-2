import os
import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no sys.path para imports como 'backend.main'.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Usa um banco SQLite temporário para os testes e o limpa a cada execução.
os.environ.setdefault("CONTROLTASK_DATABASE_URL", "sqlite:///./backend/test_controltask.db")
TEST_DB_PATH = ROOT / "backend" / "test_controltask.db"
if TEST_DB_PATH.exists():
    TEST_DB_PATH.unlink()
