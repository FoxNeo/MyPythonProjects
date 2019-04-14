import tkinter

raiz = tkinter.Tk()
raiz.title("My Python programm")

# component

input = tkinter.Entry(raiz)
input.config(justify="center") # show="*" for passwords
input.pack()


raiz.mainloop()