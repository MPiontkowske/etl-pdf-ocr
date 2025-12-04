from PIL import Image, ImageFilter, ImageOps

def preprocessar_imagem(img: Image.Image) -> Image.Image:
	"""Melhora a qualidade da imagem para ORC."""

	# 1. Converter para escala de cinza
	img = img.convert("L")

	# 2. Aumentar contraste
	img = ImageOps.autocontrast(img)

	# 3. Aplicar filtro para reduzir ruído
	#img = img.filter(ImageFilter.MedianFilter(size=3))

	# 4. Aumentar nitidez
	#img = img.filter(ImageFilter.SHARPEN)

	return img
