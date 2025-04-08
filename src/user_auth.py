import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("db/database.sqlite3")
    cursor = conexao.cursor()
    return conexao, cursor

def criar_tabela_usuarios():
    conexao, cursor = conectar_banco()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        );
    """)
    conexao.commit()
    conexao.close()

def cadastrar_usuario(nome, email, senha):
    try:
        conexao, cursor = conectar_banco()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este e-mail já está cadastrado.")
    finally:
        conexao.close()

def login_usuario(email, senha):
    conexao, cursor = conectar_banco()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()
    conexao.close()
    if usuario:
        print(f"Bem-vindo(a), {usuario[1]}!")
        return True
    else:
        print("E-mail ou senha incorretos.")
        return False
