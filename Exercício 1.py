class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def ligar(self):
        return f'O carro {self.marca}, modelo {self.modelo} {self.ano} está ligado.'
    
    def Acelerar(self):
        return f'O carro {self.marca}, modelo  {self.modelo} {self.ano} Você está pisando fundo.'
    def Desligar(self):    
        return f'O carro {self.marca}, modelo {self.modelo} {self.ano} está Desligado.'
if __name__ == "__main__":
    Gol = Carro("volkswagen", "GTI", "2015")
    Onix = Carro("JST-3725", "Onix", "2015")

    print(Gol.ligar())
    
    print(Gol.Acelerar())

    print(Gol.Desligar())

    #kddjdjdjdjdjd