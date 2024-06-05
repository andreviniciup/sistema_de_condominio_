
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\andre\Desktop\faculdade\sistema de condominio\interface\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("720x580")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 580,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    377.0,
    79.0,
    anchor="nw",
    text="retirada",
    fill="#8EBC4F",
    font=("BeVietnamPro SemiBold", 24 * -1)
)

canvas.create_text(
    34.0,
    80.0,
    anchor="nw",
    text="entrega",
    fill="#8EBC4F",
    font=("BeVietnamPro SemiBold", 24 * -1)
)

canvas.create_rectangle(
    334.0,
    69.0,
    335.0,
    509.0039367675781,
    fill="#B9B9B9",
    outline="")

canvas.create_text(
    386.0,
    126.0,
    anchor="nw",
    text="nome:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    384.0,
    296.0,
    anchor="nw",
    text="porteiro:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    510.0,
    213.0,
    anchor="nw",
    text="apartamento:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    386.0,
    213.0,
    anchor="nw",
    text="bloco:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    384.0,
    253.0,
    anchor="nw",
    text="data:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    384.0,
    167.0,
    anchor="nw",
    text="cpf:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    37.0,
    137.0,
    anchor="nw",
    text="nome:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    37.0,
    268.0,
    anchor="nw",
    text="porteiro:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    164.0,
    181.0,
    anchor="nw",
    text="apartamento:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    37.0,
    182.0,
    anchor="nw",
    text="bloco:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
)

canvas.create_text(
    37.0,
    226.0,
    anchor="nw",
    text="data:",
    fill="#000000",
    font=("BeVietnamPro Medium", 10 * -1)
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
    x=543.0,
    y=350.0,
    width=64.0,
    height=29.0
)

canvas.create_text(
    606.0,
    37.0,
    anchor="nw",
    text="encomendas",
    fill="#B9B9B9",
    font=("BeVietnamPro Light", 13 * -1)
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
    x=32.0,
    y=37.0,
    width=17.0,
    height=10.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    103.5,
    299.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=46.0,
    y=287.0,
    width=115.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    89.5,
    208.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=46.0,
    y=196.0,
    width=87.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    103.5,
    252.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=46.0,
    y=240.0,
    width=115.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    135.0,
    164.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=46.0,
    y=152.0,
    width=178.0,
    height=23.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    135.0,
    164.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=46.0,
    y=152.0,
    width=178.0,
    height=23.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    462.5,
    196.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=393.0,
    y=184.0,
    width=139.0,
    height=23.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    482.0,
    152.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=393.0,
    y=140.0,
    width=178.0,
    height=23.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    221.5,
    208.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=173.0,
    y=196.0,
    width=97.0,
    height=23.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    557.0,
    240.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=516.0,
    y=228.0,
    width=82.0,
    height=23.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    447.0,
    325.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=393.0,
    y=313.0,
    width=108.0,
    height=23.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    447.0,
    279.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=393.0,
    y=267.0,
    width=108.0,
    height=23.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    434.0,
    240.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=393.0,
    y=228.0,
    width=82.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
