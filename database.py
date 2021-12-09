import mysql.connector
from getpass import getpass
from getpass import getpass
from mysql.connector import connect
from mysql.connector import Error


#dette er får la andre å få tilgang til databasen med sin egen mysql connection, 
# samt at dette gjør det mye mer sikkert.
try:
    db=mysql.connector.connect(
        host="localhost",
        user=input("Tast inn brukernavn"),
        password = getpass("Tast inn  passord: "),
        database="kalkulator")

except Error as e:
    print(e)

except Error as e:
    print(e)

c = db.cursor()