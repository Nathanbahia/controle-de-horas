from tkinter import *
import sqlite3

m = [
    "Janeiro", "Fevereiro", "Marco",
    "Abril", "Maio","Junho",
    "Julho", "Agosto","Setembro",
    "Outubro", "Novembro","Dezembro" 
    ]

meses = [
    ["Janeiro", 31], ["Fevereiro",29], ["Marco",31],
    ["Abril",30], ["Maio",31], ["Junho",30],
    ["Julho",31], ["Agosto",31], ["Setembro",30],
    ["Outubro",31], ["Novembro",30], ["Dezembro",31], 
    ]

registros = ["Entrada", "Intervalo", "Retorno", "Saida"]

def insere_nome_no_banco_de_dados_principal(nome):
    conn_func = sqlite3.connect('geral.db')
    cursor_func = conn_func.cursor()

    cursor_func.execute(
            """
                CREATE TABLE IF NOT EXISTS funcionarios (
                    nome text
                )
            """)
    conn_func.commit()

    cursor_func.execute("INSERT INTO funcionarios (nome) VALUES ('{}')".format(nome))
    conn_func.commit()
    conn_func.close()

def conexao_banco_de_dados(banco):
    global conn
    global cursor    
    
    conn = sqlite3.connect( banco + '.db' )
    cursor = conn.cursor()

