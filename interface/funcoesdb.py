import sqlite3
from validar_entry import *
from tkinter import messagebox

class criarconexao:
    def __init__(self, db_name):
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

def morador_exists(cursor, nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    """
    Verifica se um morador com as informações fornecidas existe no banco de dados.
    
    :param cursor: Cursor do banco de dados
    :param nome: Nome do morador
    :param cpf: CPF do morador
    :param data_nascimento: Data de nascimento do morador
    :param telefone: Telefone do morador
    :param bloco: Bloco onde o morador reside
    :param apartamento: Apartamento onde o morador reside
    :param placa_carro: Placa do carro do morador
    :return: True se o morador existir, False caso contrário
    """
    sql = """
    SELECT 1 FROM moradores
    WHERE nome = ? AND cpf = ? AND data_nascimento = ? AND telefone = ? AND bloco = ? AND apartamento = ? AND placa_carro = ?
    """
    cursor.execute(sql, (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
    morador_encontrado = cursor.fetchone()
    return morador_encontrado is not None

def inserir_morador(db_conn, nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido. Deve conter exatamente 11 números.")
        return
    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Deve conter exatamente 11 números.")
        return
    if not validar_data_nascimento(data_nascimento):
        messagebox.showerror("Erro", "Data de nascimento inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_placa_carro(placa_carro):
        messagebox.showerror("Erro", "Placa de Carro inválida. Deve conter 7 caracteres alfanuméricos.")
        return

    try:
        if morador_exists(db_conn.cursor, nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
            messagebox.showerror("Erro", "Morador já existe no banco de dados.")
        else:
            db_conn.cursor.execute('''
            INSERT INTO moradores (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
            db_conn.conn.commit()
            messagebox.showinfo("Sucesso", "Morador inserido com sucesso.")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")

def inserir_visitante(db_conn, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento):
    cursor = db_conn.cursor
    
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
        db_conn.conn.commit()
    else:
        print("Morador não encontrado.")

def pesquisar_morador(db_conn, nome, bloco, apartamento):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return

    query ="SELECT nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro FROM moradores WHERE nome = ? AND bloco = ? AND apartamento = ?"
    db_conn.cursor.execute(query, (nome, bloco, apartamento))
    dados = db_conn.cursor.fetchone()
    return dados

def inserir_encomenda(db_conn, nome, data_entrega, bloco, apartamento, porteiro):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_data_nascimento(data_entrega):
        messagebox.showerror("Erro", "Data de entrega inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_nome(porteiro):
        messagebox.showerror("Erro", "Nome do porteiro inválido. Deve conter apenas letras e até 50 caracteres.")
        return

    cursor = db_conn.cursor
    cursor.execute('''
    INSERT INTO encomenda (nome, data_entrega, bloco, apartamento, porteiro)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, data_entrega, bloco, apartamento, porteiro))
    db_conn.conn.commit()
    
    messagebox.showinfo("Sucesso", "Encomenda inserida com sucesso.")

def inserir_informacoes_encomendas(db_conn, id_, nome_de_quem_retirou, cpf, data_retirada):
    cursor = db_conn.cursor

    cursor.execute('''
        UPDATE encomenda 
        SET nome_de_quem_retirou = ?, cpf = ?, data_retirada = ? 
        WHERE id = ?
    ''', (nome_de_quem_retirou, cpf, data_retirada, id_))

    db_conn.conn.commit()

def editar_morador(db_conn, nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    try:
        cursor = db_conn.cursor

        cursor.execute("""
            UPDATE moradores SET 
                nome = ?, 
                bloco = ?, 
                apartamento = ?, 
                placa_carro = ?, 
                telefone = ?, 
                data_nascimento = ?
            WHERE cpf = ?
        """, (nome, bloco, apartamento, placa_carro, telefone, data_nascimento, cpf))
        
        db_conn.conn.commit()
        affected_rows = cursor.rowcount
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    
def deletar_morador(db_conn, nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento):
    try:
        cursor = db_conn.cursor

        cursor.execute("""
            DELETE FROM moradores 
            WHERE nome = ? AND cpf = ? AND bloco = ? AND apartamento = ? AND placa_carro = ? AND telefone = ? AND data_nascimento = ?
        """, (nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento))
        
        db_conn.conn.commit()
        affected_rows = cursor.rowcount
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    
def pesquisar_encomenda(db_conn, nome, bloco, apartamento):
    cursor = db_conn.cursor
    cursor.execute("""
        SELECT nome, bloco, apartamento, porteiro, data_entrega, id
        FROM encomenda
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
    """, (nome, bloco, apartamento))
    dados_encomenda = cursor.fetchall()
    return dados_encomenda

def buscar_visitantes(db_conn, nome_morador):
    cursor = db_conn.cursor
    cursor.execute('''
    SELECT nome_visitante, horario1, horario2, data
    FROM visitantes
    WHERE nome_morador = ?
    ''', (nome_morador,))
    visitantes = cursor.fetchall()
    return visitantes

def pesquisar_encomenda_antigas(db_conn, nome, bloco, apartamento):
    cursor = db_conn.cursor
    cursor.execute("""
        SELECT * FROM encomendas_antigas
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
    """, (nome, bloco, apartamento))
    dados_encomenda_antigas = cursor.fetchall()
    return dados_encomenda_antigas

def inserir_informacoes_encomendas_antigas(db_conn, nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou):
    cursor = db_conn.cursor

    cursor.execute('''
    INSERT INTO encomendas_antigas (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou))
    db_conn.conn.commit()

def deletar_encomenda(db_conn, id_):
    cursor = db_conn.cursor

    cursor.execute('''
    DELETE FROM encomenda
    WHERE id = ?
    ''', (id_,))
    db_conn.conn.commit()


