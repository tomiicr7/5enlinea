import tkinter
from tkinter import PhotoImage
from PIL import Image,ImageTk
from functools import partial

ventana = tkinter.Tk()
ventana.title("5 En Linea")

img = Image.open("ficharoja.png")
img = resize((50, 60), Image.resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

img2 = Image.open("fazul.jpg")
img2 = resize((50, 60), Image.resampling.LANCZOS)
img2 = ImageTk.PhotoImage(img)


def agre_ficha(col, fila):
    global x
    if x:
        imagen = img
    else:
        imagen = img2
        
tabla_fichas =[]
x = true

for i in range(7):
    tabla_fichas = []    
    for j in range(4):
        b = tkinter.Button(ventana,  command=partial(agre_ficha, i, j), height=4, width=5)
        b.grid(row=i, column=j)
        fila_botones.append(b)
    tabla_botones.append(tabla_fichas)
    
ventana.mainloop


