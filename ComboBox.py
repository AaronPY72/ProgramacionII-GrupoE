import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title('Ejemplo ComboBox')
ventana.geometry('370x200')

etiqueta=tk.Label(ventana, text='Selecciona una especialidad:')
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#ComboBox
opciones=['Pediatria', 'Cardiologia', 'Neurologia', 'Dermatologia', 'Ginecologia']
combo=ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)#Seleccion primera opcion por defecto
combo.grid(row=0, column=1, padx=10, pady=10)

def mostrar():
    seleccionado=combo.get()
    tk.messagebox.showinfo("seleccion", f"Has elegido: {seleccionado}")
boton=tk.Button(ventana, text='Mostrar Seleccion', command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()