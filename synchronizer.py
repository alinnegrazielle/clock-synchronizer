
'''
    Sicronizador de Clock - Algoritmo de Berkeley
    DUPLA: Alinne Farias e Vitoria Neris.
'''

from glob import glob
from tkinter import *
from tkinter import Tk, ttk
import time
import numpy as np


# cores -------------------------
c0 = "#f0f3f5"  # Preta 
c1 = "#feffff"  # branca 
c2 = "#3fb5a3"  # verde 
c3 = "#38576b"  # valor
c4 = "#403d3d"  # letra 

difC1 = list()


# criando janela de input's -------------------------
janela = Tk()
janela.title('Avaliação de SD')
janela.geometry('450x620')
janela.configure(background=c0)
janela.resizable(width=FALSE, height=FALSE)

# divisão de tela ----------------------------------------
frame_cima = Frame(janela, width=450, height=50, bg=c1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=450, height=600, bg=c1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame de cima ----------------------------------------
l_sinc = Label(frame_cima, text='Sincronizador de Clock', anchor=NE, font=('Ivy 20'), bg=c1, fg=c4)
l_sinc.place(x=50, y=10)

l_linha = Label(frame_cima, text='', width=300, anchor=NW, font=('Ivy 1'), bg=c2, fg=c4)
l_linha.place(x=50, y=45)

    
# Pegando horário local do servidor
def criar_serv():
      
    msg = 'Servidor criado!'
    text_rsp['text'] = msg


def cria_serv():
    global horaServer
    horaUTC = time.localtime()
    horaServer = [horaUTC[3], horaUTC[4]] 
    
    return str(horaServer[0])+':'+str(horaServer[1])
    

# Pegando horário (local e de envio) do cliente1
def criar_clientes():

    nova_janela()

def horaLocCliente1():
    global horaLocCli1
    hr_local_c1 = e1_local.get()
    hr_loc_1, min_loc_1 = [int(t) for t in hr_local_c1.split(":")] # definindo hora cliente 1
    horaLocCli1 = [hr_loc_1, min_loc_1]

    return str(horaLocCli1[0])+':'+str(horaLocCli1[1])

def horaEnvCliente1():
    global horaEnvCli1
    hr_env_c1 = e1_env.get()
    hr_env_1, min_env_1 = [int(t) for t in hr_env_c1.split(":")] # definindo hora cliente 1
    horaEnvCli1 = [hr_env_1, min_env_1]

    return str(horaEnvCli1[0])+':'+str(horaEnvCli1[1])

def horaLocCliente2():
    global horaLocCli2
    hr_local_c2 = e2_local.get()
    hr_loc_2, min_loc_2 = [int(t) for t in hr_local_c2.split(":")] # definindo hora cliente 1
    horaLocCli2 = [hr_loc_2, min_loc_2]

    return str(horaLocCli2[0])+':'+str(horaLocCli2[1])

def horaEnvCliente2():
    global horaEnvCli2
    hr_env_c2 = e2_env.get()
    hr_env_2, min_env_2 = [int(t) for t in hr_env_c2.split(":")] # definindo hora cliente 1
    horaEnvCli2 = [hr_env_2, min_env_2]

    return str(horaEnvCli2[0])+':'+str(horaEnvCli2[1])

def horaLocCliente3():
    global horaLocCli3
    hr_local_c3 = e3_local.get()
    hr_loc_3, min_loc_3 = [int(t) for t in hr_local_c3.split(":")] # definindo hora cliente 1
    horaLocCli3 = [hr_loc_3, min_loc_3]

    return str(horaLocCli3[0])+':'+str(horaLocCli3[1])
    
def horaEnvCliente3():
    global horaEnvCli3
    hr_env_c3 = e3_env.get()
    hr_env_3, min_env_3 = [int(t) for t in hr_env_c3.split(":")] # definindo hora cliente 1
    horaEnvCli3 = [hr_env_3, min_env_3]

    return str(horaEnvCli3[0])+':'+str(horaEnvCli3[1])

# diferença do hr envio de cada cliente pelo local
def difCli1():
    global difC1
    he1 = horaEnvCli1
    hr1 = horaLocCli1
    difC1 = [he1[0]-hr1[0],he1[1]-hr1[1]]

    return str(difC1[0])+':'+str(difC1[1])

def difCli2():
    global difC2
    he2 = horaEnvCli2
    hr2 = horaLocCli2
    difC2 = [he2[0]-hr2[0],he2[1]-hr2[1]]

    return str(difC2[0])+':'+str(difC2[1])

def difCli3():
    global difC3
    he3 = horaEnvCli3
    hr3 = horaLocCli3
    difC3 = [he3[0]-hr3[0],he3[1]-hr3[1]]

    return str(difC3[0])+':'+str(difC3[1])


# Definindo Clock Lógico
def clock_log():
    global hr, min
    hs = horaServer
    hl1 = horaLocCli1
    hl2 = horaLocCli2
    hl3 = horaLocCli3

    # cria a lista com todos os horários e seu tamanho
    newlist = (hs,hl1,hl2,hl3)
    cl = list(map(sum, zip(hs,hl1,hl2,hl3)))
    tam = len(newlist)
    
    # gera o clock não formatado
    myArray = np.array(cl)
    myInt = tam
    newArray = myArray/myInt
    #print(newArray)

    #clock formatado
    hr = int(newArray[0])
    min = int(newArray[1])

    return str(hr)+':'+str(min)

# somando a diferença de cada cliente com o clock
def envSinc1():
    global newhr1
    clochr = [hr, min]

    newhr1 = [difC1[0]+clochr[0],difC1[1]+clochr[1]]

    return str(newhr1[0])+':'+str(newhr1[1])

def envSinc2():
    global newhr2
    clochr = [hr, min]

    newhr2 = [difC2[0]+clochr[0],difC2[1]+clochr[1]]

    return str(newhr2[0])+':'+str(newhr2[1])

def envSinc3():
    global newhr3
    clochr = [hr, min]

    newhr3 = [difC3[0]+clochr[0],difC3[1]+clochr[1]]

    return str(newhr3[0])+':'+str(newhr3[1])

# Após coletar dados
def nova_janela():
    janela2 = Tk()
    janela2.title('Resultado')
    janela2.geometry('400x500')
    janela2.configure(background=c0)
    janela2.resizable(width=FALSE, height=FALSE)

    #---------------retornando o horário local do servidor-------------
    cria_serv()
    a = 'Hr Local do Servidor: '
    b = str(horaServer[0])+':'+str(horaServer[1])
    resultserv = f'{a}{b}'
    
    # ---------------retornando o horário local dos clientes------------
    horaLocCliente1()
    c = 'Hora Local Cliente 1: '
    d = str(horaLocCli1[0])+':'+str(horaLocCli1[1])
    result1 = f'{c}{d}'

    horaLocCliente2()
    e = 'Hora Local Cliente 2: '
    f = str(horaLocCli2[0])+':'+str(horaLocCli2[1])
    result2 = f'{e}{f}'

    horaLocCliente3()
    g = 'Hora Local Cliente 3: '
    h = str(horaLocCli3[0])+':'+str(horaLocCli3[1])
    result3 = f'{g}{h}'
    #-------------------------------------------------------------------

    clock_log()
    i = 'Clock Lógico: '
    j = str(hr)+':'+str(min)
    resultclock = f'{i}{j}'
    #-------------------------------------------------------------------

    horaEnvCliente1()
    difCli1()
    envSinc1()
    k = 'Hr/Envio Ajustado(C1): '
    l = str(newhr1[0])+':'+str(newhr1[1])
    envio1 = f'{k}{l}'

    horaEnvCliente2()
    difCli2()
    envSinc2()
    k = 'Hr/Envio Ajustado(C2): '
    l = str(newhr2[0])+':'+str(newhr2[1])
    envio2 = f'{k}{l}'

    horaEnvCliente3()
    difCli3()
    envSinc3()
    k = 'Hr/Envio Ajustado(C3): '
    l = str(newhr3[0])+':'+str(newhr3[1])
    envio3 = f'{k}{l}'
    #-------------------------------------------------------------------

    frame_cima = Frame(janela2, width=410, height=50, bg=c1, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo = Frame(janela2, width=410, height=600, bg=c1, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #################################### FRAME_CIMA ######################################
    l_sinc = Label(frame_cima, text='Sincronizando...', anchor=NE, font=('Ivy 18'), bg=c1, fg=c4)
    l_sinc.place(x=40, y=12)

    l_linha = Label(frame_cima, text='', width=300, anchor=NW, font=('Ivy 1'), bg=c2, fg=c4)
    l_linha.place(x=40, y=45)

    ################################### FRAME_BAIXO ######################################
    # Horário Local ----------------------------------------------------------------------------------
    hl = Label(frame_baixo, text=resultserv, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hl.place(x=40, y=25)

    # Horário Local Clientes -------------------------------------------------------------------------
    hlc1 = Label(frame_baixo, text=result1, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc1.place(x=40, y=60)
    hlc2 = Label(frame_baixo, text=result2, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc2.place(x=40, y=85)
    hlc3 = Label(frame_baixo, text=result3, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc3.place(x=40, y=110)

    # Clock Lógico ----------------------------------------------------------------------------------
    clock = Label(frame_baixo, text=resultclock, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    clock.place(x=40, y=145)

    # Ajuste do Clock ----------------------------------------------------------------------------------
    ajuste1 = Label(frame_baixo, text=envio1, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste1.place(x=40, y=180)
    ajuste2 = Label(frame_baixo, text=envio2, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste2.place(x=40, y=205)
    ajuste3 = Label(frame_baixo, text=envio3, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste3.place(x=40, y=230)

    # Ordem de Envio ----------------------------------------------------------------------------------
    ode = Label(frame_baixo, text='Ordem de Envio', anchor=NW, font=('Ivy 18 bold'), bg=c1, fg=c4)
    ode.place(x=40, y=275)
    ode1 = Label(frame_baixo, text='1º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode1.place(x=40, y=310)
    ode2 = Label(frame_baixo, text='2º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode2.place(x=40, y=335)
    ode3 = Label(frame_baixo, text='3º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode3.place(x=40, y=360)

###################################### SERVIDOR ###############################################
# Criando Servidor
c_serv = Button(frame_baixo, command=criar_serv, text='Criar Servidor', width=12, height=1, anchor=NW, font=('Ivy 15 bold'), bg=c2, fg=c1, relief=RAISED)
c_serv.place(x=110, y=25)

text_rsp = Label(frame_baixo, text='')
text_rsp.place(x=150, y=65)

###################################### CLIENTE 1 ###############################################
# Input's Cliente 1 ----------------------------------------
c1_nome = Label(frame_baixo, text='Cliente 1', anchor=NW, font=('Ivy 15 bold'), bg=c1, fg=c4)
c1_nome.place(x=50, y=90)

# Horário Local ----------------------------------------------------------------------------------------
h_local = Label(frame_baixo, text='Hr Local', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h_local.place(x=50, y=115)
e1_local = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e1_local.place(x=50, y=135)

# Horário de Envio --------------------------------------------------------------------------------------
h_env = Label(frame_baixo, text='Hr de Envio', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h_env.place(x=50, y=160)
e1_env = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e1_env.place(x=50, y=180)

###################################### CLIENTE 2 ###############################################
# Input's Cliente 2 ----------------------------------------
c2_nome = Label(frame_baixo, text='Cliente 2', anchor=NW, font=('Ivy 15 bold'), bg=c1, fg=c4)
c2_nome.place(x=50, y=210)

# Horário Local ----------------------------------------------------------------------------------------
h2_local = Label(frame_baixo, text='Hr Local', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h2_local.place(x=50, y=235)
e2_local = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e2_local.place(x=50, y=255)

# Horário de Envio --------------------------------------------------------------------------------------
h2_env = Label(frame_baixo, text='Hr de Envio', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h2_env.place(x=50, y=280)
e2_env = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e2_env.place(x=50, y=300)

###################################### CLIENTE 3 ###############################################
# Input's Cliente 3 ----------------------------------------
c3_nome = Label(frame_baixo, text='Cliente 3', anchor=NW, font=('Ivy 15 bold'), bg=c1, fg=c4)
c3_nome.place(x=50, y=330)

# Horário Local ----------------------------------------------------------------------------------------
h3_local = Label(frame_baixo, text='Hr Local', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h3_local.place(x=50, y=355)
e3_local = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e3_local.place(x=50, y=375)

# Horário de Envio --------------------------------------------------------------------------------------
h3_env = Label(frame_baixo, text='Hr de Envio', anchor=NW, font=('Ivy 12'), bg=c1, fg=c4)
h3_env.place(x=50, y=400)
e3_env = Entry(frame_baixo, width=8, justify='left', font=("", 12), highlightthickness=1, relief='solid')
e3_env.place(x=50, y=420)

# Submeter infos Cliente 1
subm_cli1 = Button(frame_baixo, command=criar_clientes, text='Enviar', width=5, height=1, anchor=NW, font=('Ivy 15 bold'), bg=c2, fg=c1, relief=RAISED, overrelief=RIDGE)
subm_cli1.place(x=50, y=470)

janela.mainloop()
