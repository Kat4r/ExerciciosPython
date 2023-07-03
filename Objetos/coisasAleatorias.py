class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano = ano
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f"o livro {self.titulo} foi emprestado"
        return f"Não é possivel emprestar o livro {self.titulo} pois ele ja foi emprestado"

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f"O livro {self.titulo} foi devolvido"
        return f"O livro {self.titulo} não está com ninguém"


    def info_livro(self):
        return f"Titulo: \033[34m{self.titulo}\033[m\n" \
               f"Autor: \033[34m{self.autor}\033[m\n" \
               f"Ano: \033[34m{self.ano}\033[m"


class Biblioteca:

    def __init__(self):
        self.biblioteca = []

    def listar_livros(self):
        for livro in self.biblioteca:
            print(livro.info_livro())
            print("-"*20)


    def armazenar_livro(self, *livro):
        for item in livro:
            self.biblioteca.append(item)

    def buscar_por_autor(self,autor):
        livrosAutor = []
        for item in self.biblioteca:
            if item.autor.lower() == autor.lower():
                livrosAutor.append(item)
        print(f"Livros do autor: {autor}")
        for livros in livrosAutor:
            print(livros.info_livro())
            print("-"*25)


class Banco:

    def __init__(self,nome, endereco):
        self.nome = nome
        self.endereco = endereco

    class Conta:
        
        def __init__(self,titular,saldo,limite):
            self.titular = titular
            self.saldo = saldo
            self.limite = limite

        def depositar(self,valor):
            return self.saldo + valor


        def sacar(self,valor):
            novoSaldo = self.saldo - valor
            if novoSaldo >= 0 and valor < self.limite:
                self.saldo = novoSaldo
                return print(f"Você fez um saque de {valor}, seu novo saldo é de {self.saldo}")
            if valor > self.limite:
                return print(f'Seu saque não pode ser maior que o limite de saque de sua conta, limite atual R${self.limite}')

        def usar_limite(self):
            if self.saldo - self.limite < 0:
                return f"impossivel concluir transação"
            else:
                self.saldo = self.saldo - self.limite
                return self.saldo


    class Poupanca(Conta):

        def __init__(self,titular,saldo,limite,juros):
            self.juros = juros
            super().__init__(titular,saldo,limite)


        def calcular_juros(self):
            return (self.saldo * self.juros) / 100

        def aplicar_juros(self):
            self.saldo = self.saldo + (self.saldo * self.juros) / 100
            return self.saldo


class Moveis:
    def __init__(self):
        pass


    class Cadeira:
        def __init__(self, material):
            self.material = material

    class Mesa:
        def __init__(self, tamanho):
            self.tamanho = tamanho


class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._fabricante = []
        self._motor = []


    def set_motor(self,nomeMotor):
        self._motor.append(Motor(nomeMotor))

    def set_fabricante(self,nomeFab):
        self._fabricante.append(Fabricante(nomeFab))

    def mostrar_dados(self):

        print(f"Veiculo: {self.nome}")
        for dado in self._fabricante:
            print(f"Fabricante: {dado.nome}")

        for dado in self._motor:
            print(f"Motorização: {dado.nome}")


class Motor:
    def __init__(self,nome):
        self.nome = nome
        self.fabricante = []

    def fabricante(self,nomeFab):
        self.fabricante.append(Fabricante(nomeFab))


class Fabricante:
    def __init__(self,nome):
        self.nome = nome


class Veiculo:
    def __init__(self, marca, modelo, ano,spd_limit):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self.movimentacao = False
        self.velocidade = 0
        self.spd_limit = spd_limit


    def set_acelerar(self):
        if not self.movimentacao:
            self.velocidade += 25
            self.movimentacao = True
            return f"O {self._modelo} começou a acelerar"

        elif self.velocidade < self.spd_limit:
            self.velocidade += 25
            while self.velocidade > self.spd_limit:
                self.velocidade -= 1
            return f"O {self._modelo} está acelerando mais. Velocidade atual {self.velocidade}"

        else:
            return f"O veiculo {self._modelo} já atingiu sua velocidade maxima de {self.spd_limit}"

    def set_freiar(self):
        if not self.velocidade:
            return f"O veiculo {self._modelo} está parado"

        self.acelerar = False
        self.velocidade -= 15
        if self.velocidade < 0:
            self.velocidade = 0
            return f"{self._modelo} parou."
        return f"{self._modelo} começou freiar. Velocidade atual {self.velocidade}"




    def mostrar_info(self):
        print()
        print(f"{self._marca}\n"
              f"{self._modelo}\n"
              f"{self._ano}")


