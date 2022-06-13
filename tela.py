import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha  '), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')],
    [sg.Text('',key='mensagem')]
    ]
# Janela
window = sg.Window('Tela de Login',layout=layout)

# Ler os eventos
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:

        break
    
    elif event == 'Entrar':

        senha_correta = '1234'
        usuario_correto = 'Erik'
        usuario = values['usuario']
        senha = values['senha']

        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha ou usuário incorreto')


