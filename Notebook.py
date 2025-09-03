from pydoc import text
import tkinter as tk
from tkinter import messagebox, ttk

ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#contenedor notebook
pestanas=ttk.Notebook(ventana_principal)
#Crear frames
frame_pacientes=ttk.Frame(pestanas)
frame_doctores=ttk.Frame(pestanas)
#Agregar frames a las pestanas
pestanas.add(frame_pacientes, text="Pacientes")
pestanas.add(frame_doctores, text="Doctores")
#Mostrar las pestanas
pestanas.pack(expand=True, fill="both")
#Contenido frame pacientes
nombreLabel=ttk.Label(frame_pacientes, text="Nombre del Paciente:")
nombreLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
nombreEntry=ttk.Entry(frame_pacientes)
nombreEntry.grid(row=0, column=1, padx=10, pady=10)
#Fecha de Nacimiento
fechaLabel=ttk.Label(frame_pacientes, text="Fecha de Nacimiento (DD/MM/AAAA):")
fechaLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
fechaEntry=ttk.Entry(frame_pacientes)
fechaEntry.grid(row=1, column=1, padx=10, pady=10)
#Edad
edadP=ttk.Label(frame_pacientes, text="Edad:")
edadP.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadP=ttk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2, column=1, padx=10, pady=10)
#Genero
generoP=ttk.Label(frame_pacientes, text="Genero:")
generoP.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rbGenero=tk.StringVar()
rbGenero.set("Masculino")
rbMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=rbGenero, value="Masculino")
rbMasculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")
rbFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=rbGenero, value="Femenino")
rbFemenino.grid(row=4, column=1, padx=10, pady=5, sticky="w")
#Grupo Sanguineo
grupoLabel=ttk.Label(frame_pacientes, text="Grupo Sanguineo:")
grupoLabel.grid(row=5, column=0, padx=10, pady=10, sticky="w")
grupoEntry=ttk.Entry(frame_pacientes)
grupoEntry.grid(row=5, column=1, padx=10, pady=10)
#Tipo de Seguro
seguroLabel=ttk.Label(frame_pacientes, text="Tipo de Seguro:")
seguroLabel.grid(row=6, column=0, padx=10, pady=10, sticky="w")
tipo_seguro=tk.StringVar()
seguroCombo=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], state="readonly",textvariable=tipo_seguro)
seguroCombo.grid(row=6, column=1, padx=10, pady=10)
#Centro Medico
centroLabel=ttk.Label(frame_pacientes, text="Centro Medico:")
centroLabel.grid(row=7, column=0, padx=10, pady=10, sticky="w")
centro_medico=tk.StringVar()
centroCombo=ttk.Combobox(frame_pacientes, values=["Clinica Norte", "Hospital General", "Centro del Sur"], textvariable=centro_medico)
centroCombo.grid(row=7, column=1, padx=10, pady=10)
ventana_principal.mainloop()