import psycopg
from psycopg import sql
from flask_bcrypt import generate_password_hash

# Conecta ao banco de dados existente
with psycopg.connect(host="localhost", dbname="postgres", user="sasuke", password="postgres") as conn:
    conn.autocommit = True
    database_name = "martial_arts_library"
    
    with conn.cursor() as cur:
        # Cria um novo banco de dados
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))

# Conecta ao novo banco de dados criado
with psycopg.connect(host="localhost", dbname=database_name, user="sasuke", password="postgres") as conn:
    with conn.cursor() as cur:
        # Cria a tabela 'martial_arts'
        cur.execute("""
            CREATE TABLE IF NOT EXISTS martial_arts (
                id serial PRIMARY KEY,
                name text,
                points integer,
                category text
            )
        """)

        # Cria a tabela 'users'
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                name text,
                nickname text,
                password text
            )
        """)

        # Insere dados na tabela 'martial_arts'
        cur.execute(
            "INSERT INTO martial_arts (name, points, category) VALUES (%s, %s, %s)",
            ('Capoeira', 7, 'Dance')
        )

        cur.execute(
            "INSERT INTO martial_arts (name, points, category) VALUES (%s, %s, %s)",
            ('Jiu Jitsu BR', 9, 'Grappling')
        )

        cur.execute(
            "INSERT INTO martial_arts (name, points, category) VALUES (%s, %s, %s)",
            ('Karate', 9, 'Striking')
        )

        # Insere dados na tabela 'users'
        cur.execute(
            "INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)",
            ('Izuku Midoriya', 'midoriya', generate_password_hash("hero").decode('utf-8'))
        )

        cur.execute(
            "INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)",
            ('Bakugo Katsuki', 'bakugo', generate_password_hash("explosion").decode('utf-8'))
        )

        cur.execute(
            "INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)",
            ('Uchiha Sasuke', 'sasuke', 'sharingan')
        )

    # Salva as mudanças no banco de dados
    conn.commit()
