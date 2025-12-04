from PyPDF2 import PdfReader
from pathlib import Path

def extrair_texto_pdf(caminho_pdf: Path) -> str:
	"""Extrai o texto de um PDF e retorna como string.
	Se der erro, a exception sobe para quem chamou.	
	"""
	leitor = PdfReader(caminho_pdf)
	texto_paginas = []
		
	for pagina in leitor.pages:
		conteudo = pagina.extract_text() or ""
		texto_paginas.append(conteudo)

	return "\n".join(texto_paginas)

from funcoes.ocr import ocr_pdf

def extrair_texto_pdf_inteligente(caminho_pdf: Path) -> str:
	"""Tentar extrair texto nativo; se vir pouco texto, usa OCR como fallback."""

	# 1.  Primeiro tentar extração "normal"
	leitor = PdfReader(caminho_pdf)
	texto_paginas = []

	for pagina in leitor.pages:
		conteudo = pagina.extract_text() or ""
		texto_paginas.append(conteudo)

	texto = "\n".join(texto_paginas)
	texto_limpo = texto.strip()

	# Se texto normal já veio razoável, retorna
	if len(texto_limpo) > 80:
		return texto

	# Senão, tenta OCR como plano B
	texto_ocr = ocr_pdf(caminho_pdf)
	return texto_ocr
