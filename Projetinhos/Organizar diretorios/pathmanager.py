def manager(path):
    from pathlib import Path
    from shutil import move

    path = Path("J:\\Downloads")

    for arqv in path.glob("*"):
        if arqv.suffix == ".mp3":
            move(arqv, "J:\\Downloads\\Musicas")
        elif arqv.suffix == ".png" or arqv.suffix == ".jpg" or arqv.suffix == ".jpeg":
            move(arqv, "J:\\Downloads\\Fotos")
        elif arqv.suffix == ".pdf" or arqv.suffix == ".txt":
            move(arqv, "J:\\Downloads\\Documentos")
        elif arqv.suffix == '.mp4':
            move(arqv, "J:\\Downloads\\Videos")
        elif arqv.suffix == ".rar" or arqv.suffix == ".zip" or arqv.suffix == ".7z":
            move(arqv, "J:\\Downloads\\Arquivos Comprimidos")
        elif arqv.suffix:
            move(arqv, "J:\\Downloads\\Outros")



"""try:

        os.mkdir("J:\\Downloads\\Musicas")
        os.mkdir("J:\\Downloads\\Fotos")
        os.mkdir("J:\\Downloads\\Documentos")
        os.mkdir("J:\\Downloads\\Videos")
        os.mkdir("J:\\Downloads\\Outros")


    except Exception as erro:
        print(erro)
"""
