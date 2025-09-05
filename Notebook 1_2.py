from datetime import date, datetime
from pydoc import doc
import tkinter as tk
from tkinter import messagebox, ttk


def enmascarar_fecha(texto):
    limpio="".join(filter(str.isdigit, texto))
    formato_final=""
    
    if len(limpio)>8:
        limpio=limpio[:8]
    elif len(limpio)>4:
        formato_final=f"{limpio[:2]}/{limpio[2:4]}/{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}/{limpio[2:]}"
    else:
        formato_final=limpio
    
    if fechaEntry.get()!=formato_final:
        fechaEntry.delete(0, tk.END)
        fechaEntry.insert(0, formato_final)
    if len(fechaEntry.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaEntry.get(), "%d/%m/%Y").date()
        edad=fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
paciente_data=[]
doctores_data=[]
def registrarPaciente():
    paciente={
        "Nombre": nombreEntry.get(),
        "FechaN": fechaEntry.get(),
        "Edad": edadVar.get(),
        "Genero": rbGenero.get(),
        "GrupoS": grupoEntry.get(),
        "TipoS": tipo_seguro.get(),
        "CentroM": centro_medico.get()
    }
    paciente_data.append(paciente)
    cargar_treeview()
    
def cargar_treeview():
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end", iid=str(i),
            values=(
                item["Nombre"],
                item["FechaN"],
                item["Edad"],
                item["Genero"],
                item["GrupoS"],
                item["TipoS"],
                item["CentroM"]
            )
        )
def registrarDoctores():
    doctor={
        "NombreD": nombreEntryD.get(),
        "Especialidad": especialidad.get(),
        "EdadD": edadSpin.get(),
        "Telefono": telEntry.get()
    }
    doctores_data.append(doctor)
    cargar_treeviewD()
    
def cargar_treeviewD():
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    for i, item in enumerate(doctores_data):
        treeviewD.insert(
            "","end", iid=str(i),
            values=(
                item["NombreD"],
                item["Especialidad"],
                item["EdadD"],
                item["Telefono"]
            )
        )
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("700x650")
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
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaEntry=ttk.Entry(frame_pacientes,validate="key", validatecommand=(validacion_fecha, "%P"))
fechaEntry.grid(row=1, column=1, padx=10, pady=10)
#Edad
edadP=ttk.Label(frame_pacientes, text="Edad:")
edadP.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar=tk.StringVar()
edadP=ttk.Entry(frame_pacientes,textvariable=edadVar,state="readonly")
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
#Frame para los botones
btn_frame=ttk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")
#boton registrar
btn_registrar=ttk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=9,column=0,padx=5)
#boton Eliminar
btn_eliminar=ttk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=9,column=1,padx=5)
#Crear TreeView 
treeview = ttk.Treeview(frame_pacientes,columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"),show="headings")
#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Genero")
treeview.heading("GrupoS",text="Grupo Sanguineo")
treeview.heading("TipoS",text="Tipo Seguro")
treeview.heading("CentroM",text="Centro Medico")
#Definir anchos
treeview.column("Nombre",width=130)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=80,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
#Ubicar el TreeView
treeview.grid(row=10,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar
scorll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scorll_y.set)
scorll_y.grid(row=10,column=2,sticky="ns")

#Doctores
nombreLabel=ttk.Label(frame_doctores, text="Nombre:")
nombreLabel.grid(row=0, column=1, padx=10, pady=10)
nombreEntryD=ttk.Entry(frame_doctores)
nombreEntryD.grid(row=0, column=2, padx=10, pady=10)
#Especialidad
especialidadLabel=ttk.Label(frame_doctores, text="Especialidad:")
especialidadLabel.grid(row=2, column=1, padx=10, pady=10)
especialidad=tk.StringVar()
especialidadCombo=ttk.Combobox(frame_doctores, values=["Cardiologia", "Neurologia","Pediatria","Traumatologia", "Ninguno"], state="readonly",textvariable=especialidad)
especialidadCombo.grid(row=2, column=2, padx=10, pady=10)
#Edad
edadD=tk.Label(frame_doctores, text="Edad:")
edadD.grid(row=3, column=1, padx=5, pady=5)
edadSpin=tk.Spinbox(frame_doctores, from_=18, to=90)
edadSpin.grid(row=3, column=2, padx=10, pady=10)
#Telefono
telLabel=ttk.Label(frame_doctores,text="Telefono")
telLabel.grid(row=4,column=1,padx=10,pady=10)
telEntry=ttk.Entry(frame_doctores)
telEntry.grid(row=4, column=2, padx=10, pady=10)
#Frame para los botones
btn_frame=ttk.Frame(frame_doctores)
btn_frame.grid(row=5,column=1,columnspan=2,pady=5,sticky="w")
#boton registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarDoctores,bg="#008f39",fg="white")
btn_registrar.grid(row=5,column=1,padx=5)
#boton Eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="",bg="red",fg="white")
btn_eliminar.grid(row=5,column=2,padx=5)
#Crear TreeView 
treeviewD = ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad", "Edad","telefono"),show="headings")
#Definir encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("Edad",text="Edad")
treeviewD.heading("telefono",text="telefono")
#Definir anchos
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("Edad",width=50,anchor="center")
treeviewD.column("telefono",width=120,anchor="center")
#Ubicar el TreeView
treeviewD.grid(row=6,column=1,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar
scorll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeviewD.configure(yscrollcommand=scorll_y.set)
scorll_y.grid(row=6,column=2,sticky="ns")
ventana_principal.mainloop()
