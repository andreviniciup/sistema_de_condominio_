import os
import sys
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime

# Ajuste para definir o script_dir corretamente
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = Path(script_dir).parents[0]  # Isto assumindo que 'dashboard' está dentro de 'interface'

# Defina OUTPUT_PATH como a raiz do projeto
OUTPUT_PATH = project_root

# Caminho para assets
ASSETS_PATH = os.path.join(script_dir, "assets", "frame3")


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def cadastro_moradores():
    script_path = os.path.join(OUTPUT_PATH, "moradores", "cadastro_moradores_i.py")
    args = [sys.executable, script_path]
    subprocess.run(args)
    window.destroy()

    

def liberar_visitantes():
    script_path = os.path.join(OUTPUT_PATH, "visitantes", "liberar_visitantes_i.py")
    args = [sys.executable, script_path]
    subprocess.run(args)
    window.destroy()
    

def encomendas():
    script_path = os.path.join(OUTPUT_PATH, "encomendas", "encomendas_cadastro_i.py")
    args = [sys.executable, script_path]
    subprocess.run(args)
    window.destroy()

def obter_msg():
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite" 

window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")

msg = obter_msg()

canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_text( 651.0, 70.0, anchor="nw", text=msg, fill="#000000", font=("BeVietnamPro SemiBold", 53 * -1))
canvas.create_text( 807.0, 50.0, anchor="nw", text="dashboard", fill="#B9B9B9", font=("BeVietnamPro Light", 20 * -1))

#logo 
image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image( 137.0, 70.0, image=image_image_1)

#encomendas
button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command=encomendas, relief="flat")
button_3.place( x=400.0, y=450.0, width=167.0, height=167.0)

#cadastro de moradores
button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
button_4 = Button( image=button_image_4, borderwidth=0, highlightthickness=0, command=cadastro_moradores, relief="flat")
button_4.place( x=37.0, y=450.0, width=170.0, height=165.1884765625)

#liberar visitantes
button_image_5 = PhotoImage( file=relative_to_assets("button_5.png"))
button_5 = Button( image=button_image_5, borderwidth=0, highlightthickness=0, command=liberar_visitantes, relief="flat")
button_5.place( x=217.0, y=450.0, width=167.0, height=167.0)

window.resizable(False, False)
window.mainloop()
