from tkinter import *

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
c.config(bg="blue")
c.place(x=10,y=10)

cuerpo = c.create_rectangle(BASE/2-60, ALTURA/2-30,BASE/2+60,ALTURA/2+30,fill="grey60")
rueda1 = c.create_oval(BASE/2-60,ALTURA/2+15,BASE/2-20,ALTURA/2+50,fill="grey")
rueda2 = c.create_oval(BASE/2-20,ALTURA/2+15,BASE/2+20,ALTURA/2+50,fill="grey")
rueda3 = c.create_oval(BASE/2+20,ALTURA/2+15,BASE/2+60,ALTURA/2+50,fill="grey")
linea1 = c.create_rectangle(BASE/2-40,ALTURA/2+27,BASE/2-5,ALTURA/2+37,fill="black")
linea2 = c.create_rectangle(BASE/2+5,ALTURA/2+27,BASE/2+40,ALTURA/2+37,fill="black")
cuerpo2 = c.create_rectangle(BASE/2-70,ALTURA/2-20,BASE/2-60,ALTURA/2+20,fill="grey64")
cuerpo3 = c.create_rectangle(BASE/2-80, ALTURA/2-30,BASE/2-70,ALTURA/2+30,fill="grey64")
circulodelantero = c.create_arc(BASE/2-90,ALTURA/2-20,BASE/2-70,ALTURA/2+20, start=90,extent=180,fill="grey64")
chimenea1= c.create_rectangle(BASE/2-55,ALTURA/2-50,BASE/2-40,ALTURA/2-30,fill="grey64")
chimenea2 = c.create_rectangle(BASE/2-60,ALTURA/2-60,BASE/2-35,ALTURA/2-50,fill="grey64")
asiento1 = c.create_rectangle(BASE/2,ALTURA/2-30,BASE/2+60,ALTURA/2-60,fill="grey64")
ventana = c.create_rectangle(BASE/2+5,ALTURA/2-35,BASE/2+55,ALTURA/2-55,fill="white")
techo1 = c.create_rectangle(BASE/2-10,ALTURA/2-70,BASE/2+70,ALTURA/2-60,fill="GREY64")
techo2 = c.create_rectangle(BASE/2,ALTURA/2-70,BASE/2+60,ALTURA/2-80,fill="grey64")
nesticor = c.create_oval(BASE/2+20,ALTURA/2-35,BASE/2+45,ALTURA/2-55,fill="yellow")
boca = c.create_oval(BASE/2+30,ALTURA/2-41,BASE/2+35,ALTURA/2-36,fill="red")
ojo1 = c.create_oval(BASE/2+24,ALTURA/2-50,BASE/2+29,ALTURA/2-45,fill="black")
ojo2 = c.create_oval(BASE/2+34,ALTURA/2-50,BASE/2+39,ALTURA/2-45,fill="black")
texto = c.create_text(BASE/2-20, ALTURA/2-10, anchor="center", text = "julian", font = ("Arial", 20, "bold"), fill="blue", activefill="yellow")


ventana_principal.mainloop()