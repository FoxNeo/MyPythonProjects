import tkinter

raiz = tkinter.Tk()
raiz.title("Some title here")

# component
texto = "Hello GUI Python"
tag = tkinter.Label(raiz, text=texto)
tag.config(fg="black", bg="lightyellow", font=("Cortana", 30))
tag.pack()

raiz.mainloop()