# ETL Inteligente de PDF com OCR (Python)

Pipeline profissional para extração de texto de PDFs combinando:

- Extração nativa com **PyPDF2**
- OCR automático com **Tesseract**
- Conversão PDF → Imagem com **pdf2image**
- Pré-processamento inteligente de imagem com **Pillow**
- Fallback automático (OCR só quando necessário)
- Estrutura modular para escalabilidade
- Tratamento de erros por arquivo
- Registro de logs
- Preparado para integração com banco de dados

---

## 🧠 Arquitetura do Projeto

etl_pdf/
├── entrada/ # PDFs para processar
├── saida/ # Textos extraídos
├── logs/ # Registros automáticos
├── funcoes/
│ ├── extrair.py # Extrator nativo + fallback OCR
│ ├── limpar.py # Sanitização do texto
│ ├── ocr.py # Funções de OCR (imagem + PDF)
│ └── preprocessar.py # Filtros de imagem
├── executar.py # Pipeline principal
├── README.md

---

## 🚀 Como executar o ETL

### 1. Criar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate

