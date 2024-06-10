import mysql.connector

def connect():
    conbd = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'comercio'
    )
    return conbd