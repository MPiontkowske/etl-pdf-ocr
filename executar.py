from pathlib import Path
from funcoes.extrair import extrair_texto_pdf_inteligente
from funcoes.limpar import limpar_texto
from funcoes.log import registrar

pasta_entrada = Path("entrada")
pasta_saida = Path("saida")

for pdf in pasta_entrada.glob("*.pdf"):
	print(f"Extraindo: {pdf.name}")
	registrar(f"Iniciando extração de {pdf.name}")
	try:
		texto = extrair_texto_pdf_inteligente(pdf)
		texto = limpar_texto(texto)
	except Exception as e:
		mensagem_erro = f"ERRO ao processar {pdf.name}: {e}"
		print(mensagem_erro)
		registrar(mensagem_erro)
		# continue = pula este PDF e vai para o próximo
		continue

	caminho_saida = pasta_saida / f"{pdf.stem}.txt"

	with caminho_saida.open("w", encoding="utf-8") as f:
		f.write(texto)

	print(f"✔ Salvo em : {caminho_saida}")
	registrar(f"Concluido: {caminho_saida}")
