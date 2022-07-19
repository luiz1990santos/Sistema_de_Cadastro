import mysql.connector

banco = mysql.connector.connect(
   host= 'localhost',
    user='root',
    passwd=''
)# Variável com od dados pare conectar ao banco.

cursor = banco.cursor()

cursor.execute()
