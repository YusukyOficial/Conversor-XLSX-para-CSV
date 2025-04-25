import os
import openpyxl
import csv
from tqdm import tqdm

# Defina as pastas de entrada e saída
input_folder = r'Caminho da pasta de Relatorio (Entrada)'
output_folder = r'Caminho da pasta de Relatorio (Saida)'

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Lista apenas arquivos .xlsx
xlsx_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

# Inicia a barra de progresso
print("Iniciando conversão de .xlsx para .csv...\n")

for filename in tqdm(xlsx_files, desc="Convertendo arquivos", unit="arquivo"):
    xlsx_path = os.path.join(input_folder, filename)
    csv_path = os.path.join(output_folder, filename.replace('.xlsx', '.csv'))

    try:
        # Abre o arquivo .xlsx
        workbook = openpyxl.load_workbook(xlsx_path, read_only=True)  # Modo read_only para otimizar
        sheet = workbook.active  # Usando a primeira aba (planilha ativa)

        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Itera sobre as linhas da planilha (read_only mode)
            for row in sheet.iter_rows(values_only=True):
                writer.writerow(row)

        print(f"✅ Convertido com sucesso: {filename}")

    except Exception as e:
        print(f"❌ Erro ao converter {filename}: {e}")

print("\n✅ Todos os arquivos foram convertidos com sucesso!")
