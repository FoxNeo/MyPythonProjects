import tkinter
from tkinter import filedialog
raiz = tkinter.Tk()
raiz.title("file dialog")

# component

def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)

boton = tkinter.Button(raiz, text="Pulsar para empezar", command=abrirfichero)
boton.pack()


raiz.mainloop()