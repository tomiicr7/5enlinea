import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from functools import partial

class Celinea:
    def __init__(self):
        self.filaocupada = [5, 5, 5, 5, 5, 5, 5]
        
        
        self.ventana = tkinter.Tk()
        self.ventana.title("5 En Linea")
        img = Image.open("circuloR.jpg")
        img = img.resize((50, 60), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        img2 = Image.open("circuloA.jpg")
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
        self.tabla_fichas[self.filaocupada[fila]][fila].config(text=texto, image=imagen, height=0, width=0)
        self.filaocupada[fila] -= 1
        self.rojo = not self.rojo
        x = True
c = Celinea()
