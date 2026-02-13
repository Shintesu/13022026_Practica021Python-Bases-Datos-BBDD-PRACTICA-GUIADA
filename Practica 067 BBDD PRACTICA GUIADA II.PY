# Curso Python. Práctica guiada II. Vídeo 60
# https://youtu.be/o8E869dmK3U?si=Db6i4A4tOJGC1Aix

from tkinter import*
from tkinter import messagebox
import sqlite3 

root = Tk()

# menú de la  parte superior---------------------------------------------------------------------------
barraMenu = Menu(root)
root.config( menu= barraMenu, width= 400,height= 300)

MenuBBDD = Menu(barraMenu, tearoff= 0)
MenuBBDD.add_command(label= "Conectar")
MenuBBDD.add_command(label= "Salir")

MenuLimpiar = Menu(barraMenu, tearoff= 0)
MenuLimpiar.add_command(label= "Limpiar campos",)

MenuCRUD = Menu(barraMenu, tearoff= 0)
MenuCRUD.add_command(label= "Crear",)
MenuCRUD.add_command(label= "Leer",)
MenuCRUD.add_command(label= "Actualizar",)
MenuCRUD.add_command(label= "Eliminar",)

MenuAyuda = Menu(barraMenu, tearoff= 0)
MenuAyuda.add_command(label= "Licencia",)
MenuAyuda.add_command(label= "Acerca de...",)

# representar la barra de menú en la ventana-----------------------------------------------------------
barraMenu.add_cascade(label= "BBDD", menu= MenuBBDD)
barraMenu.add_cascade(label= "Limpiar", menu= MenuLimpiar)
barraMenu.add_cascade(label= "CRUD", menu= MenuCRUD)
barraMenu.add_cascade(label= "Ayuda", menu= MenuAyuda)

# sub menús--------------------------------------------------------------------------------------------
# entrys
miFrame = Frame(root)
miFrame.pack()

cuadroID = Entry(miFrame)
cuadroID.grid(row= 0, column= 1, padx= 10, pady= 10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row= 1, column= 1, padx= 10, pady= 10)
cuadroNombre.config(fg= "red", justify= "right")

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row= 2, column= 1, padx= 10, pady= 10)
cuadroPassword.config(show= "*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row= 3, column= 1, padx= 10, pady= 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row= 4, column= 1, padx= 10, pady= 10)
# caja de comentarios
cuadroComentario = Text(miFrame, width= 20, height=8)               # Text
cuadroComentario.grid(row= 5, column= 1, padx= 10, pady= 10)
# barra de desplazamiento del texto
ScrollVert = Scrollbar(miFrame, command= cuadroComentario.yview)    # crear la barra
ScrollVert.grid(row= 5, column= 2, sticky= "nsew")

cuadroComentario.config(yscrollcommand= ScrollVert.set)             # para mostrar la barra


root.mainloop()