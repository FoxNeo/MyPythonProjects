import tkinter

raiz = tkinter.Tk()
raiz.title("Title")

#component

def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check está activado")
    else:
        print("El check está desactivado")

check1 = tkinter.IntVar()

button1 = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
button1.pack()

raiz.mainloop()