familia = ["Andrey", "Talita", "Nathan"]

print(familia[0])
print(familia[-1])
print(familia[0:])
print(familia[-3:-1])

familia.extend(["Alcicleia", "Benedito", "Morgana", "Carlo"])
familia.insert(2, "Pedrita")
familia.append("Céu")
familia.remove("Carlo")

print(familia)
print(familia.count("Andrey"))

idades = [28, 30, 10, 0, 60, 61, 50, 1]
print(idades)
idades.sort()
print(idades)
familia.sort()
idades.reverse()
print(idades)
print(familia)

coordenadas = (-49, -36)
print(coordenadas)
print(coordenadas[0])