import mysql.connector
from getpass import getpass
from getpass import getpass
from mysql.connector import connect
from mysql.connector import Error



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