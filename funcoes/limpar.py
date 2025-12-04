def limpar_texto(texto: str) -> str:
	"""Limpa e normaliza o texto extraido do PDF."""
	# Quebrar em linhas
	linhas = texto.splitlines()

	linhas_limpa = []

	for linha in linhas:
		# Remover espaços extras no início/fim
		l = linha.strip()

		# Ignorar linhas vazias
		if not l:
			continue

		# Trocar miltiplos expaços por um só
		while "  " in l:
			l = l.replace("  "," ")

		linhas_limpa.append(l)

	# Junsta tudo de novo com quenras de linha
	return "\n".join(linhas_limpa)
	
