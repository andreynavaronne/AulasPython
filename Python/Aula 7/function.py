def soma(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def calcular(num1, num2):
    print (soma(num1, num2))
    print (sub(num1, num2))  

calcular(9, 4)

def maior(lista_num):
    lista_num.sort()
    lista_num.reverse()
    return lista_num[0]

lista = [0, 4, 4, 2, 6, 3, 7]
print(maior(lista))