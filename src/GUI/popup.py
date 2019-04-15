import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Pop Up Message")

def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "Borar este fichero?")
    if (resultado == "yes"):
        print("Confirmado borrar fichero")
    else:
        print("cancelación de fichero")

# crea una ventana
button = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
button.pack()

raiz.mainloop()