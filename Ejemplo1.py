import tkinter as tk
ventana=tk.Tk()#Inicio de la ventana
ventana.title('Registro de Pacientes')
ventana.geometry('600x800')
ventana.configure(bg="#334d6e")#/ventana.configure(bg="#000000") Se puede usar codigo de colores sexagecimal
texto = tk.Label(ventana, text="bienvenidos a la aplicacion de gestion de pacientes")
texto.grid(row=0, column=0, padx=5, pady=5)
boton=tk.Button(ventana, text="Salir", command=ventana.destroy)
boton.grid(row=1, column=0, padx=0, pady=0)
ventana.mainloop()#fin de la ventana