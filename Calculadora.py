from tkinter import *
from tkinter import ttk

# Janela principal
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x264')
janela.config(bg='black')  # Outra forma: janela['bg'] = 'black'

# ---------------------- FRAMES ----------------------
# Frame superior onde fica o display
frame_tela = Frame(janela, width=235, height=50, bg='gray')
frame_tela.grid(row=0, column=0)

# Frame inferior onde ficam os botões
frame_corpo = Frame(janela, width=235, height=268, bg='light gray')
frame_corpo.grid(row=1, column=0)

# ---------------------- VARIÁVEIS ----------------------
todos_valores = ''
valor_texto = StringVar()

# ---------------------- FUNÇÕES ----------------------

# Adiciona valores ao display
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# Avalia a expressão do display
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except:
        valor_texto.set('Erro')
    todos_valores = ''

# Limpa o display
def limpa_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# ---------------------- DISPLAY ----------------------
# Label onde os números e resultados são mostrados
app_label = Label(
    frame_tela,
    textvariable=valor_texto,
    width=29,
    height=3,
    padx=-4,
    pady=2,
    relief=FLAT,
    anchor='e',
    justify=RIGHT,
    font='arial 10 bold',
    bg='light blue'
)
app_label.place(x=0, y=-1)

# ---------------------- BOTÕES ----------------------

# Linha 1
Button(frame_corpo, command=limpa_tela, text='C', width=11, height=2, bg='red', font='ivy 10', relief=RAISED, overrelief=RIDGE, fg='white').place(x=-1, y=1)
Button(frame_corpo, command=lambda: entrar_valores('%'), text='%', width=12, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=99, y=3)
Button(frame_corpo, command=lambda: entrar_valores('/'), text='/', width=8, height=2, bg='orange', relief=RAISED, overrelief=RIDGE).place(x=171, y=3)

# Linha 2
Button(frame_corpo, command=lambda: entrar_valores('7'), text='7', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=0, y=44)
Button(frame_corpo, command=lambda: entrar_valores('8'), text='8', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=59, y=44)
Button(frame_corpo, command=lambda: entrar_valores('9'), text='9', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=118, y=44)
Button(frame_corpo, command=lambda: entrar_valores('*'), text='*', width=8, height=2, bg='orange', relief=RAISED, overrelief=RIDGE).place(x=170, y=44)

# Linha 3
Button(frame_corpo, command=lambda: entrar_valores('4'), text='4', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=0, y=85)
Button(frame_corpo, command=lambda: entrar_valores('5'), text='5', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=59, y=85)
Button(frame_corpo, command=lambda: entrar_valores('6'), text='6', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=118, y=85)
Button(frame_corpo, command=lambda: entrar_valores('-'), text='-', width=8, height=2, bg='orange', relief=RAISED, overrelief=RIDGE).place(x=170, y=85)

# Linha 4
Button(frame_corpo, command=lambda: entrar_valores('1'), text='1', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=0, y=126)
Button(frame_corpo, command=lambda: entrar_valores('2'), text='2', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=59, y=126)
Button(frame_corpo, command=lambda: entrar_valores('3'), text='3', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=118, y=126)
Button(frame_corpo, command=lambda: entrar_valores('+'), text='+', width=8, height=2, bg='orange', relief=RAISED, overrelief=RIDGE).place(x=170, y=126)

# Linha 5
Button(frame_corpo, command=lambda: entrar_valores('0'), text='0', width=11, height=2, bg='light gray', font='ivy 10', relief=RAISED, overrelief=RIDGE).place(x=-1, y=169)
Button(frame_corpo, command=lambda: entrar_valores('.'), text='.', width=8, height=2, bg='light gray', relief=RAISED, overrelief=RIDGE).place(x=107, y=172)
Button(frame_corpo, command=calcular, text='=', width=8, height=2, bg='orange', relief=RAISED, overrelief=RIDGE).place(x=171, y=172)

# Loop da janela
janela.mainloop()
