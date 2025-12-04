from pathlib import Path
from datetime import datetime

PASTA_LOGS = Path(__file__).resolve().parents[1] / "logs"
PASTA_LOGS.mkdir(exist_ok=True)

CAMINHO_LOG = PASTA_LOGS / "etl_pdf.log"

def registrar(mensagem: str):
	"""Registra uma mensagem no arquivo de log com timestamp."""
	agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	linha = f"[{agora}] {mensagem}\n"
	with CAMINHO_LOG.open("a", encoding="utf-8") as f:
		f.write(linha)
