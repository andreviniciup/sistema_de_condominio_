import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('condominio.db')
cursor = conn.cursor()

# Criando a tabela de moradores
cursor.execute('''
CREATE TABLE IF NOT EXISTS moradores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    telefone TEXT NOT NULL,
    bloco TEXT NOT NULL,
    apartamento TEXT NOT NULL,
    placa_carro TEXT NOT NULL
)
''')

# Criando a tabela de visitantes
cursor.execute('''
CREATE TABLE IF NOT EXISTS visitantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    morador_id INTEGER,
    nome_visitante TEXT NOT NULL,
    horario1 TEXT NOT NULL,
    horario2 TEXT NOT NULL,
    data TEXT NOT NULL,
    nome_morador TEXT NOT NULL,
    bloco TEXT NOT NULL,
    apartamento TEXT NOT NULL,
    FOREIGN KEY (morador_id) REFERENCES moradores(id)
)
''')

# Criando a tabela de encomendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS encomenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    apartamento TEXT,
    bloco TEXT,
    data_entrega TEXT,
    data_retirada TEXT,
    porteiro TEXT,
    cpf TEXT NOT NULL DEFAULT '',
    nome_de_quem_retirou TEXT
)
''')

# Inserindo dados na tabela encomenda a partir da tabela moradores
cursor.execute('''
INSERT INTO encomenda (nome, apartamento, bloco)
SELECT 
    nome,
    apartamento,
    bloco
FROM 
    moradores
''')

# Salvando (commit) as mudanças
conn.commit()

# Fechando a conexão
conn.close()

# Funções auxiliares
def inserir_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO moradores (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
    conn.commit()
    conn.close()

def inserir_visitante(nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Obtendo o morador_id baseado em nome, bloco e apartamento
    cursor.execute('''
    SELECT id FROM moradores
    WHERE nome = ? AND bloco = ? AND apartamento = ?
    ''', (nome_morador, bloco, apartamento))
    morador = cursor.fetchone()
    
    if morador:
        morador_id = morador[0]
        cursor.execute('''
        INSERT INTO visitantes (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento))
        conn.commit()
    else:
        print("Morador não encontrado.")
    
    conn.close()

def pesquisar_morador(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Consulta SQL para obter informações do morador
    cursor.execute('''
    SELECT 
        nome, 
        cpf,
        data_nascimento,
        telefone,
        bloco, 
        apartamento, 
        placa_carro
    FROM moradores
    WHERE nome = ? AND bloco = ? AND apartamento = ?
    ''', (nome, bloco, apartamento))
    
    resultados = cursor.fetchall()
    
    if resultados:
        for linha in resultados:
            print(f"Morador: {linha[0]}, CPF: {linha[1]}, Data de Nascimento: {linha[2]}, Telefone: {linha[3]}, Bloco: {linha[4]}, Apartamento: {linha[5]}, Placa do Carro: {linha[6]}")
    else:
        print("Nenhum resultado encontrado para os critérios de pesquisa fornecidos.")
    
    conn.close()
