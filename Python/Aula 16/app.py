from openpyxl import Workbook
from openpyxl import load_workbook

np = load_workbook("test.xlsx")
tabela = np.active

nomes = ["Andrey", "Nathan", "Talita", "Morgana"]
sobrenomes = ["Di Navaronne", "Di Navaronne", "Durand", "Gaudencio"]
idades = [28, 0, 30, 50]
saldo = [12, 0, 100, 1000]

for i in range(len(nomes)):
    tabela[f"A{i+1}"] = nomes[i]
    tabela[f"B{i+1}"] = sobrenomes[i]
    tabela[f"C{i+1}"] = idades[i]
    tabela[f"D{i+1}"] = saldo[i]
np.save("test.xlsx")