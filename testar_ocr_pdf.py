from pathlib import Path
from funcoes.ocr import ocr_pdf

caminho = Path("entrada")/"teste_ocr.pdf"

if not caminho.exists():
	print(f"Arquivo {caminho} não encontrado.")
else:
	texto = ocr_pdf(caminho)
	print("=== TEXTO OCR DO PDF  ===")
	print(texto)

