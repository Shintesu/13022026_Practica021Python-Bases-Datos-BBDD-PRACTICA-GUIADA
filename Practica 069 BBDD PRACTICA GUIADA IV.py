# Curso Python. Práctica guiada IV. Vídeo 62
# https://www.youtube.com/watch?v=5XPLCDp7nDk

from tkinter import*
from tkinter import messagebox
import sqlite3 

root = Tk()


# funciones del menú------------------------------------------------------------------------------------
# crear base de datos
def conexionBBDD():
    miConexion = sqlite3.connect("BaseDatosGuiada01")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR (30),
                PASSWORD VARCHAR (25),
                APELLIDO VARCHAR (30),
                DIRECCION VARCHAR (40),
                COMENTARIOS VARCHAR (150)
            )
        ''')
        messagebox.showinfo("BBDD","La base de datos ha sido creada exitoxamente")
    except:
        messagebox.showwarning("!ATENCIÓN¡", "Ya existe una base de datos")

# botón de salir
def salirAplicacion():
    respuesta = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if respuesta == "yes":
        root.destroy()



# menú de la  parte superior---------------------------------------------------------------------------
barraMenu = Menu(root)
root.config( menu= barraMenu, width= 400,height= 300)

MenuBBDD = Menu(barraMenu, tearoff= 0)
MenuBBDD.add_command(label= "Conectar", command= conexionBBDD)
MenuBBDD.add_command(label= "Salir", command= salirAplicacion)

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


# labels
IdLabel = Label(miFrame, text= "ID:")
IdLabel.grid(row= 0, column=0, sticky= "e", padx= 10, pady= 10)

NombreLabel = Label(miFrame, text= "Nombre:")
NombreLabel.grid(row= 1, column=0, sticky= "e", padx= 10, pady= 10)

PasswordLabel = Label(miFrame, text= "Password:")
PasswordLabel.grid(row= 2, column=0, sticky= "e", padx= 10, pady= 10)

ApellidoLabel = Label(miFrame, text= "Apellido:")
ApellidoLabel.grid(row= 3, column=0, sticky= "e", padx= 10, pady= 10)

DireccionLabel = Label(miFrame, text= "Direccion:")
DireccionLabel.grid(row= 4, column=0, sticky= "e", padx= 10, pady= 10)

ComentarioLabel = Label(miFrame, text= "Comentarios:")
ComentarioLabel.grid(row= 5, column=0, sticky= "e", padx= 10, pady= 10)


# botones inferiores--------------------------------------------------
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text= "Create",)
botonCrear.grid(row= 0, column= 0, sticky= "e", padx= 10, pady= 10)

botonLeer = Button(miFrame2, text= "Read",)
botonLeer.grid(row= 0, column= 1, sticky= "e", padx= 10, pady= 10)

botonActualizar = Button(miFrame2, text= "Update",)
botonActualizar.grid(row= 0, column= 2, sticky= "e", padx= 10, pady= 10)

botonEliminar = Button(miFrame2, text= "Delete",)
botonEliminar.grid(row= 0, column= 3, sticky= "e", padx= 10, pady= 10)


# loop infinito---------------------------------------------------------------------------------------
root.mainloop()