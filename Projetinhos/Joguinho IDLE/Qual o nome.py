import PySimpleGUI as sg


sg.theme('Dark Blue 3')

layout = [[sg.Text('Recursos:'), sg.Text('0', key='_RECURSOS_')],
          [sg.Button('Gerar recursos'), sg.Button('Melhorar produção')],
          [sg.Text('Produção:'), sg.Text('1', key='_PRODUCAO_')],
          [sg.Button('Sair')]]

window = sg.Window('Jogo Idle', layout)

recursos = 0
producao = 1

while True:
    event, values = window.read(timeout=1000)
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    if event == 'Gerar recursos':
        recursos += producao
        window['_RECURSOS_'].update(recursos)
    if event == 'Melhorar produção':
        if recursos >= 10:
            recursos -= 10
            producao += 1
            window['_PRODUCAO_'].update(producao)
            window['_RECURSOS_'].update(recursos)

window.close()