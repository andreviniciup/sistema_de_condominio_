import tkinter as tk
import sqlite3

def obter_informacoes_do_banco_de_dados():
    # Simule a consulta à base de dados aqui
    # Retorne os dados desejados (por exemplo, nome e data)
    return "Vinicius", "09/05/2024"

def atualizar_retangulo():
    nome, data = obter_informacoes_do_banco_de_dados()
    label_nome.config(text=f"Nome: {nome}")
    label_data.config(text=f"Data: {data}")

# Configuração da janela
root = tk.Tk()
root.title("Exemplo de Interface Gráfica")

# Crie os widgets (labels, botões, etc.)
label_nome = tk.Label(root, text="Nome:")
label_data = tk.Label(root, text="Data:")
botao_liberar = tk.Button(root, text="Liberar", command=atualizar_retangulo)

# Posicione os widgets na interface
label_nome.pack()
label_data.pack()
botao_liberar.pack()

root.mainloop()
