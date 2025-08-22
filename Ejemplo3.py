import tkinter as tk
from tkinter import messagebox

def NuevoPaciente():
    ventNuevoPaciente = tk.Toplevel(ventanaPrincipal)#toplevel es para crear una ventana secundaria
    ventNuevoPaciente.title("Registro de Paciente")
    ventNuevoPaciente.geometry("400x400")
    ventNuevoPaciente.configure(bg="#94f1d7")
    nombreLabel=tk.Label(ventNuevoPaciente, text="Nombre:", bg="#94f1d7")
    nombreLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")#n=norte, s=sur, e=este, w=oeste
    entryNombre=tk.Entry(ventNuevoPaciente)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    direccionLabel=tk.Label(ventNuevoPaciente,text="Direccion:", bg="#94f1d7")
    direccionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entryDireccion=tk.Entry(ventNuevoPaciente)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    telefonoLabel=tk.Label(ventNuevoPaciente,text="Telefono:", bg="#94f1d7")
    telefonoLabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entryTelefono=tk.Entry(ventNuevoPaciente)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    #Genero
    sexoLabel=tk.Label(ventNuevoPaciente, text="Sexo:", bg="#94f1d7")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo = tk.StringVar(value="Masculino")#stringVar es para manejar variables de texto y asignar un valor por defecto
    radioMasculino = tk.Radiobutton(ventNuevoPaciente, text="Masculino", variable=sexo, value="Masculino", bg="#94f1d7")
    radioMasculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    radioFemenino = tk.Radiobutton(ventNuevoPaciente, text="Femenino", variable=sexo, value="Femenino", bg="#94f1d7")
    radioFemenino.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    #Enfermedades
    enfermedadesLabel = tk.Label(ventNuevoPaciente, text="Enfermedades:", bg="#94f1d7")
    enfermedadesLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes=tk.BooleanVar()#BooleanVar es para manejar variables booleanas (verdadero o falso)
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar() 
    cbdiabetes= tk.Checkbutton(ventNuevoPaciente, text="Diabetes", variable=diabetes, bg="#94f1d7")
    cbdiabetes.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    cbhipertension = tk.Checkbutton(ventNuevoPaciente, text="Hipertension", variable=hipertension, bg="#94f1d7")
    cbhipertension.grid(row=6, column=1, padx=10, pady=5, sticky="w")
    cbasma = tk.Checkbutton(ventNuevoPaciente, text="Asma", variable=asma, bg="#94f1d7")
    cbasma.grid(row=7, column=1, padx=10, pady=5, sticky="w")
    
    def registrarDatos():
        enfermedades = []
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)> 0:
            enfermedadesTexto= ", ".join(enfermedades)
        else:
            enfermedadesTexto = "Ninguna"
        info=(
            f"Nombre: {entryNombre.get()}\n"
            f"Direccion: {entryDireccion.get()}\n"
            f"Telefono: {entryTelefono.get()}\n"
            f"Sexo: {sexo.get()}\n"
            f"Enfermedades: {enfermedadesTexto}")
        messagebox.showinfo("Datos del Paciente", info)
        ventNuevoPaciente.destroy()  # Cierra la ventana después de registrar los datos
    btnRegistrar=tk.Button(ventNuevoPaciente, text="Datos Registrados", command=registrarDatos)
    btnRegistrar.grid(row=8, column=1, columnspan=2, pady=15)
    

def BuscarPaciente():
    messagebox.showinfo("Buscar Paciente", "espacio para buscar paciente")
    
def EliminarPaciente():
    messagebox.showinfo("Eliminar Paciente", "espacio para eliminar paciente")
    
def NuevoDoctor():
    messagebox.showinfo("Nuevo Doctor", "espacio para crear nuevo doctor")

def BuscarDoctor():
    messagebox.showinfo("Buscar Doctor", "espacio para buscar doctor")

def EliminarDoctor():
    messagebox.showinfo("Eliminar Doctor", "espacio para eliminar doctor")

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x600")
ventanaPrincipal.configure(bg="#60ebe6")
#barra de menú
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#Menu pacientes
menuPacientes=tk.Menu(barraMenu, tearoff=0)#sirve para quitar las lineas punteadas (teraoff)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=NuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente", command=BuscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente", command=EliminarPaciente)
menuPacientes.add_separator() #separador
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu Doctores 
menuDoctores=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=NuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor", command=BuscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor", command=EliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu Ayuda
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Version1.0-Sistema Biomedicina"))
menuAyuda.add_separator() #separador
menuAyuda.add_command(label="Salir", command=ventanaPrincipal.quit) #salir del programa
ventanaPrincipal.mainloop()
