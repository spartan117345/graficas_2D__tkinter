from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 460
ALTURA = 220

# ----------------
# ventana prncipal
# ----------------
ventana_principal = Tk()
ventana_principal.title("graficas 2d")
ventana_principal.resizable(FALSE, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg = "white")

# --------------------
# frame de graficacion
# --------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# -------------------
# lienso de graficacion
# -------------------
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# -------------------------------------
# figuras de color y/o tamaño aleatorio
# -------------------------------------

for i in range(100):
    x = random.randint(0,BASE - 20)
    y = random.randint(0,ALTURA-20)

    color = "#"

    for caracter in range(6):
        color = color + random.choice("0123456789ABCDEF")

    circulo = c.create_oval(x, y, x+20, y+20, fill = color)





# --------------------
# frame de controles
# --------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg = "black", width=480, height=230)
frame_controles.place(x=10,y=260)

# ---------------------------
# desplegar ventana principal
# ---------------------------
ventana_principal.mainloop()