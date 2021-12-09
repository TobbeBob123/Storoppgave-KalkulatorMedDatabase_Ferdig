import mysql.connector


db=mysql.connector.connect(
user="root",
host="127.0.0.1",
password="Ullmann02",
port="3306",
database="kalkulator")
c=db.cursor()

