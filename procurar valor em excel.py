import openpyxl

# Carrega a planilha
workbook = openpyxl.load_workbook('dados.xlsx')

# Seleciona a planilha ativa
worksheet = workbook.active

# Procura o valor "João" na coluna A
for row in worksheet.iter_rows(min_row=2, min_col=1, max_col=1):
    for cell in row:
        if cell.value == "João":
            print("O valor foi encontrado na linha", cell.row)