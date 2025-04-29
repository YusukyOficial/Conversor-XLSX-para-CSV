<p align="center">
  <img src="banner.png" alt="Banner Conversor XLSX para CSV" width="300"/>
</p>


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
```

## 📂 Como usar
- Clone este repositório:

```bash
git clone https://github.com/YusukyOficial/nome-do-repo.git
cd nome-do-repo
```

- No arquivo Python, edite os caminhos das variáveis:

```bash
input_folder = r'Caminho da pasta de Relatorio (Entrada)'
output_folder = r'Caminho da pasta de Relatorio (Saida)'
```

- Execute o script:

``` bash
python conversor.py
```

- Os arquivos .csv convertidos serão salvos na pasta de saída indicada.

## 📁 Estrutura esperada

```bash
📂 Entrada/
   ├── arquivo1.xlsx
   ├── arquivo2.xlsx
   └── ...
📂 Saida/
   ├── arquivo1.csv
   ├── arquivo2.csv
   └── ...
```

## 🧠 Observações

- O script considera apenas a primeira aba de cada arquivo .xlsx.
- As conversões preservam apenas os valores das células, sem formatações.

---

Desenvolvido com 💚 por [YusukyOficial](https://github.com/YusukyOficial)
