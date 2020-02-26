import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
def fboton1():
    res=0
    if respuesta1.get()=="1809":
        res+=20
    if respuesta2.get()=="1822":
        res+=20
    if respuesta3.get()==2:
        res+=20
    if respuesta4.get()==3:
        res+=20
    if respuesta5_1.get()==1 and respuesta5_5.get()==1:
        res+=20
    mBox.showinfo('Resultado',str(res))

def radio1():
    ttk.Label(ventana, text=respuesta2.get()).grid(column=0, row=20)

ventana=tk.Tk()
ventana.title("Sistema Escolar")

boton1=ttk.Button(ventana, text="Calificar", command=fboton1)
boton1.grid(column=0,row=10, padx=50, pady=10)

ttk.Label(ventana, text="1.-Año de nacimiento de charles Darwin:").grid(column=0,row=0, padx=5, pady=5)
respuesta1=tk.StringVar()
pedir_variable=ttk.Entry(ventana, width=20, textvariable=respuesta1)
pedir_variable.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(ventana, text="2.-Año de nacimiento de Gregor Mendel:").grid(column=0,row=1, padx=5, pady=5)
respuesta2=tk.StringVar()
pedir_variable=ttk.Entry(ventana, width=20, textvariable=respuesta2)
pedir_variable.grid(column=1, row=1, padx=5, pady=5)

respuesta3=tk.IntVar()
ttk.Label(ventana, text="3.-Marca el animal carnívoro:").grid(column=0,row=3, padx=5, pady=5)

radio1=tk.Radiobutton(ventana, text="Gallina", variable=respuesta3, value=1, command=radio1)
radio1.grid(column=0, row=4, sticky=tk.W)

radio2=tk.Radiobutton(ventana, text="León", variable=respuesta3, value=2, command=radio1)
radio2.grid(column=1, row=4, sticky=tk.W)

radio3=tk.Radiobutton(ventana, text="Jirafa", variable=respuesta3, value=3, command=radio1)
radio3.grid(column=2, row=4, sticky=tk.W)

respuesta4=tk.IntVar()
ttk.Label(ventana, text="4.-Marca el animal herbivoro").grid(column=0,row=5, padx=5, pady=5)

radio1=tk.Radiobutton(ventana, text="Oso Pardo", variable=respuesta4, value=1, command=radio1)
radio1.grid(column=0, row=6, sticky=tk.W)

radio2=tk.Radiobutton(ventana, text="Tiburon", variable=respuesta4, value=2, command=radio1)
radio2.grid(column=1, row=6, sticky=tk.W)

radio3=tk.Radiobutton(ventana, text="Jirafa", variable=respuesta4, value=3, command=radio1)
radio3.grid(column=2, row=6, sticky=tk.W)

respuesta5_1=tk.IntVar()
ttk.Label(ventana, text="5.-Selecciona 2 caracterisiticas del desierto del desierto").grid(column=0,row=7, padx=5, pady=5)
casilla1=tk.Checkbutton(ventana, text="Soleado", variable=respuesta5_1)
casilla1.deselect()
casilla1.grid(column=0, row=8, sticky=tk.W)
respuesta5_2=tk.IntVar()
casilla1=tk.Checkbutton(ventana, text="Tiene hielo", variable=respuesta5_2)
casilla1.deselect()
casilla1.grid(column=1, row=8, sticky=tk.W)
respuesta5_3=tk.IntVar()
casilla1=tk.Checkbutton(ventana, text="Lluvioso", variable=respuesta5_3)
casilla1.deselect()
casilla1.grid(column=2, row=8, sticky=tk.W)
respuesta5_4=tk.IntVar()
casilla1=tk.Checkbutton(ventana, text="Cuenta con muchos arboles", variable=respuesta5_4)
casilla1.deselect()
casilla1.grid(column=0, row=9, sticky=tk.W)
respuesta5_5=tk.IntVar()
casilla1=tk.Checkbutton(ventana, text="Arenoso", variable=respuesta5_5)
casilla1.deselect()
casilla1.grid(column=1, row=9, sticky=tk.W)

ventana.mainloop()