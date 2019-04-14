import tkinter

raiz = tkinter.Tk()
raiz.title("Button with Python")

# component
# define accion function
def accion():
    print("Hola usuario")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="red")
boton.pack()

raiz.mainloop()