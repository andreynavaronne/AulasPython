from carro import Carro

fusca = Carro("Volkswagen", "Fusca", "Azul", "Gasolina")

fusca.ligar()

while fusca.velocidade < 20:
    fusca.acelerar()

while fusca.velocidade > 0:
    fusca.frear()

fusca.desligar()