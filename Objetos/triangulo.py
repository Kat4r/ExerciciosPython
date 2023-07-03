class FormasGeometricas():
    def __init__(self,largura,altura=0):
        self.largura = largura
        self.altura = altura

    def perimetro(self):
        return (self.altura*2) + (self.largura*2)

    def raio(self):
        return self.largura / 2

    def area(self, circulo=False):
        return (self.largura * self.altura) if not circulo else (3.14 * self.raio()) **2

    def circunferencia(self):
        return (2 * 3.14) * self.raio()

class Vetor:

    def __init__(self):
        self._x = []
        self._y = []
        self.__listaAdd = []
        self.__listaSub = []


    @property
    def set_x(self):
        return self._x
    @set_x.setter
    def set_x(self,valor):
        self._x = valor

    @property
    def set_y(self):
        return self._y

    @set_y.setter
    def set_y(self, valor):
        self._y = valor

    def mostrar_vetores(self):
        print(self._x)
        print(self._y)


    def somar_vetores(self):
        while len(self._y) < len(self._x):
            self._y.append(0)
        while len(self._x) < len(self._y):
            self._x.append(0)

        for pos, i in enumerate(self._x):
            self.__listaAdd.append(i + self._y[pos])
        return self.__listaAdd

    def subtrair_vetores(self):
        while len(self._y) < len(self._x):
            self._y.append(0)
        while len(self._x) < len(self._y):
            self._x.append(0)

        for pos, i in enumerate(self._x):
            self.__listaSub.append(i - self._y[pos])
        return self.__listaSub

    def ext_vetores(self):
        return self._y + self._x


class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return (self.lado + self.lado) * 2

    def perimetro(self):
        return self.area() * 2



class Cubo(Quadrado):

    def __init__(self, lado, altura):
        self.altura = altura
        super().__init__(lado)

    def volume(self):
        return self.lado * self.lado * self.altura


class Ponto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self):
        if self.x - self.y < 0 or self.x - self.y >= 0 :
            return f"A distancia entre os pontos {self.x} e {self.y} é de {abs(self.x - self.y)}"


class Pilha:

    def __init__(self, *valores):
        self.valores = []
        for valor in valores:
            self.valores.append(valor)

    def empilhar(self, *valores):
        for valor in valores:
            self.valores.append(valor)

    def mostrar_pilha(self):
        return f"A Pilha está da seguinte forma {self.valores}"


    def desempilhar(self):
        maiorValor = max(self.valores)
        self.valores.remove(maiorValor)
        return f"O Maior valor foi removido da pilha: {maiorValor}"

    def primeiro(self):
        return f"{self.valores[0]} é o primeiro item da pilha"

    def organizar(self):
        return sorted(self.valores)

class Fila:

    def __init__(self, *valores):
        self.valores = [valor for valor in valores]

    def inserir(self, valor):
        self.valores.insert(0, valor)

    def remover(self):
        self.valores.pop()

    def primeiro(self):
        return self.valores[0]


#class Conjunto:   certo, isso aqui é um set()

class Arvore:

    def __init__(self,chave=None,esquerda=None,direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return "%s <- %s -> %s" % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

    def set_numero(self,raiz,nodo):
        if not raiz:
            raiz = nodo

        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo

            else:
                self.set_numero(raiz.direita, nodo)
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo

            else:
                self.set_numero(raiz.esquerda, nodo)




















