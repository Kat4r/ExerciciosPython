class Banco:

    def __init__(self,nome,saldo=0,limite=750):
        self.nome = nome
        self.__saldo = saldo
        self.__limite = limite
        self.__saques = []

        if self.__saldo < 0:
            self.__saldo = 0

        if self.__limite < 0:
            self.__limite = 0

    def set_deposito(self,valor):
        if valor > 0:
            self.__saldo += valor
            self.__saques.append(f"Deposito: {valor}")


    def sacar(self,valor):
        if valor >= 0:
            if valor > self.__saldo:
                return f"Impossivel sacar um valor acima do saldo"
            self.__saldo -= valor
            self.__saques.append(f"Saque: {valor}")


    def extrato(self):
        print(f"Saldo Atual: {self.__saldo}\n")
        for saque in self.__saques:
            print(saque)






