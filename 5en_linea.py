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
        self.ficharoja = True
        self.fichaazul = False
        for i in range(6):
            tabla_fichas = []    
            for j in range(7):
                b = tkinter.Button(self.ventana,  command=partial(self.agre_ficha, i, j), height=5, width=5)
                b.grid(row=i, column=j)
                tabla_fichas.append(b)
            self.tabla_fichas.append(tabla_fichas)

        print(self.tabla_fichas)    
        self.ventana.mainloop()

    def agre_ficha(self, col, fila):
        if self.ficharoja:
            imagen = img
        else:
            imagen = img2
        self.tabla_ficha[col][fila].config
        self.ficharoja = not self.ficharoja
        self.tabla_fichas =[]
        x = True

c = Celinea()

