class BasePessoa:

    def __init__(self, nome, idade, sexo):
        self.nome = nome.title()
        self.idade = idade
        self.acao = False
        self.falar = False
        self.sexo = sexo.title()
        self.endereco = []

    def set_endereco(self,endereco):
        self.endereco.append(endereco)


    def realizar_acao(self, acao):
        if self.falar:
            print(f"{self.nome} está falando.")
            return
        print(f"{self.nome} está {acao}")
        self.acao = True


    def parar_acao(self):
        if not self.acao:
            print(f"{self.nome} não está fazendo nada")
            return
        print(f"{self.nome} parou de fazer o que estava fazendo")
        self.acao = False


    def falar_algo(self, frase):
        if self.acao:
            print(f"{self.nome} está ocupado.")
            return
        print(f"{self.nome} disse {frase}")
        self.falar = True


    def parar_falar(self):
        if not self.falar:
            return f"{self.nome} está quieto"

        self.falar = False
        return f"{self.nome} parou de falar"



    @classmethod
    def gerar_pessoa_rand(cls):
        from modulos.libtestes import testespy as tpy
        sexo = tpy.choice(['m', 'f'])
        nome = tpy.nomesRand(sexo)
        idade = tpy.idadeRand()
        return cls(nome,idade,sexo)


class Animal(BasePessoa):

    def __init__(self, nome, idade, sexo, som, cor):
        super().__init__(nome, idade, sexo)
        self.som = som
        self.cor = cor
        self.raca = False


    def emitir_som(self):
        if self.som:
            print(f"{self.nome} está falando: {self.som}")

    def mostrar_raca(self):
        if not self.raca:
            self.raca = "Vira-lata"
            return print(f"{self.nome} é {self.raca}")
        print(f"{self.nome} é da raça {self.raca}")


    def mostrar_cor(self):
        if self.cor:
            print(f"A cor de {self.nome} é {self.cor}")
            return
        print(f"{self.nome} não tem dados de cor informado")

    def info_animal(self):
        if not self.raca:
            self.raca = 'Vira-lata'
        return  f"O animal {self.nome} é um {self.raca} e possui {self.idade} anos"


class Funcionario(BasePessoa):

    def __init__(self, nome, idade, sexo, cargo, trabalhar=False):
        self.cargo = cargo
        self.trabalhar = trabalhar
        super().__init__(nome, idade, sexo)


    def set_trabalhar(self):
        if not self.trabalhar:
            print(f"{self.nome} começou a trabalhar")
            self.trabalhar = True
            return
        print(f"{self.nome} já está trabalhando")


    def parar_trabalhar(self):
        if not self.trabalhar:
            return print(f"{self.nome} não está trabalhando")
        print(f"{self.nome} parou de fazer o que estava fazendo")
        self.trabalhar = False

class Gerente(Funcionario):

    def __init__(self, nome, idade, sexo, cargo,departamento):
        self.departamento = departamento
        super().__init__(nome, idade, sexo, cargo)


class Empresa:

    def __init__(self,nome,endereco):
        self.endereco = endereco
        self.nome = nome


class Cliente:
     def __init__(self,nome,idade,cpf):
         self.nome = nome
         self.idade = idade
         self.cpf = cpf

class Pedido:

    def __init__(self,cliente,produto,quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

class PessoaFisica(BasePessoa):

    def __init__(self, nome, idade, sexo, cpf):
        self.cpf = cpf
        super().__init__(nome, idade, sexo)

class PessoaJuridica(BasePessoa):

    def __init__(self, nome, idade, sexo, cnpj):
        self.cnpj = cnpj
        super().__init__(nome, idade, sexo)

class Professor(PessoaFisica):

    def __init__(self, nome, idade, sexo, cpf, disciplina, salario):
        self.disciplina = disciplina
        self.salario = salario
        super().__init__(nome, idade, sexo, cpf)

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.disciplina}")

class Aluno(BasePessoa):

    def __init__(self, nome, idade, sexo, matricula):
        self.matricula = matricula
        super().__init__(nome, idade, sexo)

    def estudar(self):
        print(f"{self.nome} está assistindo à aula")

class Turma:

    def __init__(self):
        self.professores = []
        self.alunos = []


    def set_professor(self,professor):
        self.professores.append(professor)


    def set_aluno(self,aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)

    def mostrar_escola(self):
        for aluno in self.alunos:
            print(f"Aluno: {aluno.nome}")

        for prof in self.professores:
            print(f"Professor: {prof.nome} | Matéria: {prof.disciplina}")

class Agenda:

    def __init__(self):
        self.compromissos = []

    def set_compromisso(self,*compromisso):
        for item in compromisso:
            self.compromissos.append(item)

    def remover_compromissoITEM(self, compromisso):
        try:
            self.compromissos.remove(compromisso)
        except:
            return print(f"O compromisso {compromisso} não está na lista ou já foi removido.")
    def remover_compromissoINDICE(self, valor):
        try:
            self.compromissos.pop(valor-1)
        except:
            return print(f"O indice {valor} não está na lista ou já foi removido.")

    def mostrar_compromissos(self):
        for item in self.compromissos:
            print(item)


class Paciente(BasePessoa):

    def __init__(self, nome, idade, sexo, enfermidade):
        self.enfermidade = enfermidade
        super().__init__(nome, idade, sexo)

class Medico(BasePessoa):

    def __init__(self, nome, idade, sexo, especialidade, crm):
        self.especialidade = especialidade
        self.crm = crm
        super().__init__(nome, idade, sexo)


class Consulta:

    def __init__(self,paciente,medico,data_e_hora):
        self._paciente = paciente
        self._medico = medico
        self.datahora = data_e_hora
        self.consulta = False

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico


    def set_consulta(self):
        if not self.consulta:
            self.consulta = True
            return f"o paciente {self.paciente} marcou uma consulta com o médico {self.medico}"
        return f"o paciente {self.paciente} já tem uma consulta marcada."

    def desmarcar_consulta(self):
        if self.consulta:
            self.consulta = False
            return f"o paciente {self.paciente} desmarcou a consulta"
        return f"o paciente {self.paciente} não tem nenhuma consulta marcada"


class Compra:

    def __init__(self,cliente,data):
        self.cliente = cliente
        self.data = data
        self.valorTotal = 0
        self.itens = []

    def set_item(self,**item):
        self.itens.append(item)

    def remover_item(self,item):
        self.itens[0].pop(item)

    def somar_itens(self):
        return sum(self.itens[0].values())




