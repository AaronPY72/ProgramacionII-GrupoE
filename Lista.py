import tkinter as tk
from tkinter import messagebox

from pyparsing import col

ventana=tk.Tk()
ventana.title('Ejemplo ListBox')
ventana.geometry('270x250')


sintomaLabel=tk.Label(ventana, text='Sintomas:')
sintomaLabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')

lista=tk.Listbox(ventana, selectmode=tk.SINGLE)
lista.insert(1, 'Fiebre')
lista.insert(2, 'Tos')
lista.insert(3, 'Dolor de cabeza')
lista.insert(4, 'Dolor muscular')
lista.insert(5, 'Dificultad para respirar')
lista.grid(row=0, column=1, pady=10, sticky='we')

#Boton
def mostrar():
    seleccionado=lista.get(lista.curselection())
    tk.messagebox.showinfo("seleccion", f"has elegido: {seleccionado}")
boton=tk.Button(ventana, text='Mostrar Seleccion', command=mostrar)
boton.grid(row=1, column=0, padx=10, pady=10)

ventana.mainloop()