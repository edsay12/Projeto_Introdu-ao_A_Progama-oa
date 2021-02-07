from PyQt5 import uic,QtWidgets

# aqui eu importei a imagem da tela de login
import imagens
import imagemf
import imagen2
# importado a biblioteca responsavel pelo banco de dados
import pymysql

import time

# fechando a pagina de erro
def erroclose():
    Erro.close()


try:
# conexao com o banco de dados 
    conexao = pymysql.connect(
        host="localhost",user="root",passwd="",database="introduçaoaprogamaçao"
    )

    # inicia a conecçao com o banco de dados 
    cursor = conexao.cursor()
except:

    app= QtWidgets.QApplication([])
    Erro =uic.loadUi("paginas/erro.ui")
    Erro.show()
    Erro.label.setText("Erro de Acesso ao banco")
    
    
    # botao de funçao
    Erro.pushButton.clicked.connect(erroclose)

    app.exec()
    print("erro no banco de dados ")
    
else:
#    telas de ediçao 
    def Telacadastroprodutos1():
        Telacadastroprodutos.show()

    


    

       



#   ********************************************************************** Cadastro de usuario******************************************************************************************************************************
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
                # janela de cadastro de novos usuarios
    def cadastro():
        Telacadastroprodutos.label_2.setText("")
        Telacadastro.label_7.setText("")
        Telacadastro.show()

# ***************************************************************************************************************************************************************************



# ********************************************************************Tela_Usuario************************************************************************************


    def excluir_usuario():
        # retorna o numero da coluna adicionada
        row = painel_usuario.tableWidget.currentRow()
        # remove a linha adicionada
        painel_usuario.tableWidget.removeRow(row)
        cursor.execute("SELECT id_usuarios FROM usuarios")
        id = cursor.fetchall()
        idusuario = id[row][0]
        cursor.execute(f"DELETE FROM usuarios WHERE id_usuarios  =  {idusuario} ")
        conexao.commit()
        
    def update_usuarios():
        # RECEBE OS VALORES DO LINE EDIT E MANDA PRO BANCO
        row = painel_usuario.tableWidget.currentRow()
        cursor.execute("SELECT id_usuarios FROM usuarios")
        id = cursor.fetchall()
        idusuario = id[row][0]
        login = Tela_editar_usuario.lineEdit.text()
        senha = Tela_editar_usuario.lineEdit_2.text()
        email = Tela_editar_usuario.lineEdit_3.text()
        nome = Tela_editar_usuario.lineEdit_4.text()
        sobrenome = Tela_editar_usuario.lineEdit_5.text()
        # mandando os valores pro banco
        cursor.execute(f"UPDATE usuarios SET logim = '{login}' ,senha = '{senha}', email = '{email}',nome = '{nome}' ,sobrenome = '{sobrenome}' WHERE id_usuarios  =  '{idusuario}' ")
        conexao.commit()

        Tela_editar_usuario.close()
        painel() 

    def editar_usuario():
        Tela_editar_usuario.show()
       
    # retorna numero da coluna adicionada
        row = painel_usuario.tableWidget.currentRow()
        cursor.execute("SELECT id_usuarios FROM usuarios")
        id = cursor.fetchall()
        idusuario = id[row][0]
        
        # mostrar valores no formulario
        cursor.execute(f"SELECT * from usuarios WHERE id_usuarios  =  {idusuario}")
        id1 = cursor.fetchall()
        # login
        Tela_editar_usuario.lineEdit.setText(f"{id1[0][4]}")
        # senha
        Tela_editar_usuario.lineEdit_2.setText(f"{id1[0][5]}")
        # email
        Tela_editar_usuario.lineEdit_3.setText(f"{id1[0][3]}")
        # nome
        Tela_editar_usuario.lineEdit_4.setText(f"{id1[0][1]}")
        # sobrenome
        Tela_editar_usuario.lineEdit_5.setText(f"{id1[0][2]}")
        painel_usuario.close()   
     
    # funçao que abre o painel e atualiza os dados
    def painel():
            painel_usuario.show()
            cursor.execute("SELECT * FROM usuarios")
            dados = cursor.fetchall()

                    # impressao dos usuarios na tela
            painel_usuario.tableWidget.setRowCount(len(dados))
            painel_usuario.tableWidget.setColumnCount(7)

            # Adicionando dados para a visualizaçao
            for c in range(0,len(dados)):
                for b in range(0,7):
                    # adiciona os valores na tabela
                    painel_usuario.tableWidget.setItem(c,b,QtWidgets.QTableWidgetItem(str(dados[c][b])))



    def exit_usuario_editar():
                Tela_editar_usuario.close()
                painel_usuario.show()

