from pathlib import Path
from funcoes.campos import extrair_cnpj

# escolher um dos arquivos .txt gerados pelo ETL
caminho_txt = Path("saida") / "teste_ocr.txt" # troque o nome se precisar

if not caminho_txt.exists():
	print(f"Arquivo {caminho_txt} não encontrado.")
else:
	texto = caminho_txt.read_text(encoding="utf-8", errors="ignore")
	cnpj = extrair_cnpj(texto)

	print("CNPJ encontrado:", cnpj)
