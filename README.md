# ETL Inteligente de PDF (Python + OCR)

Pipeline profissional de extração de texto de PDF usando:

- PyPDF2 (extração nativa)
- Tesseract OCR (fallback para PDFs escaneados)
- Pré-processamento de imagem (Pillow)
- Estrutura modular (funções separadas)
- Logs, tratamento de erro e limpeza de texto

## Estrutura do Projeto
etl_pdf/
├── entrada/ # PDFs para processar
├── saida/ # Textos extraídos
├── logs/ # Logs do ETL
├── funcoes/ # Funções do pipeline
│ ├── extrair.py
│ ├── limpar.py
│ ├── ocr.py
│ └── preprocessar.py
├── executar.py # Pipeline principal
├── README.md

## Como rodar

1. Ativar ambiente virtual  
2. Instalar dependências  
3. Colocar PDFs na pasta `entrada/`  
4. Executar:

```bash
python3 executar.py