# *********************************************************************************************************************************************************


# ********************************************************************************tela de login****************************************************************************************************************************************
        


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
                Telalogin.close()
                painel_de_controle.show()
            
            else:
                Telalogin .label_aviso.setText("     Login ou senha incorretos ")
        except:
            Telalogin .label_aviso.setText("     Voce nao possui Cadastro  ")
# ********************************************************************************************************************************************************************
            

    
# ************************************************************************clientes**************************************************************************************
    
                
    def painelclientes():
        painel_clientes.show()


        
# **********************************************************************************************************************************************************************

# **********************************************************************produtos**************************************************************************************




    def painelprodutos():
        painel_produtos.show()
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()
                # impressao dos usuarios na tela
        painel_produtos.tableWidget.setRowCount(len(dados))
        painel_produtos.tableWidget.setColumnCount(7)
        # Adicionando dados para a visualizaçao
        for c in range(0,len(dados)):
            for b in range(0,7):
                # adiciona os valores na tabela
                painel_produtos.tableWidget.setItem(c,b,QtWidgets.QTableWidgetItem(str(dados[c][b])))
    def painelvendas():
        painel_vendas.show()


    
 

    def cadastro_produtos():
        nomeproduto = Telacadastroprodutos.lineEdit.text()
        tipoproduto = Telacadastroprodutos.comboBox.currentText()
        quantidadeproduto = Telacadastroprodutos.lineEdit_2.text()
        marcaproduto = Telacadastroprodutos.lineEdit_3.text()
        valorproduto = Telacadastroprodutos.lineEdit_4.text()
        try:
            cursor.execute("INSERT INTO produtos(nome,tipo,valor,quantidade,marca)  VALUES('"+nomeproduto+"','"+tipoproduto+"','"+valorproduto+"','"+quantidadeproduto+"','"+marcaproduto+"')")
            
        except:
            Telacadastroprodutos.label_2.setText("Erro ao adicionar produto")
        else:
             Telacadastroprodutos.label_2.setText("Adicionado Com sucesso")
             conexao.commit()
# ****************************************************************************************************************************************************************************

        

       
    app= QtWidgets.QApplication([])


    # *******************************chamada das telas********************************************************* 
    Telalogin  =uic.loadUi("paginas/paginaLogin.ui")

    Telacadastro =uic.loadUi("paginas/cadastro.ui")

    painel_usuario = uic.loadUi("paginas/cpanel.ui")

    painel_de_controle = uic.loadUi("paginas/paineldecontrole.ui")
    
    Tela_editar_usuario  = uic.loadUi("paginas/editar_usuario.ui")
    painel_clientes= uic.loadUi("paginas/cpanelclientes.ui")
    painel_produtos= uic.loadUi("paginas/cpanelprodutos.ui")
    painel_vendas= uic.loadUi("paginas/cpanelvendas.ui")
    Telacadastroprodutos = uic.loadUi("paginas\cadastrodeprodutos.ui")

    # ********************************bottoes de click*********************************************************
    # verifica as informaçoes e entra no sistema
    Telalogin .botao1.clicked.connect(login)
    # botao responsavel por cadastrar um novo usuario
    Telalogin .pushButton_2.clicked.connect(cadastro)
    
    painel_usuario.pushButton_6.clicked.connect(excluir_usuario)
    painel_usuario.pushButton_7.clicked.connect(editar_usuario)
    painel_usuario.pushButton_8.clicked.connect(cadastro)

    Telacadastro.pushButton.clicked.connect(Cadastrabanco)
    

    Tela_editar_usuario.pushButton.clicked.connect(update_usuarios)
    Tela_editar_usuario.pushButton_2.clicked.connect(exit_usuario_editar)

    

    
    painel_produtos.pushButton_8.clicked.connect(Telacadastroprodutos1)

    Telacadastroprodutos.pushButton.clicked.connect(cadastro_produtos)




    painel_de_controle.pushButton.clicked.connect(painel)
    painel_de_controle.pushButton_2.clicked.connect(painelprodutos)
    painel_de_controle.pushButton_3.clicked.connect(painelclientes)
    painel_de_controle.pushButton_4.clicked.connect(painelvendas)
    
    
    



    # *******************************mostra a tema e inicia o progama*****************************************
    Telalogin .show()
    app.exec()
    # *******************************mostra a tema e inicia o progama*****************************************
