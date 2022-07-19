from PyQt5 import uic,QtWidgets #modulo importado para ler o arquivo UI
import mysql.connector

banco = mysql.connector.connect(
   host= 'localhost',
    user='root',
    passwd='2403120818',
    database='cadastro'
)

def funcao_principal():#função para ler os campos do app
    print('teste')

def funcao_cadastro_frota():
    cadastro_frota.show()
    campo1 = cadastro_frota.lineEdit.text() #Lê o que foi digitado no campo.
    campo2 = cadastro_frota.lineEdit_2.text()
    campo3 = cadastro_frota.lineEdit_3.text()
    campo4 = cadastro_frota.lineEdit_4.text()
    print(f'Motorista: {campo1}')
    print(f'Placa: {campo2}')
    print(f'Quilometragem: {campo3}')
    print(f'Observação: {campo4}')
    checagem = ''
    if cadastro_frota.radioButton.isChecked():
        checagem='Entrada'
    elif cadastro_frota.radioButton_2.isChecked():
        checagem='Saída'

    cursor = banco.cursor()
    comando = 'INSERT INTO FROTA (ID_FROTA,MOTORISTA,PLACA,KM,CHECK_IN_OUT,OBSERVACAO,DATA) VALUES (%s,%s,%s,%s,%s,%s)'
    dados = ('',str(campo1),str(campo2),str(campo3),str(campo4),checagem,'')
    cursor.execute(comando,dados)
    banco.commit()

def funcao_consulta():
    consulta.show()

def funcao_cadastro_terceiros():
    cadastro_terceiros.show()
    campo1 = cadastro_terceiros.lineEdit.text()
    campo2 = cadastro_terceiros.lineEdit_2.text()
    campo3 = cadastro_terceiros.lineEdit_4.text()
    campo4 = cadastro_terceiros.lineEdit_5.text()

    print(f'Nome: {campo1}')
    print(f'Documento: {campo2}')
    print(f'Observação: {campo3}')
    print(f'Responsável: {campo4}')

    if cadastro_terceiros.radioButton_3.isChecked():
        print('ENVIO')
    elif cadastro_terceiros.radioButton_4.isChecked():
        print('RETIRADA')
    elif cadastro_terceiros.radioButton_5.isChecked():
        print('OUTROS')

    if cadastro_terceiros.radioButton.isChecked():
        print('ENTRADA')
    elif cadastro_terceiros.radioButton_2.isChecked():
        print('SAÍDA')

app=QtWidgets.QApplication([]) #Cria a app
menu_principal=uic.loadUi('menu_principal.ui') #Carrega o arquivo UI
cadastro_frota=uic.loadUi('cadastro_frota.ui') #Para carregar a próximo tela
consulta=uic.loadUi('consulta.ui')
cadastro_terceiros=uic.loadUi('cadastro_terceiros.ui')
menu_principal.pushButton.clicked.connect(funcao_cadastro_frota)#interação com os botões.
menu_principal.pushButton_2.clicked.connect(funcao_consulta)
menu_principal.pushButton_3.clicked.connect(funcao_cadastro_terceiros)
menu_principal.pushButton_4.clicked.connect(funcao_principal)
cadastro_frota.pushButton.clicked.connect(funcao_cadastro_frota)
cadastro_terceiros.pushButton.clicked.connect(funcao_cadastro_terceiros)

menu_principal.show()
app.exec()