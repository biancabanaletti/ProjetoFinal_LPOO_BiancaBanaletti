import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="lpoo_projeto_biancabanaletti",
        user="postgres",
        password="1234"
    )