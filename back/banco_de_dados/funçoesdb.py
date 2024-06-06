import sqlite3
import re

def validar_nome(nome):
    match = re.match(r'^[a-zA-Z\s]{1,50}$', nome)
    return match is not None

# Função para validar CPF
def validar_cpf(cpf):
    match = re.match(r'^\d{11}$', cpf) 
    return match is not None

# Função para validar telefone
def validar_telefone(telefone):
    match = re.match(r'^\d{11}$', telefone)
    return match is not None

def validar_data_nascimento(data_nascimento):
    match = re.match(r'^\d{8}$', data_nascimento)
    return match is not None


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

