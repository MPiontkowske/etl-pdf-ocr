from pathlib import Path
from PIL import Image
import pytesseract


def ocr_imagem(caminho_imagem: Path, lang: str = "por+eng") -> str:
	"""Aplica ORC em uma imagem e retorna o texto reconhecido."""
	img = Image.open(caminho_imagem)
	texto = pytesseract.image_to_string(img, lang=lang)
	return texto

from pdf2image import convert_from_path
from funcoes.preprocessar import preprocessar_imagem

def ocr_pdf(caminho_pdf: Path, lang: str = "por+eng") -> str:
	"""Executa OCR em todas as paginas de um PDF (escaneado)."""
	
	# 1. PDF -> lista de imagns (uma por página)
	imagens = convert_from_path(caminho_pdf)
	texto_paginas = []

	# 2. Para cada imagem, aplicar OCR
	for img in imagens:
		img = preprocessar_imagem(img) # <--- PRE-PROCESSAMENTO
		texto = pytesseract.image_to_string(img, lang=lang)
		texto_paginas.append(texto)

	# 3. Juntar tudo
	return "\n".join(texto_paginas)
