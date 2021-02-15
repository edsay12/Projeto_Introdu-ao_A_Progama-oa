from os import O_APPEND
from PyQt5 import uic,QtWidgets

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
# aqui eu importei a imagem da tela de login
import imagens
import imagemf
import imagen2
# importado a biblioteca responsavel pelo banco de dados
import pymysql


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
    print("deu certo ")

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
        line = painel_usuario.tableWidget.currentRow()
        # remove a linha adicionada
        painel_usuario.tableWidget.removeRow(line)
        try:
            cursor.execute("SELECT id_usuarios FROM usuarios")
            id = cursor.fetchall()
            idusuario = id[line][0]
            cursor.execute(f"DELETE FROM usuarios WHERE id_usuarios  =  {idusuario} ")
        except:
            print("erro no banco")
        else:
            conexao.commit()
            print("exclusao feita com exito")

    def update_usuarios():
        # RECEBE OS VALORES DO LINE EDIT E MANDA PRO BANCO
        line = painel_usuario.tableWidget.currentRow()
        try:
            cursor.execute("SELECT id_usuarios FROM usuarios")
            id = cursor.fetchall()
            idusuario = id[line][0]
            login = Tela_editar_usuario.lineEdit.text()
            senha = Tela_editar_usuario.lineEdit_2.text()
            email = Tela_editar_usuario.lineEdit_3.text()
            nome = Tela_editar_usuario.lineEdit_4.text()
            sobrenome = Tela_editar_usuario.lineEdit_5.text()
            # mandando os valores pro banco
            cursor.execute(f"UPDATE usuarios SET logim = '{login}' ,senha = '{senha}', email = '{email}',nome = '{nome}' ,sobrenome = '{sobrenome}' WHERE id_usuarios  =  '{idusuario}' ")

        except:
            print("erro de acesso ao banco")
        else:
            conexao.commit()
            print("dados salvos com sucesso ")

        Tela_editar_usuario.close()
        painel() 

    def editar_usuario():
        Tela_editar_usuario.show()
       
    # retorna numero da coluna adicionada
        line = painel_usuario.tableWidget.currentRow()
        cursor.execute("SELECT id_usuarios FROM usuarios")
        id = cursor.fetchall()
        idusuario = id[line][0]
        
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
        global login1
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
        painel_clientes.show()
        cursor.execute("SELECT * FROM clientes")
        dados = cursor.fetchall()
                # impressao dos usuarios na tela
        painel_clientes.tableWidget.setRowCount(len(dados))
        painel_clientes.tableWidget.setColumnCount(7)
        # Adicionando dados para a visualizaçao
        for c in range(0,len(dados)):
            for b in range(0,7):
                # adiciona os valores na tabela
                painel_clientes.tableWidget.setItem(c,b,QtWidgets.QTableWidgetItem(str(dados[c][b])))



    
    def excluir_clientes():
        # retorna o numero da coluna adicionada
        line = painel_clientes.tableWidget.currentRow()
        # remove a linha adicionada
        painel_clientes.tableWidget.removeRow(line)
        cursor.execute("SELECT id_clientes FROM clientes")
        id = cursor.fetchall()
        idclientes = id[line][0]
        try:
            cursor.execute(f"DELETE FROM clientes WHERE id_clientes = '{idclientes}'")
            conexao.commit()
        except:
            print("adicionar aqui ")



    def editar_cliente():
        tela_editar_cliente.show()
        line = painel_clientes.tableWidget.currentRow()
        cursor.execute("SELECT id_clientes FROM clientes")
        id = cursor.fetchall()
        idclientes = id[line][0]
        
        # mostrar valores no formulario
        cursor.execute(f"SELECT * from clientes WHERE id_clientes = {idclientes}")
        id1 = cursor.fetchall()
        # nome
        tela_editar_cliente.lineEdit.setText(f"{id1[0][1]}")
        # cpf
        tela_editar_cliente.lineEdit_3.setText(f"{id1[0][3]}")
        # endereçp
        tela_editar_cliente.lineEdit_2.setText(f"{id1[0][2]}")
        # complemento
        tela_editar_cliente.lineEdit_4.setText(f"{id1[0][4]}")
        # Telefone 
        tela_editar_cliente.lineEdit_5.setText(f"{id1[0][5]}")

    def update_clientes():
        line = painel_clientes.tableWidget.currentRow()
        cursor.execute("SELECT id_clientes FROM clientes")
        id = cursor.fetchall()
        idcliente = id[line][0]

        Nome = tela_editar_cliente.lineEdit.text()
        Endereço = tela_editar_cliente.lineEdit_2.text()
        Cpf = tela_editar_cliente.lineEdit_3.text()
        Complemento = tela_editar_cliente.lineEdit_4.text()
        Telefone = tela_editar_cliente.lineEdit_5.text()

        # mandando os valores pro banco
        try:
            cursor.execute(f"UPDATE clientes SET nome = '{Nome}' ,Endereço = '{Endereço}', cpf= '{Cpf}',complemento = '{Complemento}' ,telefone = '{Telefone}' WHERE id_clientes  =  '{idcliente}' ")
            conexao.commit()
        except:
            print("erro no banco")
        else:
            print("sucesso")
            tela_editar_cliente.close()
            painelclientes()

    def cadastroclientes1():
        Telacadastroclientes.show()
 
    def cadastrarcliente():
        nomecliente = Telacadastroclientes.lineEdit.text()
        endereçocliente = Telacadastroclientes.lineEdit_2.text()
        telefonecliente = Telacadastroclientes.lineEdit_3.text()
        complemento = Telacadastroclientes.lineEdit_4.text()
        cpfcliente = Telacadastroclientes.lineEdit_5.text()
        try:
            cursor.execute("INSERT INTO clientes(nome,cpf,endereço,complemento,telefone) VALUES('"+nomecliente+"','"+cpfcliente+"','"+endereçocliente+"','"+complemento+"','"+telefonecliente+"') ")
        except:
            
            Telacadastroclientes.label_2.setText("ouve um problema ao adiciona cliente")
        else:
            Telacadastroclientes.label_2.setText("Sucesso ao adiciona cliente")
            conexao.commit()




        


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

    def editar_produtos():
        tela_editar_produto.show()
        line = painel_produtos.tableWidget.currentRow()
        cursor.execute("SELECT id_produtos FROM produtos")
        id = cursor.fetchall()
        idprodutos = id[line][0]
        
        # mostrar valores no formulario
        cursor.execute(f"SELECT * from produtos WHERE id_produtos =  {idprodutos}")
        id1 = cursor.fetchall()
        # nome
        tela_editar_produto.lineEdit.setText(f"{id1[0][1]}")
        # quantidade
        tela_editar_produto.lineEdit_3.setText(f"{id1[0][3]}")
        # modelo
        tela_editar_produto.lineEdit_4.setText(f"{id1[0][5]}")
        # valor
        tela_editar_produto.lineEdit_5.setText(f"{id1[0][4]}")

    def update_produtos():
        print("updatando ")
        line= painel_produtos.tableWidget.currentRow()
        cursor.execute("SELECT id_produtos FROM produtos")
        id = cursor.fetchall()
        idprodutos = id[line][0]
        Nome =  tela_editar_produto.lineEdit.text()
        Quantidade =  tela_editar_produto.lineEdit_3.text()
        Modelo =  tela_editar_produto.lineEdit_4.text()
        Tipo =tela_editar_produto.comboBox.currentText()
        Valor =  tela_editar_produto.lineEdit_5.text()

        # mandando os valores pro banco
        try:
            cursor.execute(f"UPDATE produtos SET nome = '{Nome}' ,quantidade = '{Quantidade}', marca = '{Modelo}',tipo = '{Tipo}' ,valor = '{Valor}' WHERE id_produtos  =  '{idprodutos}' ")
            conexao.commit()
        except:
            print("erro no banco")
        else:
            print("sucesso")
            tela_editar_produto.close()
            painelprodutos()


    def excluir_produto():
        # retorna o numero da coluna adicionada
        line = painel_produtos.tableWidget.currentRow()
        # remove a linha adicionada
        painel_produtos.tableWidget.removeRow(line)
        cursor.execute("SELECT id_produtos FROM produtos")
        id = cursor.fetchall()
        idproduto = id[line][0]
        cursor.execute(f"DELETE FROM produtos WHERE id_produtos  =  {idproduto}")
        conexao.commit()



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

    def Telacadastroprodutos1():
        Telacadastroprodutos.show()

