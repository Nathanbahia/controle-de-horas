from tkinter import *
import sqlite3

MESES = ["JANEIRO", "FEVEREIRO", "MARCO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO" ,"OUTUBRO", "NOVEMBRO", "DEZEMBRO"]

def checkValores(dia, mes, e1,s1,e2,s2):
    if 1 <= dia <= 31:
        if mes in MESES:
            if len(e1) == 5 and len(s1) == 5 and len(e2) == 5 and len(s2) == 5:
                print(True)

            else:
                print(False)
        else:
            print(False)
    

class App:
    def __init__(self, master):
        self.master = master

        self.sidebar = Frame(self.master)
        self.sidebar.configure(background="#484848")
        self.sidebar.place(x=0,y=0,w=150,h=680)

        self.titulo = Label(self.master, text="Casa dos Cereais Super Center").place(x=160)
        
        self.lblDia = Label(self.master, text="Dia: ").place(x=20,y=10,w=50,h=20)
        self.dia = Entry(self.master)
        self.dia.place(x=70,y=10,w=60,h=20)
        
        var = StringVar()
        self.selecionaMes = OptionMenu(self.master, var, *MESES, command = self.setMonth).place(x=20,y=50,h=20,w=110)
        self.mes = ""

        self.lblEntrada = Label(self.master, text="E1").place(x=20,y=100)
        self.entrada = Entry(self.master)
        self.entrada.place(x=70,y=100,w=60)

        self.lblIntervalo = Label(self.master, text="S1").place(x=20,y=140)
        self.intervalo = Entry(self.master)
        self.intervalo.place(x=70,y=140,w=60)
        
        self.lblRetorno = Label(self.master, text="E2").place(x=20,y=190)
        self.retorno = Entry(self.master)
        self.retorno.place(x=70,y=190,w=60)

        self.lblSaida = Label(self.master, text="S2").place(x=20,y=230)
        self.saida = Entry(self.master)
        self.saida.place(x=70,y=230,w=60)

        self.btnConfirma = Button(self.master, text="Confirmar")
        self.btnConfirma["command"] = self.capturaHoras
        self.btnConfirma.place(x=20, y=270,w=110)

        posx = 200
        posy = 30

        self.dias = {}
        for i in range(1, 32):
            self.dias["dia"] = Label(self.master, text = i).place(x=posx-30, y=posy, w=40, h=20)
            self.dias[str(i)+"-E1"] = Label(self.master, text = "--:--").place(x=posx, y=posy, w=40, h=20)
            self.dias[str(i)+"-S1"] = Label(self.master, text = "--:--").place(x=posx + 50, y=posy, w=40, h=20)
            self.dias[str(i)+"-E2"] = Label(self.master, text = "--:--").place(x=posx + 100, y=posy, w=40, h=20)
            self.dias[str(i)+"-S2"] = Label(self.master, text = "--:--").place(x=posx + 150, y=posy, w=40, h=20)

            posy += 20

    def setMonth(self, value):
        self.mes = value

    def capturaHoras(self):
        dia = self.dia.get()
        mes = self.mes
        e1 = self.entrada.get()
        s1 = self.intervalo.get()
        e2 = self.retorno.get()
        s2 = self.saida.get()

        checkValores(dia, mes, e1,s1,e2,s2)
 


root = Tk()
App(root)
root.title("Casa dos Cereais Super Center")
root.geometry("{}x{}+0+0".format(400, 660))
root.mainloop()