def start():

    a = cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")    
    if len(a.fetchall()) == 0:
        for i in meses:
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS {} (
                        dia integer,
                        Entrada text,
                        Intervalo text,
                        Retorno text,
                        Saida text
                    )
                """.format(i[0])
                )
     
        for i in range(len(meses)):
            for d in range(meses[i][1]):            
                    
                cursor.execute("INSERT INTO {} (dia, Entrada, Intervalo, Retorno, Saida) VALUES ({}, '{}', '{}', '{}', '{}')".format(meses[i][0], d+1, " ", " ", " ", " "))
        conn.commit()    

def bd_inclui_horas(mes, reg, hora, dia):
    cursor.execute("UPDATE {} SET '{}' = '{}' WHERE dia = {}".format(mes, reg, hora, dia))
    conn.commit()

def bd_exibe_hora(mes):
    dados = cursor.execute("SELECT * FROM {}".format(mes))
    return list(dados.fetchall())

def bd_func_cadastrados():
    conn_func = sqlite3.connect('geral.db')
    cursor_func = conn_func.cursor()
    nomes_funcionarios = []
    
    func = cursor_func.execute("SELECT * FROM funcionarios")
    for i in func.fetchall():
        nomes_funcionarios.append(i[0])
    return nomes_funcionarios

class Folha:
    def __init__(self, master = None):
        self.bg_padrao = "#aaff00"
        self.bg_horas = "#ffffff"
        self.fonte_horas = ("Arial", "18")


        # PLANO DE FUNDO PRINCIPAL
        self.frame_0 = Label(master, text = "", bg = self.bg_padrao)
        self.frame_0.place(x = 0, y = 0, width = 1366, height = 768)
        

        # PLANO DE FUNDO ONDE SÃO PLOTADOS OS WIDGETS DE CADASTRO DE FUNCIONARIO
        self.frame_1 = Label(self.frame_0, text = "", bg = self.bg_horas)
        self.frame_1.place(x = 0, y = 0, width = 1366, height = 500)


        # TELA DE ENTRADA COM ENTRY E OPTION MENU PARA SELECIONAR FUNCIONARIO
        self.boas_vindas = Label(self.frame_1, bg = self.bg_horas, text = "Supermercado Casa dos Cereais\nControle de Ponto Mensal", font = ("Arial", "36"))
        self.boas_vindas.place(x = 0, y = 50, width = 1366)
        
        self.func_label = Label(self.frame_1, text = "Cadastre um novo funcionário ou selecione um abaixo:", bg = self.bg_padrao, font = self.fonte_horas)
        self.func_label.place(x = 0, y = 250, width = 1366)

        self.func = Entry(self.frame_1, font = self.fonte_horas)
        self.func.place(x = 500, y = 300, width = 366, height = 30)

        self.cad = Button(self.frame_1, text = "Cadastrar", font = ("Arial", "12", "bold"), bg = self.bg_padrao)
        self.cad.bind("<Return>", self.cadastro_de_funcionario)
        self.cad.bind("<Button-1>", self.cadastro_de_funcionario)
        self.cad.place(x = 600, y = 350, width = 166, height = 30)       

        var3 = StringVar()
        self.func_options = OptionMenu(self.frame_1, var3, *bd_func_cadastrados(), command = self.seleciona_nome)
        self.func_options["bg"] = self.bg_padrao
        self.func_options["font"] = self.fonte_horas
        self.func_options.place(x = 500, y = 400, width = 366)  


        # AREA DO MENU PRINCIPAL

        ''' LABEL/ENTRY DIA '''
        self.label_dia = Label(master, text = "DIA: ", bg = self.bg_padrao, font = ("Arial", "14", "bold"), justify = "right")
        self.label_dia.place(x = 50, y = 520, width = 100, height = 30)        

        self.entry_dia = Entry(master, font = ("Arial", "14", "bold"), justify = "center")
        self.entry_dia.place(x = 200, y = 520, width = 200, height = 30)


        ''' LABEL/OPTIONMENU MÊS '''
        self.label_mes = Label(master, text = "MES: ", bg = self.bg_padrao, font = ("Arial", "14", "bold"), justify = "right")
        self.label_mes.place(x = 50, y = 570, width = 100, height = 30)                  

        var1 = StringVar()
        self.meses = OptionMenu(master, var1, *m, command = self.set_mes)
        self.meses["font"] = ("Arial", "14", "bold")
        self.meses.place(x = 200, y = 570 , width = 200, height = 30)
        self.select_mes = "Marco"


        ''' LABEL/ENTRY HORA '''
        self.label_hora = Label(master, text = "HORA: ", bg = self.bg_padrao, font = ("Arial", "14", "bold"), justify = "right")
        self.label_hora.place(x = 50, y = 620, width = 100, height = 30)

        self.entry_hora = Entry(master, font = ("Arial", "14", "bold"), justify = "center")
        self.entry_hora.place(x = 200, y = 620, width = 200, height = 30)


        ''' LABEL/OPTIONMENU REGISTRO '''
        self.label_registro = Label(master, text = "REGISTRO:", bg = self.bg_padrao, font = ("Arial", "14", "bold"), justify = "right")
        self.label_registro.place(x = 50, y = 670, width = 110, height = 30)        

        var2 = StringVar()
        self.reg = OptionMenu(master, var2, *registros, command = self.set_reg)
        self.reg["font"] = ("Arial", "14", "bold")
        self.reg.place(x = 200, y = 670, width = 200, height = 30)
        
        self.select_reg = None        


        ''' BOTÕES CONFIRMA E RETORNA '''
        self.btn_confirma = Button(master, text = "Confirma", font = ("Arial", "14", "bold"))
        self.btn_confirma.bind("<Return>", self.inclui_hora_banco_de_dados)
        self.btn_confirma.bind("<Button-1>", self.inclui_hora_banco_de_dados)
        self.btn_confirma.place(x = 450, y = 550, width = 200, height = 50)

        self.btn_voltar = Button(master, text = "Voltar", font = ("Arial", "14", "bold"))
        self.btn_voltar["command"] = self.voltar
        self.btn_voltar.place(x = 450, y = 650, width = 200, height = 50)

        
        ''' LABEL NOME DO FUNCIONARIO '''
        self.lbl_func = Label(master, text = "", font = self.fonte_horas, bg = self.bg_padrao)
        self.lbl_func.place(x = 700, y = 650, width = 580)

        

    def seleciona_nome(self, value):
        '''
            Função que seleciona o nome a partir do OptionMenu da tela inicial e o usa como parâmetro
            para se conectar ao banco de dados do funcionario selecionado.

        '''
        nome = value
        '''
            Altera o nome na tela de horários e troca a cor de fundo do label para branco.
        '''
        self.lbl_func["text"] = nome
        self.lbl_func["bg"] = "#ffffff"
        '''
            Realiza a concexão com o banco de dados, verifica se há a necessidade de contrução das tabelas,
            e em seguida atualiza a tela.
    
        '''        
        conexao_banco_de_dados(nome)
        start()
        self.atualizar_tela()

    def cadastro_de_funcionario(self, event):
        '''
            Função que captura o nome inserido no label na tela principal, verifica se ele é do tipo string,
            se seu tamanho é maior que zero, e se não é None.

            Altera o nome na tela de horários e a cor de fundo.

            Insere o funcionario no banco de dados geral, e em seguida cria um banco de dados para o funcionario a
            partir da função start.            

            Realiza a conexão com o banco de dados e atualiza a tela com os dados do funcionario recem cadastrado.
        '''
        nome = self.func.get()

        if isinstance(nome, str) and len(nome.strip()) > 0 and nome != None:
            self.func_options.destroy()

            self.lbl_func["text"] = nome
            self.lbl_func["bg"] = "#ffffff"

            insere_nome_no_banco_de_dados_principal(nome)
            
            conexao_banco_de_dados(nome)
            start()
            self.atualizar_tela()


    def set_mes(self, value):        
        self.select_mes = value
        self.atualizar_tela()



    def set_reg(self, value):        
        self.select_reg = value        



    def inclui_hora_banco_de_dados(self, event):        
        mes = self.select_mes
        reg = self.select_reg
        hora = self.entry_hora.get()
        dia = int(self.entry_dia.get())
        bd_inclui_horas(mes, reg, hora, dia)
        self.atualizar_tela()

        self.entry_hora.delete(0, END)
        self.entry_dia.delete(0, END)

    def atualizar_tela(self):
        self.destroy_frame()

        self.frame_1 = Label(self.frame_0, text = "", bg = self.bg_horas)
        self.frame_1.place(x = 0, y = 0, width = 1366, height = 500)
        
        mes = self.select_mes

        self.titulo_mes = Label(self.frame_1, text = mes, font = ("Arial", "24", "bold", "italic"), bg = self.bg_horas).place(x = 10, y = 10, width = 1366)

        pos_y = 120
        for i in range(0,10):
            for k in range(len(bd_exibe_hora(mes)[i]) - 1):
                d = bd_exibe_hora(mes)[i][0]
                e1 = bd_exibe_hora(mes)[i][1]
                s1 = bd_exibe_hora(mes)[i][2]
                e2 = bd_exibe_hora(mes)[i][3]
                s2 = bd_exibe_hora(mes)[i][4]
                    
            t = str(d) + " " + e1 + " " + s1 + " " + e2 + " " + s2
                
            l = Label(self.frame_1, text = t , bg = self.bg_horas, font = self.fonte_horas).place(x = 100, y = pos_y)
            pos_y += 30

        pos_y = 120
        t = ""
        for i in range(10, 20):
            for k in range(len(bd_exibe_hora(mes)[i]) - 1):
                d = bd_exibe_hora(mes)[i][0]
                e1 = bd_exibe_hora(mes)[i][1]
                s1 = bd_exibe_hora(mes)[i][2]
                e2 = bd_exibe_hora(mes)[i][3]
                s2 = bd_exibe_hora(mes)[i][4]
                    
            t = str(d) + " " + e1 + " " + s1 + " " + e2 + " " + s2
            
            l = Label(self.frame_1, text = t, bg = self.bg_horas, font = self.fonte_horas).place(x = 500, y = pos_y)
            pos_y += 30

        pos_y = 120 
        for i in range(20, len(bd_exibe_hora(mes))):
            for k in range(len(bd_exibe_hora(mes)[i]) - 1):
                d = bd_exibe_hora(mes)[i][0]
                e1 = bd_exibe_hora(mes)[i][1]
                s1 = bd_exibe_hora(mes)[i][2]
                e2 = bd_exibe_hora(mes)[i][3]
                s2 = bd_exibe_hora(mes)[i][4]
                    
            t = str(d) + " " + e1 + " " + s1 + " " + e2 + " " + s2
            
            l = Label(self.frame_1, text = t, bg = self.bg_horas, font = self.fonte_horas).place(x = 900, y = pos_y)
            pos_y += 30

    def destroy_frame(self):
        self.frame_1.destroy()    
        self.frame_1 = Label(self.frame_0, text = "", bg = self.bg_horas)
        self.frame_1.place(x = -5, y = 30, width = 600, height = 380)

    def voltar(self):
        self.lbl_func["text"] = ""
        self.lbl_func["bg"] = self.bg_padrao
        
        self.destroy_frame()
        
        self.frame_1 = Label(self.frame_0, text = "", bg = self.bg_horas)
        self.frame_1.place(x = 0, y = 0, width = 1366, height = 500)

        self.boas_vindas = Label(self.frame_1, bg = self.bg_horas, text = "Supermercado Casa dos Cereais\nControle de Ponto Mensal", font = ("Arial", "36"))
        self.boas_vindas.place(x = 0, y = 50, width = 1366)
        
        self.func_label = Label(self.frame_1, text = "Cadastre um novo funcionário ou selecione um abaixo:", bg = self.bg_padrao, font = self.fonte_horas)
        self.func_label.place(x = 0, y = 250, width = 1366)

        self.func = Entry(self.frame_1, font = self.fonte_horas)
        self.func.place(x = 500, y = 300, width = 366, height = 30)

        self.cad = Button(self.frame_1, text = "Cadastrar", font = ("Arial", "12", "bold"), bg = self.bg_padrao)
        self.cad.bind("<Return>", self.cadastro_de_funcionario)
        self.cad.bind("<Button-1>", self.cadastro_de_funcionario)
        self.cad.place(x = 600, y = 350, width = 166, height = 30)       

        var3 = StringVar()
        self.func_options = OptionMenu(self.frame_1, var3, *bd_func_cadastrados(), command = self.seleciona_nome)
        self.func_options["bg"] = self.bg_padrao
        self.func_options["font"] = self.fonte_horas
        self.func_options.place(x = 500, y = 400, width = 366)  

root = Tk()
root.title("Calculo de Horas")
root.geometry("{}x{}".format(1366, 768))
Folha(root)
root.mainloop()
