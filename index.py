from PyQt5 import uic,QtWidgets
# aqui eu importei a imagem da tela de login
import imagens
# importado a biblioteca responsavel pelo banco de dados
import pymysql

import time



# conexao com o banco de dados 
conexao= pymysql.connect(
    host="localhost",user="root",passwd="",database="introduçaoaprogamaçao"
)

# inicia a conecçao com o banco de dados 
cursor = conexao.cursor()

# pagina de login acionada por um Telalogin  =uic.loadUi("paginas/paginaLogin.ui")
def login():
    count = 0
    # captura oque foi escrito na pag inicial
    login1 = Telalogin .lineEdit_usuario.text()
    senha = Telalogin .lineEdit_2_senha.text()
    try:
        cursor.execute("SELECT senha FROM usuarios  WHERE logim =  '"+login1+"' ")
        # verificaçao de login 
        verifica = cursor.fetchall()
        if senha == verifica[0][0]:
            Telalogin .label_aviso.setText("     Login feito com sucesso")
            painel_usuario.show()
            Telalogin.close()
            cursor.execute("SELECT * FROM usuarios")
            dados = cursor.fetchall()

            # impressao dos usuarios na tela
            painel_usuario.tableWidget.setRowCount(len(dados))
            painel_usuario.tableWidget.setColumnCount(6)

            # Adicionando dados para a visualizaçao
            for c in range(0,len(dados)):
                for b in range(0,6):
                    # adiciona os valores na tabela
                    painel_usuario.tableWidget.setItem(c,b,QtWidgets.QTableWidgetItem(str(dados[c][b])))
                
                
           
        else:
            Telalogin .label_aviso.setText("     Login ou senha incorretos ")
    except:
        Telalogin .label_aviso.setText("     Voce nao possui Cadastro  ")
        
# janela de cadastro 
def cadastro():
    Telacadastro.show()

# cadastra um novo usuario
def Cadastrabanco():
    nome = Telacadastro.lineEdit.text()
    sobrenome = Telacadastro.lineEdit_2.text()
    email = Telacadastro.lineEdit_3.text()
    login1 = Telacadastro.lineEdit_4.text()
    senha = Telacadastro.lineEdit_5.text()



    try:
        cursor.execute("INSERT INTO usuarios(nome,sobrenome,email,logim,senha) VALUES('"+nome+"','"+sobrenome+"','"+email+"','"+login1+"','"+senha+"')")
        conexao.commit()
    except:
        print("erro ao adicionar usuario ")
    else:
        Telacadastro.label_7.setText("Sucesso ao cadastrar um novo usuario ")

    # time.sleep(3)
    # Telacadastro.close()
        

app= QtWidgets.QApplication([])

# *******************************chamada das telas********************************************************* 
Telalogin  =uic.loadUi("paginas/paginaLogin.ui")
Telacadastro =uic.loadUi("paginas/cadastro.ui")
painel_usuario = uic.loadUi("paginas/cpanel.ui")

# ********************************bottoes de click*********************************************************
Telalogin .botao1.clicked.connect(login)
Telalogin .pushButton_2.clicked.connect(cadastro)
# botao responsavel por cadastrar um novo usuario
Telacadastro.pushButton.clicked.connect(Cadastrabanco)


# *******************************mostra a tema e inicia o progama*****************************************
Telalogin .show()
app.exec()
# *******************************mostra a tema e inicia o progama*****************************************