# ****************************************************************************************************************************************************************************
# *************************************************************vendas************************************************************

    def painelvendas():
            painel_vendas.show()
            cursor.execute("SELECT * FROM vendas ")
            dados = cursor.fetchall()
                # impressao dos usuarios na tela
            painel_vendas.tableWidget.setRowCount(len(dados))
            painel_vendas.tableWidget.setColumnCount(6)
            # Adicionando dados para a visualizaçao
            for c in range(0,len(dados)):
                for b in range(0,6):
                # adiciona os valores na tabela
                    painel_vendas.tableWidget.setItem(c,b,QtWidgets.QTableWidgetItem(str(dados[c][b])))

    # tela de cadastro
    def cadastrovendas():
        # listas vazias para adiçao dos  nomes
        lista_produto = []
        lista_cliente = []
        # pega os prudutos e nomes cadastrados do banco  
        cursor.execute("SELECT nome FROM produtos ")
        nome_produto = cursor.fetchall()
        cursor.execute("SELECT nome FROM clientes ")
        nome_cliente = cursor.fetchall()
        # *********************************************
        # adicionando os nomes pegos no banco nas listas
        for c in nome_produto:
            lista_produto.append(c[0])
        for b in nome_cliente:
            lista_cliente.append(b[0])
        # *************************************************   
        # mostra os valores no combobox
        Telacadastrovendas.comboBox.addItems(lista_produto)
        Telacadastrovendas.comboBox_2.addItems(lista_cliente)
        Telacadastrovendas.show()