class Moto(Veiculo):

    def __init__(self, marca, modelo, ano, spd_limit,cilindrada):
        self.cilindrada = cilindrada
        super().__init__(marca, modelo, ano, spd_limit)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"{self.cilindrada}")


class Caminhao(Veiculo):

    def __init__(self, marca, modelo, ano, spd_limit, limite_carga):
        self.limite_carga = limite_carga
        self.carga = 0
        super().__init__(marca, modelo, ano, spd_limit)


    def set_carga(self, qt_carga):
        if qt_carga > 0:
            peso_disponivel = self.limite_carga - self.carga
            if qt_carga <= peso_disponivel:
                self.carga += qt_carga
                return f"{self._modelo} adicionou {qt_carga} kg de carga. Ainda restam {self.limite_carga - self.carga} kg de limite."
            else:
                return f"Peso excede o limite disponível, limite disponivel: {peso_disponivel}."
        else:
            return "Peso inválido. Insira um valor positivo."


class veiculoEletrico(Veiculo):

    def __init__(self, marca, modelo, ano, spd_limit,autonomia):
        self.autonomia = autonomia
        self.bateria = 5
        super().__init__(marca, modelo, ano, spd_limit)

    def carregar_bateria(self):
        while self.bateria < 100:
            self.bateria += 1
        return f"Bateria carregada"

    def conferir_bateria(self):
        if self.bateria == 100:
            return f"A bateria está totalmente carregada"
        elif self.bateria > 15 and self.bateria < 100:
            return f"Estado atual da bateria: {self.bateria}"
        elif self.bateria <= 15:
            return f"\033[31mBateria em estado critico, carregue o mais rapido possivel: {self.bateria}\033[m"


class Bicicleta:

    def __init__(self,marca,modelo,tamanho_roda):
        self.marca = marca
        self.modelo = modelo
        self.tamanhoRoda = tamanho_roda
        self.movimentacao = False
        self.velocidade = 0



    def set_pedalar(self):
        if not self.movimentacao:
            self.velocidade += 2
            self.movimentacao = True
            return f"A bicicleta {self.modelo} começou a ser pedalada"

        elif self.velocidade < 15:
            self.velocidade += 2
            while self.velocidade > 15:
                self.velocidade -= 1
            return f"A {self.modelo} está acelerando mais. Velocidade atual {self.velocidade}"
        else:
            return f"A bicicleta {self.modelo} já atingiu sua velocidade maxima de {15}Kmh"

    def set_freiar(self):
        if not self.velocidade:
            return f"O veiculo {self.modelo} está parado"

        self.acelerar = False
        self.velocidade -= 5
        if self.velocidade <= 0:
            self.velocidade = 0
            return f"{self.modelo} parou."
        return f"{self.modelo} começou freiar. Velocidade atual {self.velocidade}"


class Motorizacao:

    def __init__(self, potencia, combustivel):
        self.potencia = potencia
        self.combustivel = combustivel
        self.motor_ligado = False

    def ligar_motor(self):
        if not self.motor_ligado:
            from time import sleep
            self.motor_ligado = True
            return f"Ligando motor...\n" \
                   f"Motor ligado."
        return f"O motor já está ligado"

    def desligar_motor(self):
        if self.motor_ligado:
            self.motor_ligado = False
            return f"Desligando motor...\n" \
                   f"Motor desligado"
        return f"O motor já está desligado."


class Carro2(Motorizacao):

    def __init__(self, potencia, combustivel):
        self.tanque = 0
        self.tanque_limite = 50
        super().__init__(potencia, combustivel)

    def set_combustivel(self, litragem):
        if litragem > 0:
            disponivel = self.tanque_limite - self.tanque
            if litragem <= disponivel:
                self.tanque += litragem
                return f"Foi adicionado {litragem}1litros no canto de combustivel, ainda restam {self.tanque_limite - self.tanque}"
            else:
                return f"Não há limite no tanque para adicionar mais combustivel, quantidade atual {self.tanque}"
        else:
            raise ValueError

















