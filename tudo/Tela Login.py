from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.title('Tela Login')
tela.geometry("460x340")


def recebe():
    entr = name_01.get()
    entr02 = senha_01.get()
    if entr == "admin" and entr02 == "1234":
        messagebox.showinfo(title="login Aprovado", message="Bem Vindo")
    else:
        messagebox.showerror(title="login errado", message="sem Autorizaçao")


name_01 = Label(tela, width=20, font="Arial 11", text="Name:")
name_01.place(x=40, y=60)

senha_01 = Label(tela, width=20, text="Senha:", font="Arial 11")
senha_01.place(x=40, y=120)

name_01 = Entry(tela, width=20)
name_01.place(x=160, y=60)

senha_01 = Entry(tela, width=20)
senha_01.place(x=160, y=120)

bot = Button(tela, width=20,relief=RAISED,overrelief=RIDGE, command=recebe, bg="lightgray", text="Confirmar", font="Arial 11")
bot.place(x=120, y=180)

receb01 = senha_01.get()
print(receb01)

tela.mainloop()
