
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame8")


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


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
canvas.create_text(
    724.0,
    25.0,
    anchor="nw",
    text="Liberar visitantes",
    fill="#B9B9B9",
    font=("BeVietnamPro Light", 19 * -1)
)

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
    x=69.0,
    y=34.0,
    width=30.0,
    height=15.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    219.0,
    349.0,
    image=image_image_1
)

canvas.create_text(
    85.0,
    337.0,
    anchor="nw",
    text="horário",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    309.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    240.0,
    337.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    85.0,
    305.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

canvas.create_text(
    85.0,
    296.0,
    anchor="nw",
    text="nome",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    239.0,
    297.0,
    anchor="nw",
    text="data",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    349.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    330.0,
    349.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    294.0,
    349.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    282.0,
    349.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    85.0,
    349.0,
    anchor="nw",
    text="09h00 ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    134.0,
    349.0,
    anchor="nw",
    text="ás",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    151.0,
    349.0,
    anchor="nw",
    text=" 21h30",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
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
    x=182.0,
    y=380.0,
    width=69.0,
    height=21.327281951904297
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    219.0,
    502.0,
    image=image_image_2
)

canvas.create_text(
    85.0,
    490.0,
    anchor="nw",
    text="horário",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    462.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    240.0,
    490.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    85.0,
    458.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

canvas.create_text(
    85.0,
    449.0,
    anchor="nw",
    text="nome",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    239.0,
    450.0,
    anchor="nw",
    text="data",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    502.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    330.0,
    502.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    294.0,
    502.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    282.0,
    502.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    85.0,
    502.0,
    anchor="nw",
    text="09h00 ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    134.0,
    502.0,
    anchor="nw",
    text="ás",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    151.0,
    502.0,
    anchor="nw",
    text=" 21h30",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
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
    x=182.0,
    y=533.0,
    width=69.0,
    height=21.327281951904297
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    219.0,
    196.0,
    image=image_image_3
)

canvas.create_text(
    85.0,
    184.0,
    anchor="nw",
    text="horário",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    156.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    240.0,
    184.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    85.0,
    152.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

canvas.create_text(
    85.0,
    143.0,
    anchor="nw",
    text="nome",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    239.0,
    144.0,
    anchor="nw",
    text="data",
    fill="#7C7C7C",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    240.0,
    196.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    330.0,
    196.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    294.0,
    196.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    282.0,
    196.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    85.0,
    196.0,
    anchor="nw",
    text="09h00 ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    134.0,
    196.0,
    anchor="nw",
    text="ás",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    151.0,
    196.0,
    anchor="nw",
    text=" 21h30",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=182.0,
    y=227.0,
    width=69.0,
    height=21.327281951904297
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=251.0,
    y=74.0,
    width=180.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=71.0,
    y=74.0,
    width=180.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
