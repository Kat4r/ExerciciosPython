class Pessoa:

    def __init__(self,nome,idade,profissao=False):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao
        if not self.profissao:
            self.profissao = 'Desempregado'

    def dados(self):
        print(f"Olá me chamo {self.nome}\n"
              f"Tenho {self.idade} anos\n"
              f"Trabalho como {self.profissao}")


class Carro:

    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._cor = None

    @property
    def cor(self):
        return self._cor


    @cor.setter
    def cor(self,cor):
        self._cor = cor

    def mostrar_dados(self):
        print(f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano: {self.ano}\n", end='')
        print(f"Cor: {self._cor}" if self._cor is not None else "Cor não informada")


class Circulo:

    def __init__(self,area):
        self.area = area

    def calcularArea(self):
        pass