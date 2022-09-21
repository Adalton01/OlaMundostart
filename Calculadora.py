from tkinter import*
from tkinter import ttk

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x264')
janela['bg'] = 'black'
#poderia usar tbm o janela.config(bg='gray')

frame_tela = Frame(janela, width=235,height=50,bg= 'gray')
frame_tela.grid(row=0, column=0 )

frame_corpo = Frame(janela, width=235,height=268,bg='light gray')
frame_corpo.grid(row=1,column=0)

todos_valores = ''

def entrar_valores (event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)

def calcular ():
    global todos_valores
    resultado =eval(todos_valores)

    valor_texto.set(resultado)

def limpa_tela () :
    global todos_valores
    todos_valores = ('')
    valor_texto.set('')
  




valor_texto = StringVar()

app_label = Label(frame_tela,textvariable=valor_texto,text='123456789 ',width=29,height=3,padx=-4,pady=2,relief=FLAT,anchor='e',justify=RIGHT,font='arial 10  bold',bg='light blue')
app_label.place(x=0,y=-1)



b_1=Button(frame_corpo,command=limpa_tela,text='C',width=11,height=2,bg='red',font='ivy 10  ',relief=RAISED,overrelief=RIDGE,fg='white')
b_1.place(x=-1,y=1)

b_2=Button(frame_corpo,command=lambda: entrar_valores('%'),text='%',width=12,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_2.place(x=99,y=3)

b_3=Button(frame_corpo,command=lambda: entrar_valores('/') ,text='/',width=8,height=2,bg='orange',relief=RAISED,overrelief=RIDGE)
b_3.place(x=171,y=3)

b_7=Button(frame_corpo,command=lambda: entrar_valores('7') ,text='7',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_7.place(x=0,y=44)
b_8=Button(frame_corpo,command=lambda: entrar_valores('8') ,text='8',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_8.place(x=59,y=44)
b_9=Button(frame_corpo,command=lambda: entrar_valores('9') ,text='9',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_9.place(x=118,y=44)
b_a=Button(frame_corpo,command=lambda: entrar_valores('*') ,text='*',width=8,height=2,bg='orange',relief=RAISED,overrelief=RIDGE)
b_a.place(x=170,y=44)

b_4=Button(frame_corpo,command=lambda: entrar_valores('4') ,text='4',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=85)
b_5=Button(frame_corpo,command=lambda: entrar_valores('5') ,text='5',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_5.place(x=59,y=85)
b_6=Button(frame_corpo,command=lambda: entrar_valores('6') ,text='6',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_6.place(x=118,y=85)

b_b=Button(frame_corpo,command=lambda: entrar_valores('-') ,text='-',width=8,height=2,bg='orange',relief=RAISED,overrelief=RIDGE)
b_b.place(x=170,y=85)

b_1=Button(frame_corpo,command=lambda: entrar_valores('1') ,text='1',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=126)
b_2=Button(frame_corpo,command=lambda: entrar_valores('2') ,text='2',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_2.place(x=59,y=126)
b_3=Button(frame_corpo,command=lambda: entrar_valores('3') ,text='3',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE)
b_3.place(x=118,y=126)
b_c=Button(frame_corpo,command=lambda: entrar_valores('+') ,text='+',width=8,height=2,bg='orange',relief=RAISED,overrelief=RIDGE)
b_c.place(x=170,y=126)

b_0=Button(frame_corpo,command=lambda: entrar_valores('0') ,text='0',width=11,height=2,bg='light gray',font='ivy 10   ',relief=RAISED,overrelief=RIDGE)
b_0.place(x=-1,y=169)
b_s=Button(frame_corpo,command=lambda: entrar_valores('.') ,text='.',width=8,height=2,bg='light gray',relief=RAISED,overrelief=RIDGE,)
b_s.place(x=107,y=172)
b_r=Button(frame_corpo,command = calcular,text='=',width=8,height=2,bg='orange',relief=RAISED,overrelief=RIDGE,)
b_r.place(x=171,y=172)




janela.mainloop()
