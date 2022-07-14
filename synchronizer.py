
'''
    Sicronizador de Clock - Algoritmo de Berkeley
    DUPLA: Alinne Farias e Vitoria Neris.
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



# Definindo Clock Lógico
def clock_log():
    # hs = horaServer.get()
    hl1 = e1_local.get()
    hl2 = e2_local.get()
    hl3 = e3_local.get()

    # cl = hl1+hl2+hl3/4
    print(hl1)
    print(hl2)
    print(hl3)

    
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
    hr_env_c1 = e1_env.get()

    hr_loc_1, min_loc_1 = [int(t) for t in hr_local_c1.split(":")] # definindo hora cliente 1
    horaLocCli1 = [hr_loc_1, min_loc_1]

    hr_env_1, min_env_1 = [int(t) for t in hr_env_c1.split(":")] # definindo hora cliente 1
    horaEnvCli1 = [hr_env_1, min_env_1]

    print(horaLocCli1)
    print(horaEnvCli1)

    hr_local_c2 = e2_local.get()
    hr_env_c2 = e2_env.get()

    hr_loc_2, min_loc_2 = [int(t) for t in hr_local_c2.split(":")] # definindo hora cliente 1
    horaLocCli2 = [hr_loc_2, min_loc_2]

    hr_env_2, min_env_2 = [int(t) for t in hr_env_c2.split(":")] # definindo hora cliente 1
    horaEnvCli2 = [hr_env_2, min_env_2]

    print(horaLocCli2)
    print(horaEnvCli2)

    hr_local_c3 = e3_local.get()
    hr_env_c3 = e3_env.get()

    hr_loc_3, min_loc_3 = [int(t) for t in hr_local_c3.split(":")] # definindo hora cliente 1
    horaLocCli3 = [hr_loc_3, min_loc_3]

    hr_env_3, min_env_3 = [int(t) for t in hr_env_c3.split(":")] # definindo hora cliente 1
    horaEnvCli3 = [hr_env_3, min_env_3]

    print(horaLocCli3)
    print(horaEnvCli3)

# Após coletar dados
def nova_janela():
    janela2 = Tk()
    janela2.title('Resultado')
    janela2.geometry('400x500')
    janela2.configure(background=c0)
    janela2.resizable(width=FALSE, height=FALSE)

    x = cria_serv()
    #hr1, min1 = [int(t) for t in horaServer.split(":")]
    #s = 'Hora Local do Servidor: '
    #h = horaServer
    #h = str(':'.split(horaServer))
    #result = f'{s}{h}'
    #print(result)


    xx = horaLocCliente1()
    #hr1, min1 = [int(t) for t in horaServer.split(":")]
    ss = 'Hora Local Cliente 1: '
    hh = horaLocCli1
    #h = str(':'.split(horaServer))
    result2 = f'{ss}{hh}'
    #print(result)

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
    hl = Label(frame_baixo, text=x, anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hl.place(x=40, y=25)

    # Horário Local Clientes -------------------------------------------------------------------------
    hlc1 = Label(frame_baixo, text=str(result2), anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc1.place(x=40, y=60)
    hlc2 = Label(frame_baixo, text='Hora Local Cliente 2: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc2.place(x=40, y=85)
    hlc3 = Label(frame_baixo, text='Hora Local Cliente 3: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    hlc3.place(x=40, y=110)

    # Clock Lógico ----------------------------------------------------------------------------------
    clock = Label(frame_baixo, text='Clock Lógico: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    clock.place(x=40, y=145)

    # Ajuste do Clock ----------------------------------------------------------------------------------
    ajuste1 = Label(frame_baixo, text='Hr/Envio Ajustado(C1): ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste1.place(x=40, y=180)
    ajuste2 = Label(frame_baixo, text='Hr/Envio Ajustado(C2): ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste2.place(x=40, y=205)
    ajuste3 = Label(frame_baixo, text='Hr/Envio Ajustado(C3): ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ajuste3.place(x=40, y=230)

    # Ordem de Envio ----------------------------------------------------------------------------------
    ode = Label(frame_baixo, text='Ordem de Envio', anchor=NW, font=('Ivy 18 bold'), bg=c1, fg=c4)
    ode.place(x=40, y=265)
    ode1 = Label(frame_baixo, text='1º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode1.place(x=40, y=295)
    ode2 = Label(frame_baixo, text='2º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode2.place(x=40, y=320)
    ode3 = Label(frame_baixo, text='3º Cliente: ', anchor=NE, font=('Ivy 16'), bg=c1, fg=c4)
    ode3.place(x=40, y=345)

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
