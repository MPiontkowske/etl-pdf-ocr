import re


def extrair_cnpj(texto: str) -> str | None:
    """
    Procura um CNPJ no texto e retorna o primeiro encontrado.
    Formatos aceitos: 00.000.000/0000-00 ou só números.
    """
    # 1) padrão com máscara: 00.000.000/0000-00
    padrao_mascarado = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"

    encontrado = re.search(padrao_mascarado, texto)
    if encontrado:
        return encontrado.group(0)

    # 2) padrão só dígitos: 14 números seguidos
    padrao_numerico = r"\b\d{14}\b"

    encontrado = re.search(padrao_numerico, texto)
    if encontrado:
        return encontrado.group(0)

    return None

