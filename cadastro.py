import FreeSimpleGUI as sg

# Layout
sg.theme('SystemDefault')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],
    [sg.Button('Sair')]
   
]

# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'matheus' and valores['senha'] == '123456':
            print('Bem-vindo')
    if eventos == 'Sair':
        break
