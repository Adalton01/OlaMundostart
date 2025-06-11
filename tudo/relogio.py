import datetime
from tkinter import *
from tkinter import ttk
from datetime import *
import pyglet

pyglet.font.add_file('Technology.ttf')




janela = Tk()
janela.geometry('340x180')
janela.title('Relogio')
janela.configure(bg='black')
janela.resizable(width=False,height=False)

def relogio ():

    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%B')
    ano = tempo.strftime('%Y')
    l1.config(text=hora)
    l1.after(200,relogio)
    l2.config(text=dia_semana +'  ' + str (dia) + ' ' + str (mes) +'  ' + str (ano) )


l1 = Label(janela,font='Technology 80',bg='black',fg='red')
l1.grid(row=1,column=0,sticky =W , padx=5)

l2 = Label(janela,font='Technology 20',bg='black',fg='white')
l2.grid(row=2,column=0,sticky =SW, padx=5)

relogio()
janela.mainloop()
