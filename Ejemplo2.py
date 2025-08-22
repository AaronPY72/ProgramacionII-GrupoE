import tkinter as tk 
from tkinter import messagebox

def enviarDatos():
    nombre1=nombreEntry.get()
    edad1=edadEntry.get()
    messagebox.showinfo("Datos del paciente", f"Nombre: {nombre1}\n Edad:{edad1}")

ventana=tk.Tk()
ventana.title("Registtro de Pacientes")
ventana.geometry("600x600")
ventana.configure(bg="#81b7bb")
#Pedir Nombre
nombreLabel=tk.Label(ventana, text="Nombre: ")
nombreLabel.grid(row=0, column=0, padx=5, pady=5)
nombreEntry=tk.Entry(ventana)
nombreEntry.grid(row=0, column=1,padx=5, pady=5)
#Pedir Edad
edadLabel=tk.Label(ventana, text="Edad: ")
edadLabel.grid(row=1, column=0, padx=5, pady=5)
edadEntry=tk.Entry(ventana)
edadEntry.grid(row=1, column=1, padx=5, pady=5)
#Boton enviar
botonEnviar=tk.Button(ventana, text="Enviar Datos", command=enviarDatos)
botonEnviar.grid(row=3, column=0, padx=5,pady=5)
ventana.mainloop()