from PyQt5 import uic,QtWidgets
import imagens

def login():
    login = Telalogin .lineEdit_usuario.text()
    senha = Telalogin .lineEdit_2_senha.text()

    if login == "edvan" and senha =="123456":
        Telalogin .label_aviso.setText("     Login feito com sucesso")
    else:
        Telalogin .label_aviso.setText("     Login ou senha incorretos ")
    # print(senha)
    # print(login)
    # Telalogin .label_aviso.setText("     Login ou senha incorretos ")

# janela de cadastro 
def cadastro():
    Telacadastro.show()

# cadastra um novo usuario
def Cadastrabanco():
    nome = Telacadastro.lineEdit.text()
    sobrenome = Telacadastro.lineEdit_2.text()
    email = Telacadastro.lineEdit_3.text()
    login = Telacadastro.lineEdit_4.text()
    senha = Telacadastro.lineEdit_5.text()
  
    print(nome)
    print(sobrenome)
    print(email )
    print(login)
    print(senha)

app= QtWidgets.QApplication([])

# *******************************chamada das telas********************************************************* 
Telalogin  =uic.loadUi("paginas/paginaLogin.ui")
Telacadastro =uic.loadUi("paginas/cadastro.ui")

# ********************************bottoes de click*********************************************************
Telalogin .botao1.clicked.connect(login)
Telalogin .pushButton_2.clicked.connect(cadastro)
# botao responsavel por cadastrar um novo usuario
Telacadastro.pushButton.clicked.connect(Cadastrabanco)




# *******************************mostra a tema e inicia o progama*****************************************
Telalogin .show()
app.exec()
# *******************************mostra a tema e inicia o progama*****************************************
