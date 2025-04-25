# 🧾 Conversor XLSX para CSV em Python

Este projeto é um conversor simples e eficiente de arquivos `.xlsx` para `.csv`, desenvolvido em Python. Ideal para automatizar a conversão de relatórios e planilhas, especialmente quando há múltiplos arquivos envolvidos.

## 🚀 Funcionalidades

- ✅ Converte todos os arquivos `.xlsx` de uma pasta para `.csv`
- ✅ Mantém a estrutura dos dados das planilhas
- ✅ Utiliza `openpyxl` em modo `read_only` para otimizar a leitura
- ✅ Exibe barra de progresso com `tqdm`
- ✅ Cria automaticamente a pasta de saída (se não existir)
- ✅ Tratamento de erros durante o processo de conversão

## 🛠️ Requisitos

- Python 3.6+
- [openpyxl](https://pypi.org/project/openpyxl/)
- [tqdm](https://pypi.org/project/tqdm/)

### Instalação das dependências

```bash
pip install openpyxl tqdm
