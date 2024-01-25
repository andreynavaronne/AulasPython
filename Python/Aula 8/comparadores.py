tenho_sede = True

if tenho_sede:
    print("Beber agua")
else:
    print("vida que segue")

esta_frio = True

if esta_frio:
    print("Põe casaco")
else:
    print("Tira casaco")

tenho_fome = False

if tenho_sede or tenho_fome:
    print("Vou na cozinha")
else:
    print("Continuo deitado") 

if tenho_sede and tenho_fome:
    print("PRECISO ir na cozinha")
else:
    print("Talvez espere mais um pouco")

if tenho_sede and tenho_fome:
    print("Suco e batatinha")
elif tenho_sede and not(tenho_fome):
    print("Suquinho")
elif not(tenho_sede) and tenho_fome:
    print("Batatinha")
else:
    print("Vou ficar deitado")

num1 = 2
num2 = 1

if num1 == num2:
    print("São iguais")
elif num1 > num2:
    print("Número 1 é maior")
else:
    print("Número 2 é maior")