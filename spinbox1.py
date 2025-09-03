<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()

def mostrarEdad():
    messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
    
def mostrarGenero():
    messagebox.showinfo("Genero", f"El genero seleccionado es: {spinGenero.get()}")

labelEdad=tk.Label(ventana, text="Edad")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventana, from_=1, to=110)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana, text="Obtener valor", command=mostrarEdad)
boton.grid(row=1,column=0, padx=10, pady=10)
#Genero
labelGEnero=tk.Label(ventana, text="Genero")
labelGEnero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
#spinbox genero
spinGenero=tk.Spinbox(ventana, values=("Masculino", "Femenino"))
spinGenero.grid(row=2, column=1, padx=10,pady=10)
botonGenero=tk.Button(ventana,text="Obtener genero", command=mostrarGenero)
botonGenero.grid(row=3,column=0, padx=10, pady=10)
=======
import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()

def mostrarEdad():
    messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
    
def mostrarGenero():
    messagebox.showinfo("Genero", f"El genero seleccionado es: {spinGenero.get()}")

labelEdad=tk.Label(ventana, text="Edad")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventana, from_=1, to=110)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana, text="Obtener valor", command=mostrarEdad)
boton.grid(row=1,column=0, padx=10, pady=10)
#Genero
labelGEnero=tk.Label(ventana, text="Genero")
labelGEnero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
#spinbox genero
spinGenero=tk.Spinbox(ventana, values=("Masculino", "Femenino"))
spinGenero.grid(row=2, column=1, padx=10,pady=10)
botonGenero=tk.Button(ventana,text="Obtener genero", command=mostrarGenero)
botonGenero.grid(row=3,column=0, padx=10, pady=10)
>>>>>>> 49203089e246ead8b1fdad27602fe8832cbe0616
ventana.mainloop()