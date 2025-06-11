from tkinter import *
from tkinter import messagebox

# Criação da janela principal
tela = Tk()
tela.title('Tela Login')
tela.geometry("460x340")

# Função para validar o login
def recebe():
    # Obtém o texto digitado nos campos de entrada
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Verifica se o usuário e senha estão corretos
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo(title="Login Aprovado", message="Bem Vindo")
    else:
        messagebox.showerror(title="Login Errado", message="Sem autorização")

# Label para o campo usuário
label_usuario = Label(tela, width=20, font="Arial 11", text="Usuário:")
label_usuario.place(x=40, y=60)

# Label para o campo senha
label_senha = Label(tela, width=20, text="Senha:", font="Arial 11")
label_senha.place(x=40, y=120)

# Entrada de texto para o usuário
entry_usuario = Entry(tela, width=20)
entry_usuario.place(x=160, y=60)

# Entrada de texto para a senha (com caractere oculto)
entry_senha = Entry(tela, width=20, show="*")
entry_senha.place(x=160, y=120)

# Botão para confirmar login, que chama a função recebe()
botao_confirmar = Button(tela, width=20, relief=RAISED, overrelief=RIDGE,
                        command=recebe, bg="lightgray", text="Confirmar", font="Arial 11")
botao_confirmar.place(x=120, y=180)

# Inicia o loop da interface gráfica
tela.mainloop()
