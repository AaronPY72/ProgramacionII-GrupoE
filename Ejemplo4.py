import tkinter as tk
from tkinter import messagebox

RegistroDoctores=tk.Tk()
RegistroDoctores.title("Registro de Doctores")
RegistroDoctores.geometry("400x500")
RegistroDoctores.configure(bg="#60ebe6")

nombreTituloLabel=tk.Label(RegistroDoctores, text="Registro de Doctores",bg="#60ebe6")
nombreTituloLabel.grid(row=0, column=1, padx=10, pady=10,sticky="w")
nombreLabel=tk.Label(RegistroDoctores, text="Nombre Completo: ",bg="#60ebe6")
nombreLabel.grid(row=1, column=0, padx=5, pady=10)
entryNombre=tk.Entry(RegistroDoctores)
entryNombre.grid(row=1, column=1, padx=5, pady=10)
#Direccion
direccionLabel=tk.Label(RegistroDoctores, text="Direccion: ",bg="#60ebe6")
direccionLabel.grid(row=2, column=0, padx=5, pady=10, sticky="w")
entryDireccion=tk.Entry(RegistroDoctores)
entryDireccion.grid(row=2, column=1, padx=5, pady=10)
#Telefono
telefonoLabel=tk.Label(RegistroDoctores, text="Telefono: ",bg="#60ebe6")
telefonoLabel.grid(row=3, column=0, padx=5, pady=10, sticky="w")
entryTelefono=tk.Entry(RegistroDoctores)
entryTelefono.grid(row=3, column=1, padx=5, pady=10)
#Especialidad
especialidadLabel=tk.Label(RegistroDoctores, text="Especialidad: ",bg="#60ebe6")
especialidadLabel.grid(row=4, column=0, padx=5, pady=10, sticky="w")
especialidad= tk.StringVar(value=None)
radioPediatra=tk.Radiobutton(RegistroDoctores, text="Pediatra", variable=especialidad, value="Pediatra", bg="#60ebe6")
radioPediatra.grid(row=4, column=1, padx=5, pady=5, sticky="w")
radiocardiologo=tk.Radiobutton(RegistroDoctores, text="Cardiologo", variable=especialidad, value="Cardiologo", bg="#60ebe6")
radiocardiologo.grid(row=5, column=1, padx=5, pady=5, sticky="w")
radioNeurologo=tk.Radiobutton(RegistroDoctores, text="Neurologo", variable=especialidad, value="Neurologo", bg="#60ebe6")
radioNeurologo.grid(row=6, column=1, padx=5, pady=5, sticky="w")
#Disponibilidad
disponibilidadLabel=tk.Label(RegistroDoctores, text="Disponibilidad: ",bg="#60ebe6")
disponibilidadLabel.grid(row=7, column=0, padx=5, pady=10, sticky="w")
manana=tk.BooleanVar()
tarde=tk.BooleanVar()
noche=tk.BooleanVar()
cbmanana=tk.Checkbutton(RegistroDoctores, text="Mañana", variable=manana, bg="#60ebe6")
cbmanana.grid(row=7, column=1, padx=5, pady=5, sticky="w")
cbtarde=tk.Checkbutton(RegistroDoctores, text="Tarde", variable=tarde, bg="#60ebe6")
cbtarde.grid(row=8, column=1, padx=5, pady=5, sticky="w")
cbnoche=tk.Checkbutton(RegistroDoctores, text="Noche", variable=noche, bg="#60ebe6")
cbnoche.grid(row=9, column=1, padx=5, pady=5, sticky="w")

def registrarDatos():
        disponibilidad = []
        if manana.get():
            disponibilidad.append("Mañana")
        elif tarde.get():
            disponibilidad.append("Tarde")
        elif noche.get():
            disponibilidad.append("Noche")
        if len(disponibilidad)> 0:
            disponibilidadTexto= ", ".join(disponibilidad)
        else:
            disponibilidadTexto = "Ninguna"
        info=(
            f"Nombre: {entryNombre.get()}\n"
            f"Direccion: {entryDireccion.get()}\n"
            f"Telefono: {entryTelefono.get()}\n"
            f"Especialidad: {especialidad.get()}\n"
            f"Disponibilidad: {disponibilidadTexto}")
        messagebox.showinfo("Registro del Doctor", info)
        RegistroDoctores.destroy()  # Cierra la ventana después de registrar los datos
btnRegistrar=tk.Button(RegistroDoctores, text="Datos Registrados", command=registrarDatos)
btnRegistrar.grid(row=10, column=1, columnspan=2, pady=15)

RegistroDoctores.mainloop()