from tkinter import *
import sqlite3

MESES = ["JANEIRO", "FEVEREIRO", "MARCO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO" ,"OUTUBRO", "NOVEMBRO", "DEZEMBRO"]

def checkValores(dia, mes, e1,s1,e2,s2):
    valores = [e1, s1, e2, s2]
    if 1 <= int(dia) <= 31:
        if mes in MESES:
            for i in valores:
                if ":" in i:
                    if 7 < int(i[:2]) < 23:
                        if 0 <= int(i[:2]) <= 59:
                            if len(i) == 5:
                                print("Valores aceitos")
                                
         
    

class App:
    def __init__(self, master):
        self.master = master

        self.sidebar = Frame(self.master)
        self.sidebar.configure(background="#484848")
        self.sidebar.place(x=0,y=0,w=150,h=680)

        self.titulo = Label(self.master, text="Victor Gabriel dos S. Nunes", font="Courier 10 bold", fg="#d91214").place(x=160)
        
        self.lblDia = Label(self.master, text="Dia: ", font="Courier 10 bold", bg="#484848", fg="#ffffff").place(x=20,y=10,w=50,h=20)
        self.dia = Entry(self.master, font="Courier 10")
        self.dia.place(x=70,y=10,w=60,h=20)
        
        var = StringVar()
        self.selecionaMes = OptionMenu(self.master, var, *MESES, command = self.setMonth)
        self.selecionaMes["font"] = "Courier 10"
        self.selecionaMes.place(x=20,y=50,h=20,w=110)
        self.mes = ""

        self.lblEntrada = Label(self.master, text="E1", font="Courier 10 bold", bg="#484848", fg="#ffffff").place(x=30,y=100)
        self.entrada = Entry(self.master, font="Courier 10")
        self.entrada.place(x=70,y=100,w=60)

        self.lblIntervalo = Label(self.master, text="S1", font="Courier 10 bold", bg="#484848", fg="#ffffff").place(x=30,y=140)
        self.intervalo = Entry(self.master, font="Courier 10")
        self.intervalo.place(x=70,y=140,w=60)
        
        self.lblRetorno = Label(self.master, text="E2", font="Courier 10 bold", bg="#484848", fg="#ffffff").place(x=30,y=180)
        self.retorno = Entry(self.master, font="Courier 10")
        self.retorno.place(x=70,y=180,w=60)

        self.lblSaida = Label(self.master, text="S2", font="Courier 10 bold", bg="#484848", fg="#ffffff").place(x=30,y=220)
        self.saida = Entry(self.master, font="Courier 10")
        self.saida.place(x=70,y=220,w=60)

        self.btnConfirma = Button(self.master, text="Confirmar", font="Courier 10 bold")
        self.btnConfirma["command"] = self.capturaHoras
        self.btnConfirma.place(x=20, y=270,w=110)
        
        posx = 200
        posy = 30

        self.dias = {}
        for i in range(1, 32):
            self.dias["dia"] = Label(self.master, text = i, font="Courier 10 bold", bg="#d91214", fg="#ffffff").place(x=posx-30, y=posy, w=40, h=20)
            self.dias[str(i)+"-E1"] = Label(self.master, text = "--:--").place(x=posx, y=posy, w=40, h=20)
            self.dias[str(i)+"-S1"] = Label(self.master, text = "--:--").place(x=posx + 50, y=posy, w=40, h=20)
            self.dias[str(i)+"-E2"] = Label(self.master, text = "--:--").place(x=posx + 100, y=posy, w=40, h=20)
            self.dias[str(i)+"-S2"] = Label(self.master, text = "--:--").place(x=posx + 150, y=posy, w=40, h=20)
            posy += 20

        '''
        Esse trecho de código será removido pelos dados que virão do banco de dados
        '''

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
