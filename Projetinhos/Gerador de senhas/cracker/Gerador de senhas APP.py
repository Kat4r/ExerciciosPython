import random
import string
import time
import PySimpleGUI as sg


seg_baixa = string.ascii_letters + string.digits
seg_media = string.ascii_letters + string.punctuation
seg_alta = string.printable


def gerar_senha(seguranca, tamanho):
    senha_gerada = ''
    if seguranca == 0:
        for i in range(tamanho):
            senha_gerada += str(random.choice(seg_baixa)).strip()
    elif seguranca == 1:
        for i in range(tamanho):
            senha_gerada += str(random.choice(seg_media)).strip()
    elif seguranca == 2:
        for i in range(tamanho):
            senha_gerada += str(random.choice(seg_alta)).strip()
    return senha_gerada


layout = [
    [sg.Text('Escolha o nível de segurança da senha')],
    [sg.Radio('Levemente Segura', "nivel", default=True, key='seg_baixa'),
     sg.Radio('Segura', "nivel", key='seg_media'),
     sg.Radio('Muito Segura', "nivel", key='seg_alta')],
    [sg.Text('Digite o comprimento da senha a ser gerada (entre 4 e 24):'), sg.InputText(key='tamanho')],
    [sg.Button('Gerar Senha')],
    [sg.Output(size=(60, 10))],
]

window = sg.Window('Gerador de Senhas', layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    seguranca = 0
    if values['seg_media']:
        seguranca = 1
    elif values['seg_alta']:
        seguranca = 2
    tamanho = int(values['tamanho'])
    if tamanho < 4 or tamanho > 24:
        print('Parâmetros incorretos! O comprimento da senha deve ser entre 4 e 24.')
    else:
        senha_gerada = gerar_senha(seguranca, tamanho)
        print('Senha gerada: {}'.format(senha_gerada))
        bancoSenhas = open('senhas.txt', 'a')
        bancoSenhas.write(senha_gerada)
        bancoSenhas.write('\n')

window.Close()