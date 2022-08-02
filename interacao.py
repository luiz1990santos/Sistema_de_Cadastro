import mysql.connector
from PyQt5 import uic, QtWidgets  # modulo importado para ler o arquivo UI

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cadastro'
)

def funcao_cadastro_frota():
    cadastro_frota.show()
    id_frota = int(cadastro_frota.radioButton_2.isChecked())
    motorista = str(cadastro_frota.lineEdit.text())  # Lê o que foi digitado no campo.
    placa = str(cadastro_frota.lineEdit_2.text())
    km = str(cadastro_frota.lineEdit_3.text())
    observacao = str(cadastro_frota.lineEdit_4.text())
    controle = str(cadastro_frota.lineEdit_5.text())
    data_atual = str(cadastro_frota.radioButton.isChecked())

    comando = "INSERT INTO FROTA VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor = banco.cursor()
    dados = (id_frota, motorista, placa, km, controle, observacao, data_atual)
    cursor.execute(comando, dados)
    banco.commit()
    cadastro_frota.lineEdit.setText('')
    cadastro_frota.lineEdit_2.setText('')
    cadastro_frota.lineEdit_3.setText('')
    cadastro_frota.lineEdit_4.setText('')
    cadastro_frota.lineEdit_5.setText('')


def funcao_consulta_frota():
    consulta_frota.show()
    cursor = banco.cursor()
    comando_sql = 'SELECT * FROM FROTA'
    cursor.execute(comando_sql)
    valor = cursor.fetchall()
    consulta_frota.tableWidget.setRowCount(len(valor))
    consulta_frota.tableWidget.setColumnCount(7)
    for i in range(0, len(valor)):
        for j in range(0, 7):
            consulta_frota.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor[i][j])))


def funcao_cadastro_terceiros():
    cadastro_terceiros.show()
    id_terceiros = int(cadastro_terceiros.radioButton.isChecked())
    nome = str(cadastro_terceiros.lineEdit.text())
    documento = str(cadastro_terceiros.lineEdit_2.text())
    finalidade = str(cadastro_terceiros.lineEdit_3.text())
    observacao = str(cadastro_terceiros.lineEdit_4.text())
    controle = str(cadastro_terceiros.lineEdit_5.text())
    responsavel = str(cadastro_terceiros.lineEdit_6.text())
    data_atual = str(cadastro_terceiros.radioButton_2.isChecked())

    comando = "INSERT INTO TERCEIROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = banco.cursor()
    dados = (id_terceiros, nome, documento, finalidade, observacao, controle, responsavel, data_atual)
    cursor.execute(comando, dados)
    banco.commit()
    cadastro_terceiros.lineEdit.setText('')
    cadastro_terceiros.lineEdit_2.setText('')
    cadastro_terceiros.lineEdit_3.setText('')
    cadastro_terceiros.lineEdit_4.setText('')
    cadastro_terceiros.lineEdit_5.setText('')
    cadastro_terceiros.lineEdit_6.setText('')


def funcao_consulta_terceiros():
    consulta_terceiros.show()
    cursor = banco.cursor()
    comando_sql = 'SELECT * FROM TERCEIROS'
    cursor.execute(comando_sql)
    valor = cursor.fetchall()
    consulta_terceiros.tableWidget.setRowCount(len(valor))
    consulta_terceiros.tableWidget.setColumnCount(8)
    for i in range(0, len(valor)):
        for j in range(0, 8):
            consulta_terceiros.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor[i][j])))


app = QtWidgets.QApplication([])  # Cria a app
menu_principal = uic.loadUi('menu_principal.ui')  # Carrega o arquivo UI
cadastro_frota = uic.loadUi('cadastro_frota.ui')  # Para carregar a próximo tela
consulta_frota = uic.loadUi('consulta_frota.ui')
cadastro_terceiros = uic.loadUi('cadastro_terceiros.ui')
consulta_terceiros = uic.loadUi('consulta_terceiros.ui')

menu_principal.pushButton.clicked.connect(funcao_cadastro_frota)  # interação com os botões.
menu_principal.pushButton_2.clicked.connect(funcao_consulta_frota)
menu_principal.pushButton_3.clicked.connect(funcao_cadastro_terceiros)
menu_principal.pushButton_4.clicked.connect(funcao_consulta_terceiros)
cadastro_frota.pushButton.clicked.connect(funcao_cadastro_frota)
cadastro_terceiros.pushButton.clicked.connect(funcao_cadastro_terceiros)

menu_principal.show()
app.exec()
