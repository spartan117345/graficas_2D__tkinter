from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 460
ALTURA = 220
x_nave = 100
y_nave = 100
img_naves = "img/nave.png"
numero = 1

# -------------------
# funciones
# -------------------

# funcion para mover nave a la derecha
def mover_derecha(event=None):
    # borrar canvas
    c.delete("all")
    mover_asteroides()
    global x_nave
    global nave
    if x_nave<BASE:
        x_nave = x_nave + 10
    else:
        x_nave = 0
    #c.move(nave,x_nave, y_nave)
    nave = c.create_image(x_nave,y_nave,image=img_nave)
    

# funcion para mover nave a la izquierda
def mover_izquierda(event = None):
    # borrar canvas
    c.delete("all")
    mover_asteroides()
    global x_nave
    global nave
    if x_nave>0:
        x_nave = x_nave - 10
    else:
        x_nave = BASE - 64
    #c.move(nave,x_nave, y_nave)
    nave = c.create_image(x_nave,y_nave,image=img_nave)

# funcion para mover nave arriba
def mover_arriba(event = None):
# borrar canvas
    c.delete("all")
    mover_asteroides()
    global y_nave
    global nave
    if y_nave>0:
        y_nave = y_nave - 10
    else:
        y_nave = ALTURA - 44
    #c.move(nave,x_nave, y_nave)
    nave = c.create_image(x_nave,y_nave,image=img_nave)

# funcion para mover nave abajo
def mover_abajo(event = None):
# borrar canvas
    c.delete("all")
    mover_asteroides()
    global y_nave
    global nave
    if y_nave>0:
        y_nave = y_nave + 10
    else:
        y_nave = ALTURA + 44
    #c.move(nave,x_nave, y_nave)
    nave = c.create_image(x_nave,y_nave,image=img_nave)


# funcion para mover asteroides
def mover_asteroides():
    for i in range(20):
        x = random.randint(0, BASE-20)
        y = random.randint(0, ALTURA-20)
        tamanio_asteroide = random.randint(0,30)
        color = "#"
        for caracter in range(6):
            color = color + random.choice("0123456789ABCDEF")
        circulo = c.create_oval(x, y, x+tamanio_asteroide, y+tamanio_asteroide, fill=color)

def cambiar_nave():
    c.delete("all")
    mover_asteroides()
    global img_naves
    img_naves = "img/nave.png"

def cambiar_nave2():
    c.delete("all")
    mover_asteroides()    
    global img_naves
    img_naves = "img/nave2.png"

def cambiar_nave3():
    c.delete("all")
    mover_asteroides()    
    global img_naves
    img_naves = "img/nave3.png"

# -----------------
# ventana principal
# -----------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# frame de graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# ubicacion inicial nave
img_nave = PhotoImage(file=img_naves)
nave = c.create_image(x_nave,y_nave,image=img_nave)

# movientos teclado
ventana_principal.bind("<KeyPress-Right>",mover_derecha)

ventana_principal.bind("<KeyPress-Left>",mover_izquierda)

ventana_principal.bind("<KeyPress-Up>",mover_arriba)

ventana_principal.bind("<KeyPress-Down>",mover_abajo)



# frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10,y=260)

# botones movimiento
img_up = PhotoImage(file="img/up.png")
bt_up = Button(frame_controles, image=img_up, command=mover_arriba)
bt_up.place(x=208,y=19)

img_down = PhotoImage(file="img/down.png")
bt_down = Button(frame_controles, image=img_down, command=mover_abajo)
bt_down.place(x=208,y=147)

img_right = PhotoImage(file="img/right.png")
bt_right = Button(frame_controles, image=img_right, command=mover_derecha)
bt_right.place(x=272,y=83)

img_left = PhotoImage(file="img/left.png")
bt_left = Button(frame_controles, image=img_left, command=mover_izquierda)
bt_left.place(x=144,y=83)

img_nave = PhotoImage(file="img/nave.png")
bt_nave = Button(frame_controles, image=img_nave, command=cambiar_nave)
bt_nave.place(x=10,y=10)

img_nave2 = PhotoImage(file="img/nave2.png")
bt_nave2 = Button(frame_controles, image=img_nave2, command=cambiar_nave2)
bt_nave2.place(x=10,y=83)

img_nave3 = PhotoImage(file="img/nave3.png")
bt_nave3 = Button(frame_controles, image=img_nave3, command=cambiar_nave3)
bt_nave3.place(x=10,y=160)

# desplegar ventana
ventana_principal.mainloop()