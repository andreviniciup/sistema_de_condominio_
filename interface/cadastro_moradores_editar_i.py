import sys
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage,messagebox

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(Path(__file__).resolve().parent.parent))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame5")
from back.banco_de_dados.funcoesdb import pesquisar_morador

dados = sys.argv[1:]

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


def preencher_campos_com_dados_do_banco(nome, bloco, apartamento):
    dados_morador = pesquisar_morador(nome=nome, bloco=bloco, apartamento=apartamento)
    if dados_morador:
        entry_1.insert(0, dados_morador[0])
        entry_2.insert(0, dados_morador[1])
        entry_7.insert(0, dados_morador[2])
        entry_6.insert(0, dados_morador[3])
        entry_3.insert(0, dados_morador[4])
        entry_5.insert(0, dados_morador[5])
        entry_4.insert(0, dados_morador[6])
    else:
        messagebox.showinfo("Resultado da Pesquisa", "Nenhum morador encontrado.")


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 680,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=56.0,
    y=525.0,
    width=90.0,
    height=40.78125
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=169.0,
    y=526.0,
    width=90.0,
    height=37.82606506347656
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=28.0,
    y=33.0,
    width=30.0,
    height=15.0
)

canvas.create_text(
    683.0,
    24.0,
    anchor="nw",
    text="cadastro de moradores",
    fill="#B9B9B9",
    font=("BeVietnamPro Light", 19 * -1)
)

canvas.create_text(
    58.0,
    78.0,
    anchor="nw",
    text="Cadastro",
    fill="#8EBC4F",
    font=("BeVietnamPro Bold", 45 * -1)
)

canvas.create_text(
    58.0,
    155.0,
    anchor="nw",
    text="nome:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    214.0,
    192.66262912750244,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=67.0,
    y=177.0,
    width=294.0,
    height=29.325258255004883
)

canvas.create_text(
    58.0,
    214.0,
    anchor="nw",
    text="cpf:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    166.0,
    251.66262912750244,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=67.0,
    y=236.0,
    width=198.0,
    height=29.325258255004883
)

canvas.create_text(
    56.0,
    391.0,
    anchor="nw",
    text="bloco:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    133.5,
    428.66262912750244,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=65.0,
    y=413.0,
    width=137.0,
    height=29.325258255004883
)

canvas.create_text(
    56.0,
    450.0,
    anchor="nw",
    text="placa do carro:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    133.5,
    487.66262912750244,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=65.0,
    y=472.0,
    width=137.0,
    height=29.325258255004883
)

canvas.create_text(
    231.0,
    391.0,
    anchor="nw",
    text="apartamento:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    308.5,
    428.66262912750244,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=240.0,
    y=413.0,
    width=137.0,
    height=29.325258255004883
)

canvas.create_text(
    58.0,
    332.0,
    anchor="nw",
    text="telefone:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    179.0,
    369.66262912750244,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=65.0,
    y=354.0,
    width=228.0,
    height=29.325258255004883
)

canvas.create_text(
    58.0,
    273.0,
    anchor="nw",
    text="data de nascimento:",
    fill="#000000",
    font=("BeVietnamPro SemiBold", 17 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    164.0,
    310.66262912750244,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=65.0,
    y=295.0,
    width=198.0,
    height=29.325258255004883
)



window.resizable(False, False)
window.mainloop()