#   tela de cadastro
    def update_vendas():
        Produto_vendas = Telacadastrovendas.comboBox.currentText()
        Cliente_vendas = Telacadastrovendas.comboBox_2.currentText()
        Quantidade_vendas = Telacadastrovendas.lineEdit.text()
        cursor.execute(f"SELECT valor FROM produtos WHERE nome = '{Produto_vendas}' ")
        valor = cursor.fetchall()
        valor1 = str(valor[0][0])




        try:
            cursor.execute(f"INSERT INTO vendas(nome_produto,nome_cliente,quatidade_produto,valor,vendedor) VALUES(  '"+Produto_vendas+"','"+Cliente_vendas+"', '"+Quantidade_vendas+"', '"+valor1+"','"+login1+"')")
            conexao.commit()
        except:
            print("erro no banco")
        else:
            print("tudo okay ")
            

# ***************************************  tela de ediçao****************************************************************
    def vendas_editar():
         # listas vazias para adiçao dos  nomes
        lista_produto = []
        lista_cliente = []
        # pega os prudutos e nomes cadastrados do banco  
        cursor.execute("SELECT nome FROM produtos ")
        nome_produto = cursor.fetchall()
        cursor.execute("SELECT nome FROM clientes ")
        nome_cliente = cursor.fetchall()
        # *********************************************
        # adicionando os nomes pegos no banco nas listas
        for c in nome_produto:
            lista_produto.append(c[0])
        for b in nome_cliente:
            lista_cliente.append(b[0])
        # *************************************************   
        # mostra os valores no combobox
        Telacadastrovendas2.comboBox.addItems(lista_produto)
        Telacadastrovendas2.comboBox_2.addItems(lista_cliente)
        Telacadastrovendas2.show()



    def editar_vendas ():
        print("updatando 34343")
        line= painel_vendas.tableWidget.currentRow()
        cursor.execute("SELECT id_vendas FROM vendas")
        id = cursor.fetchall()
        idvendas = id[line][0]

        Produto_vendas = Telacadastrovendas2.comboBox.currentText()
        Cliente_vendas = Telacadastrovendas2.comboBox_2.currentText()
        Quantidade_vendas = Telacadastrovendas2.lineEdit.text()

        # mandando os valores pro banco
        try:
            cursor.execute(f"UPDATE vendas SET nome_produto = '{Produto_vendas}' ,nome_cliente = '{Cliente_vendas}', quatidade_produto = '{Quantidade_vendas}',vendedor = '{login1}' WHERE id_vendas  =  '{idvendas}' ")
            conexao.commit()
        except:
            print("erro no banco")
        else:
            print("sucesso")
    # **************************************************************
            
          
    def excluir_vendas():
        # retorna o numero da coluna adicionada
        line = painel_vendas.tableWidget.currentRow()
        # remove a linha adicionada
        painel_vendas.tableWidget.removeRow(line)
        cursor.execute("SELECT id_vendas FROM vendas")
        id = cursor.fetchall()
        idvendas = id[line][0]
        cursor.execute(f"DELETE FROM vendas WHERE id_vendas  =  {idvendas}")
        conexao.commit()
        
