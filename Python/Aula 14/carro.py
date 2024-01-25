class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("Já está ligado")
        else: 
            print("Carro ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro desligado")
            self.ligado = False
        else:
            print("Já desligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade}KM/H")
        else:
            print("Carro desligado, não pode acelerar")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade}KM/H")
        else:
            print("Carro desligado, não pode frear")