import tkinter
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
from functools import partial

class Celinea:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("5 En Linea")
        img = Image.open("ficharoja.png")
        img = img.resize((50, 60), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        img2 = Image.open("fazul.jpg")
        img2 = img2.resize((50, 60), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        self.tabla_fichas = []
        self.rojo = True
        self.azul = False
        for i in range(6):
            tabla_fichas = []    
            for j in range(7):
                b = tkinter.Button(self.ventana, command=partial(self.agre_ficha, i, j), height=5, width=5)
                b.grid(row=i, column=j)
                tabla_fichas.append(b)
            self.tabla_fichas.append(tabla_fichas)

        print(self.tabla_fichas)    
        self.ventana.mainloop()

    def agre_ficha(self, col, fila):
        if self.rojo:
            imagen = self.img
            texto = "rojo"
            self.turno = "rojo"
        else:
            imagen = self.img2
            texto = "azul"
            self.turno = "azul"
        self.tabla_fichas[col][fila].config(text=texto, image=imagen, height=63, width=65)
        self.chequearGanador(self.tabla_fichas)
        self.rojo = not self.rojo
        x = True
        
    def chequearGanador(self, tabla_botones):
        if self.tabla_fichas[0][0].cget("text") and self.tabla_fichas[0][0].cget("text") == self.tabla_fichas[0][1].cget("text") and self.tabla_fichas[0][1].cget("text") == self.tabla_fichas[0][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[1][0].cget("text") and self.tabla_fichas[1][0].cget("text") == self.tabla_fichas[1][1].cget("text") and self.tabla_fichas[1][1].cget("text") == self.tabla_fichas[1][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[2][0].cget("text") and self.tabla_fichas[2][0].cget("text") == self.tabla_fichas[2][1].cget("text") and self.tabla_fichas[2][1].cget("text") == self.tabla_fichas[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[0][0].cget("text") and self.tabla_fichas[0][0].cget("text") == self.tabla_fichas[1][0].cget("text") and self.tabla_fichas[1][0].cget("text") == self.tabla_fichas[2][0].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[0][1].cget("text") and self.tabla_fichas[0][1].cget("text") == self.tabla_fichas[1][1].cget("text") and self.tabla_fichas[1][1].cget("text") == self.tabla_fichas[2][1].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[0][2].cget("text") and self.tabla_fichas[0][2].cget("text") == self.tabla_fichas[1][2].cget("text") and self.tabla_fichas[1][2].cget("text") == self.tabla_fichas[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[0][0].cget("text") and self.tabla_fichas[0][0].cget("text") == self.tabla_fichas[1][1].cget("text") and self.tabla_fichas[1][1].cget("text") == self.tabla_fichas[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_fichas[0][2].cget("text") and self.tabla_fichas[0][2].cget("text") == self.tabla_fichas[1][1].cget("text") and self.tabla_fichas[1][1].cget("text") == self.tabla_fichas[2][0].cget("text"):
            print("gano " + self.turno)

c = Celinea()
