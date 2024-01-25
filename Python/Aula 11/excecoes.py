try:
 numero = int(input("Digite um número: "))
 resultado = 10/numero
 print(resultado)

except ZeroDivisionError:
 print("Essa divisão tende ao infinito")

except ValueError:
 print("Digite um valor válido")

except:
 print("Erro inesperado")

finally:
 print("Até mais!")