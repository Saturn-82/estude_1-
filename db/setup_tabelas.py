import sqlite3

def criar_tabelas():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # Tabela de usuários (caso ainda não tenha)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        );
    ''')

    # Tabela de curso
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS curso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        );
    ''')

    # Tabela de matérias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            dificuldade TEXT,
            FOREIGN KEY (curso_id) REFERENCES curso(id)
        );
    ''')

    # Tabela de disponibilidade de horas por dia
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disponibilidade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            dia TEXT NOT NULL,
            horas_disponiveis INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        );
    ''')

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")

# Executar a função ao rodar o arquivo
if __name__ == "__main__":
    criar_tabelas()
