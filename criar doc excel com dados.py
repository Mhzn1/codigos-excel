import openpyxl

# Cria uma nova planilha
workbook = openpyxl.Workbook()

# Seleciona a planilha ativa
worksheet = workbook.active

# Adiciona alguns dados na planilha
worksheet["A1"] = "Nome"
worksheet["B1"] = "Idade"
worksheet["C1"] = "E-mail"

worksheet["A2"] = "João"
worksheet["B2"] = 25
worksheet["C2"] = "joao@email.com"

worksheet["A3"] = "Maria"
worksheet["B3"] = 30
worksheet["C3"] = "maria@email.com"

# Salva a planilha
workbook.save("dados.xlsx")
