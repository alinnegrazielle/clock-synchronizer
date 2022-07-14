
'''
    Sicronizador de Clock - Algoritmo de Berkeley
    DUPLA: Alinne Farias e Vitoria Neris.


# Layout
sg.theme('Reddit')
layout = [
    [sg.Button('Criar Servidor')],
    [sg.Button('Criar Cliente')],
    [sg.Text('Hora Local'),sg.Input(key='hr_local')],
    [sg.Text('Hora de Envio'),sg.Input(key='hr_envio')],
    [sg.Button('Enviar')]
]
'''

from tkinter import *
from tkinter import Tk, ttk
import time


# cores -------------------------
c0 = "#f0f3f5"  # Preta 
c1 = "#feffff"  # branca 
c2 = "#3fb5a3"  # verde 
c3 = "#38576b"  # valor
c4 = "#403d3d"  # letra 


# criando janela de input's -------------------------
janela = Tk()
janela.title('')
janela.geometry('280x300')
janela.configure(background=c1)
janela.resizable(width=FALSE, height=FALSE)

# divisão de tela ----------------------------------------
frame_cima = Frame(janela, width=410, height=50, bg=c1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=410, height=250, bg=c1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame de cima ----------------------------------------
l_sinc = Label(frame_cima, text='Sincronizador', anchor=NE, font=('Ivy 25'), bg=c1, fg=c4)
l_sinc.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=230, anchor=NW, font=('Ivy 1'), bg=c2, fg=c4)
l_linha.place(x=10, y=45)

# Pegando horário local do servidor
def criar_serv():
    horaUTC = time.localtime()
    horaServer = [horaUTC[3], horaUTC[4]] 

    print(horaServer) 


# Criando Servidor
c_serv = Button(frame_baixo, command=criar_serv, text='Criar Servidor', width=12, height=1, anchor=NW, font=('Ivy 10 bold'), bg=c2, fg=c1, relief=RAISED)
c_serv.place(x=15, y=10)

# Criando Cliente
c_cli = Button(frame_baixo, text='Criar Cliente', width=12, height=1, anchor=NW, font=('Ivy 10 bold'), bg=c2, fg=c1, relief=RAISED)
c_cli.place(x=14, y=50)

def criar_cli1():
    hr_local_c1 = e_local.get()
    hr_env_c1 = e_env.get()

    hr_loc_1, min_loc_1 = [int(t) for t in hr_local_c1.split(":")] # definindo hora cliente 1
    horaLocCli1 = [hr_loc_1, min_loc_1]

    hr_env_1, min_env_1 = [int(t) for t in hr_env_c1.split(":")] # definindo hora cliente 1
    horaEnvCli1 = [hr_env_1, min_env_1]

    print(horaLocCli1)
    print(horaEnvCli1)

# Input's Cliente 1 ----------------------------------------
c1_nome = Label(frame_baixo, text='Cliente 1', anchor=NW, font=('Ivy 10'), bg=c1, fg=c4)
c1_nome.place(x=10, y=90)

# Horário Local ----------------------------------------------------------------------------------------
h_local = Label(frame_baixo, text='Hr Local', anchor=NW, font=('Ivy 10'), bg=c1, fg=c4)
h_local.place(x=14, y=110)
e_local = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e_local.place(x=20, y=130)

# Horário de Envio --------------------------------------------------------------------------------------
h_env = Label(frame_baixo, text='Hr de Envio', anchor=NW, font=('Ivy 10'), bg=c1, fg=c4)
h_env.place(x=14, y=155)
e_env = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e_env.place(x=20, y=175)

# Submeter infos Cliente 1
subm_cli1 = Button(frame_baixo, command=criar_cli1, text='Enviar', width=5, height=1, anchor=NW, font=('Ivy 10 bold'), bg=c2, fg=c1, relief=RAISED)
subm_cli1.place(x=14, y=205)

janela.mainloop()
