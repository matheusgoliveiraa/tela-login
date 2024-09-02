import tkinter as tk
from tkinter import messagebox

# Função para verificar login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == 'matheus' and senha == '123456':
        messagebox.showinfo("Login", "Seja bem-vindo!")
    else:
        messagebox.showerror("Login", "Usuário ou senha inválidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title('Tela de Login')

# Definição do layout
tk.Label(janela, text='Usuário').grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_usuario = tk.Entry(janela)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text='Senha').grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_senha = tk.Entry(janela, show='*')
entry_senha.grid(row=1, column=1, padx=10, pady=10)

var_salvar_login = tk.BooleanVar()
tk.Checkbutton(janela, text='Salvar o login?', variable=var_salvar_login).grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Button(janela, text='Entrar', command=verificar_login).grid(row=3, column=1, padx=10, pady=10, sticky='e')

# Inicia o loop da interface gráfica
janela.mainloop()
