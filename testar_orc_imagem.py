from pathlib import Path
from funcoes.ocr import ocr_imagem

caminho = Path("entrada")/"teste_ocr.png"

if not caminho.exists():
	print(f"Arquivo {caminho} não encontrado.")
else:
	texto = ocr_imagem(caminho)
	print("=== TEXTO RECONHECIDO ==")
	print(texto)
