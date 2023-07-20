import PySimpleGUI as sg

aqv = open('Numeros.txt', 'r')

opcao = [x for x in aqv.readlines()]

def app(arquivo):
    layout = [
        [sg.Text('Selecione seu Numero:')],
        [sg.Combo(arquivo, default_value='Escolha', key='-DROPDOWN-')],
        [sg.Button('Ok')]]

    janela = sg.Window('Seletor de Numero', layout)

    while True:
        evento, valores = janela.read()

        if evento == sg.WIN_CLOSED or evento == 'Ok':
            break

        opcao_selecionada = valores['-DROPDOWN-']
        sg.popup(f'Opção selecionada: {opcao_selecionada}')

    janela.close()

app(opcao)
aqv.close()
