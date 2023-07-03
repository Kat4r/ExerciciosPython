def horariofuncionamento():
    from datetime import datetime
    hora = datetime.now().hour
    minuto = datetime.now().minute
    if hora > 22 or hora < 6:
        return exit()
    print(f"Horário atual {hora:02d}:{minuto:02d}\n")

def interface():
    frase = f"Bem vindo(a) ao \033[34mBig Ass Bank!\033[m"
    print("-" * int(len(frase.replace("\033[34m", '').replace('\033[m)', ''))+6))
    print(frase.center(46))
    print("-" * int(len(frase.replace("\033[34m", '').replace('\033[m)', ''))+6))
    print()

def converterLimite(valor):
    try:
        if valor == '':
            valor.strip()
            return int(valor)

    except:
        pass
