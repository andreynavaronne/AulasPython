i = 1
while i < 10:
  print(i)
  i += 1

print("Terminou")

lista = ["Andrey", "Talita", "Nathan"]

for i in lista:
   print(i)

nome_completo = "Andrey di Navaronne Gaudencio Leite"

for letra in nome_completo:
    if letra.upper() != "E" and letra.upper() != "A" :
       print(letra)

for letras in range(len(nome_completo)):
    if (letras % 3) == 0:
        print(nome_completo[letras])
    
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]   

for linha in matriz:
    print("-----")
    for numero in linha:
        if numero % 2 == 0:
            print(numero)