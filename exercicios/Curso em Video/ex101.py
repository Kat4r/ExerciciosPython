from datetime import datetime
def voto(nascimento):
    """
    verificador de obrigatoriedade com a eleição

    :param nascimento: idade de nascimento
    :return: será retornado uma frase de acordo com seu direito ao voto
    """

    anoAtual = datetime.now().year

    if anoAtual - nascimento <= 15:
        return "Você ainda não tem direito ao voto"
    elif anoAtual - nascimento < 18 or anoAtual - nascimento >= 70:
        return "O seu voto é opcional"
    elif anoAtual - nascimento >= 18 or anoAtual - nascimento < 70:
        return "O seu voto é obrigatório"


direitoVoto = voto(int(input("Digite sua data de nascimento para verificar seu direito ao voto: ")))
print(direitoVoto)