# ***************************************************************************************************************************
# *********************************************************Nota Fiscal*******************************************************


    def salvar_nota():
        # essa parte pega o nome do cliente  e busca os dados dele no banco pra imprimir na nota
         # retorna o numero da coluna adicionada
        line = painel_vendas.tableWidget.currentRow()
        try:
            cursor.execute("SELECT id_vendas FROM vendas")
            id = cursor.fetchall()
            idvendas = id[line][0]
            cursor.execute(f"SELECT * FROM vendas WHERE id_vendas  =  {idvendas}")
            produto2 = cursor.fetchall()

            # pega os dado do cliente que realizou a a compra 
            cursor.execute(f"SELECT * FROM clientes WHERE nome =  '{produto2[0][2]}' ")
            dado_cliente = cursor.fetchall()
            # print(dado_cliente)
        except:
            print("erro no banco de dasdos")
        else:
            print("acesso oa banco com exito")

        try:
            cnv = canvas.Canvas(f"notas/{dado_cliente[0][1]}.pdf")
            minha_logo = ImageReader('img/max.jpg')
            cnv.drawImage(minha_logo, 100, 780,width=150,height=40)
            cnv.drawString(100,750,"Rua rio Bahia, 261 D ")
            cnv.drawString(100,735,"Paulista, 53413-010 ")
            cnv.drawString(100,720,"Fone: (81)98590-9703")
            cnv.drawString(100,705,"E-mail: edvandearaujo2@hotmail.com")


            cnv.drawString(400,800,"Fatura")
            cnv.drawString(400,750,"Data: 22/02/2021")
            # gerar numero altimaticamente depois
            cnv.drawString(400,735,"Fatura nº 1123")
            # importar data altomatica depois
            cnv.drawString(400,720,"Data: 22/02/2021")


            cnv.drawString(100,680,"Cobrança para:                                                             ")
            cnv.drawString(100,678,"__________________________________________________________")

            cnv.drawString(100,650,f"Nome: {dado_cliente[0][1]} ")
            cnv.drawString(100,635,f"endereço  {dado_cliente[0][4]}  ")
            cnv.drawString(100,620,f"cpf : {dado_cliente[0][2]} ")
            
            cnv.drawString(370,650,"Acima de R$ 100")
            cnv.drawString(370,635,"desconto a definir ")


            cnv.drawString(100,605," ___________________________________________________________")
            cnv.drawString(100,590," id | Quantidade |         Nome         | Preço unitario |           Valor Total ")
            cnv.drawString(100,585," ___________________________________________________________")
             # VENDAS 
            cnv.drawString(110,570,f"{produto2[0][0]}")
            cnv.drawString(150,570,f"{produto2[0][3]}")
            cnv.drawString(222,570,f"{produto2[0][1]}")
            cnv.drawString(315,570,f"{produto2[0][4]}")

            quantidade = float(produto2[0][3])
            valor =  float(produto2[0][4])

            cnv.drawString(400,570,f"{quantidade*valor} R$")


            
            # subtotal
            cnv.drawString(100,405," ___________________________________________________________")
            cnv.drawString(100,390,f" Subtotal -                                                                               {quantidade*valor} R$")
            cnv.drawString(100,385," ___________________________________________________________")

           

            
            cnv.save()
        except:
            print("erro ao salvar nota nome jae xiste")
        else:
            print("nota salva com sucesso")
        


