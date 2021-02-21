import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QPushButton,QToolTip,QLabel,QLineEdit
# from pyQt5 import QtGui

# classe recebendo o qmainwindow
class janela(QMainWindow):
    def __init__(self):
        super().__init__()
        # variavei para criaçao da janela
        self.topo = 100
        self.lado = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Max Eletronica"
        
        self.caixatext = QLineEdit(self)
        self.caixatext.move(250,50)
        self.caixatext.resize(200,50)



        label1 = QLabel(self)
        label1.setText('ola mundo')
        label1.move(280,200)
        label1.setStyleSheet("Qlabel {font-size:90px;color:'blue'}")
        label1.resize(200,25)

        self.label2 = QLabel(self)
        self.label2.setText('Digitou: ')
        self.label2.move(400,200)
        self.label2.setStyleSheet("Qlabel {font-size:90px;color:'blue'}")
        self.label2.resize(200,25)

        # imagem no pyton
        # self.carro = QLabel(self)
        # self.carro.move(50,400)
        # self.carro.setPixmap(QtGui.QPixmap('goku.png'))

        # chamando um bottao 
        bottao1 = QPushButton('Botao1',self)
        
        
        # define a posiçao do botao na janela
        
        # tamanho do botao
        bottao1.resize(80,50)
        # dx o bottao bonitinho hehee
        bottao1.setStyleSheet('QPushButton {background-color:#9AFF84}')
        # move o botao pela janela
        bottao1.move(250,250)

        # da uma funçao ao bottao 
        bottao1.clicked.connect(self.botao)

        
        # boatao 22222222 
        bottao2 = QPushButton('Botao2',self)
        bottao2.resize(80,50)
        bottao2.setStyleSheet('QPushButton {background-color:#9AFF84}')
        bottao2.move(400,250)
        bottao2.clicked.connect(self.botao2)

        # boatao 22222222 
        bottao3 = QPushButton('Enviar textp',self)
        bottao3.resize(80,50)
        bottao3.setStyleSheet('QPushButton {background-color:#9AFF84}')
        bottao3.move(550,250)
        bottao3.clicked.connect(self.botao3)


        # faz o carregamento da janela
        self.carregarjanela()
        # funçao fara o carregamento da janela
        
        
    def carregarjanela(self):
        # aqui serao repassados os valores das variaveis criadas anteriormente
        self.setGeometry(self.lado,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        # faz com que a janela seja mostrada
        self.show()
    def botao(self):
        print('bottao 1 clicado')
    def botao2(self):
        print('bottao 2 clicado')
    def botao3(self):
        conteudo = self.caixatext.text()
        self.label2.setText(f"Digitou: {conteudo}")

aplicaçao = QApplication(sys.argv)
J = janela()
sys.exit(aplicaçao.exec_())


