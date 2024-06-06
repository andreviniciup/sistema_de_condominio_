
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import ImageFont
import subprocess




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\andre\Desktop\faculdade\sistema de condominio\sistema_de_condominio_\interface\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    72.0,
    137.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    292.0,
    170.0,
    image=image_image_1
)

canvas.create_text(
    276.0,
    185.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    72.0,
    174.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    276.0,
    174.0,
    anchor="nw",
    text="data da entrega",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    72.0,
    127.0,
    anchor="nw",
    text="nome",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
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
    x=440.0,
    y=134.0,
    width=70.0,
    height=18.214290618896484
)

canvas.create_text(
    276.0,
    137.0,
    anchor="nw",
    text="robeval",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    276.0,
    127.0,
    anchor="nw",
    text="porteiro",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    451.0,
    187.0,
    anchor="nw",
    text="000234",
    fill="#545454",
    font=("BeVietnamPro Medium", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_2.place(
    x=42.0,
    y=35.0,
    width=30.0,
    height=15.0
)

canvas.create_text(
    790.0,
    23.0,
    anchor="nw",
    text="encomendas",
    fill="#B9B9B9",
    font=("BeVietnamPro Light", 19 * -1)
)

canvas.create_text(
    72.0,
    185.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    162.0,
    185.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    126.0,
    185.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    114.0,
    185.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    72.0,
    259.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    292.0,
    292.0,
    image=image_image_2
)

canvas.create_text(
    276.0,
    307.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    72.0,
    296.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    276.0,
    296.0,
    anchor="nw",
    text="data da entrega",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    72.0,
    249.0,
    anchor="nw",
    text="nome",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
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
    x=440.0,
    y=256.0,
    width=70.0,
    height=18.214290618896484
)

canvas.create_text(
    276.0,
    259.0,
    anchor="nw",
    text="robeval",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    276.0,
    249.0,
    anchor="nw",
    text="porteiro",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    451.0,
    309.0,
    anchor="nw",
    text="000234",
    fill="#545454",
    font=("BeVietnamPro Medium", 12 * -1)
)

canvas.create_text(
    72.0,
    307.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    162.0,
    307.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    126.0,
    307.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    114.0,
    307.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    72.0,
    381.0,
    anchor="nw",
    text="vinicius",
    fill="#000000",
    font=("BeVietnamPro MediumItalic", 14 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    292.0,
    414.0,
    image=image_image_3
)

canvas.create_text(
    276.0,
    429.0,
    anchor="nw",
    text="09/05/2024",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    72.0,
    418.0,
    anchor="nw",
    text="Unidade Vinculada",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    276.0,
    418.0,
    anchor="nw",
    text="data da entrega",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    72.0,
    371.0,
    anchor="nw",
    text="nome",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
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
    x=440.0,
    y=378.0,
    width=70.0,
    height=18.214290618896484
)

canvas.create_text(
    276.0,
    381.0,
    anchor="nw",
    text="robeval",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    276.0,
    371.0,
    anchor="nw",
    text="porteiro",
    fill="#545454",
    font=("BeVietnamPro Medium", 11 * -1)
)

canvas.create_text(
    451.0,
    431.0,
    anchor="nw",
    text="000234",
    fill="#545454",
    font=("BeVietnamPro Medium", 12 * -1)
)

canvas.create_text(
    72.0,
    429.0,
    anchor="nw",
    text="bloco ",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    162.0,
    429.0,
    anchor="nw",
    text="504",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    126.0,
    429.0,
    anchor="nw",
    text="apto",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
)

canvas.create_text(
    114.0,
    429.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("BeVietnamPro Medium", 14 * -1)
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
    x=237.0,
    y=70.0,
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
    x=57.0,
    y=70.0,
    width=180.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