# ****************************************************************************************************************************




    app= QtWidgets.QApplication([])


# *******************************chamada das telas***************************************************************************
    Telalogin  =uic.loadUi("paginas/paginaLogin.ui")

    Telacadastro =uic.loadUi("paginas/cadastro.ui")

    painel_usuario = uic.loadUi("paginas/cpanel.ui")

    painel_de_controle = uic.loadUi("paginas/paineldecontrole.ui")
    
    Tela_editar_usuario  = uic.loadUi("paginas/editar_usuario.ui")

    painel_clientes= uic.loadUi("paginas/cpanelclientes.ui")

    painel_produtos= uic.loadUi("paginas/cpanelprodutos.ui")

    painel_vendas= uic.loadUi("paginas/cpanelvendas.ui")

    Telacadastroprodutos = uic.loadUi("paginas\cadastrodeprodutos.ui")

    Telacadastroclientes = uic.loadUi("paginas\cadastroclientes .ui")

    tela_editar_produto = uic.loadUi("paginas/editar_produtos.ui")

    tela_editar_cliente = uic.loadUi("paginas\editar_clientes.ui")

    Telacadastrovendas = uic.loadUi("paginas/cadastrovendas.ui")
    Telacadastrovendas2 = uic.loadUi("paginas/cadastrovendas2.ui")
    


    # ********************************bottoes de click*********************************************************
    # verifica as informaçoes e entra no sistema
    Telalogin .botao1.clicked.connect(login)
    # botao responsavel por cadastrar um novo usuario
    Telalogin .pushButton_2.clicked.connect(cadastro)
    
    painel_usuario.pushButton_6.clicked.connect(excluir_usuario)
    painel_usuario.pushButton_7.clicked.connect(editar_usuario)
    painel_usuario.pushButton_8.clicked.connect(cadastro)
    Tela_editar_usuario.pushButton.clicked.connect(update_usuarios)
    Tela_editar_usuario.pushButton_2.clicked.connect(exit_usuario_editar)

    
    Telacadastro.pushButton.clicked.connect(Cadastrabanco)
    

    painel_produtos.pushButton_8.clicked.connect(Telacadastroprodutos1)
    painel_produtos.pushButton_6.clicked.connect(excluir_produto)
    painel_produtos.pushButton_7.clicked.connect(editar_produtos)
    tela_editar_produto.pushButton.clicked.connect(update_produtos)
    Telacadastroprodutos.pushButton.clicked.connect(cadastro_produtos)

    tela_editar_cliente.pushButton.clicked.connect(update_clientes)
    painel_clientes.pushButton_8.clicked.connect(cadastroclientes1)
    painel_clientes.pushButton_6.clicked.connect(excluir_clientes)
    painel_clientes.pushButton_7.clicked.connect(editar_cliente)
    Telacadastroclientes.pushButton.clicked.connect(cadastrarcliente)

    
    painel_vendas.pushButton_8.clicked.connect(cadastrovendas)
    painel_vendas.pushButton_6.clicked.connect(excluir_vendas)
    painel_vendas.pushButton_7.clicked.connect(vendas_editar)
    painel_vendas.pushButton_9.clicked.connect(salvar_nota)

    Telacadastrovendas.pushButton.clicked.connect(update_vendas)

    Telacadastrovendas2.pushButton.clicked.connect(editar_vendas )
    
    # botoes do painel principal eles abrem as tela de cadastro
    painel_de_controle.pushButton.clicked.connect(painel)
    painel_de_controle.pushButton_2.clicked.connect(painelprodutos)
    painel_de_controle.pushButton_3.clicked.connect(painelclientes)
    painel_de_controle.pushButton_4.clicked.connect(painelvendas)
    # ************************************************************
    

    # *******************************mostra a tema e inicia o progama*****************************************
    Telalogin .show()
    app.exec()
    # *******************************mostra a tema e inicia o progama*****************************************
