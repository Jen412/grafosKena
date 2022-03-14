from tkinter import *

raiz = Tk()



frame = Frame(raiz, width=1000, height=600)
frame.pack()

def agregar():
    agregarG = Frame(raiz, width=1000, height=600)
    agregarG.pack()
    frame.pack_forget()
    lbNumeroN = Label(agregarG, text="Numero de Nodos")
    lbNumeroN.grid(column=0, row=0, padx=10, pady=10)
    enNumeroN = Entry(agregarG)
    enNumeroN.grid(column=1, row=0, padx=10, pady=10)



btnCrearG= Button(frame, text="Crear Grafo", command=agregar)
btnCrearG.grid(column=0 ,row=0, padx=15, pady=15)
btnVisualG =Button(frame, text="Visualizar Grafo")
btnVisualG.grid(column=1 ,row=0, padx=15, pady=15)
btnEliN= Button(frame, text="Eliminar Nodo")
btnEliN.grid(column=2 ,row=0, padx=15, pady=15)
btnModG= Button(frame, text="Modificar Grafo")
btnModG.grid(column=3 ,row=0, padx=15, pady=15)
btnEliG= Button(frame, text="Eliminar Grafo")
btnEliG.grid(column=4 ,row=0, padx=15, pady=15)







raiz.mainloop()