import tkinter as tk
from tkinter import ttk, messagebox



def guardarArchivoD():
    with open("doctores.txt","w",encoding="utf-8") as archivo:
        for doctores in doctores_data:
            archivo.write(f"{doctores['NombreD']}|{doctores['Especialidad']}|{doctores['AñosExD']}|{doctores['Genero']}|{doctores['Hospital']}\n")

def cargarArchivoDoctores():
    try:
        with open("doctores.txt","r",encoding="utf-8")as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==5:
                    doctores={
                        "NombreD":datos[0],
                        "Especialidad":datos[1],
                        "AñosExD":datos[2],
                        "Genero":datos[3],
                        "Hospital":datos[4]
                    }
                    doctores_data.append(doctores)
        cargar_treeviewD()
    except FileNotFoundError:
        open("doctores.txt","w",encoding="utf-8").close() 
        

        
paciente_data=[]
doctores_data=[]

    

def registrarDoctores():
    doctor={
        "NombreD": nombreEntryD.get(),
        "Especialidad": especialidad.get(),
        "AñosExD": AñosExDSpin.get(),
        "Genero": rbGenero.get(),
        "Hospital":Hospital.get()
    }
    doctores_data.append(doctor)
    guardarArchivoD()
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
                item["AñosExD"],
                item["Genero"],
                item["Hospital"]
            )
        )

    
def eliminarDoctores():
    seleccionado=treeviewD.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar paciente", f"Estas seguro de eliminar el doctor '{treeviewD.item(id_item, 'values')[0]}'?"):
            del doctores_data[indice]
            guardarArchivoD()
            cargar_treeviewD()
            messagebox.showinfo("Eliminar doctor", "Doctor eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar doctor", "No se ha selecionado ningun doctor")
        return
    
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Doctores")
ventana_principal.geometry("700x650")
#contenedor notebook
pestanas=ttk.Notebook(ventana_principal)
#Crear frames
frame_doctores=ttk.Frame(pestanas)
#Agregar frames a las pestanas
pestanas.add(frame_doctores, text="Doctores")
#Mostrar las pestanas
pestanas.pack(expand=True, fill="both")
    
nombreLabel=ttk.Label(frame_doctores, text="Nombre:")
nombreLabel.grid(row=0, column=0, padx=10, pady=10)
nombreEntryD=ttk.Entry(frame_doctores)
nombreEntryD.grid(row=0, column=1, padx=10, pady=10)
#Especialidad
especialidadLabel=ttk.Label(frame_doctores, text="Especialidad:")
especialidadLabel.grid(row=2, column=0, padx=10, pady=10)
especialidad=tk.StringVar()
especialidadCombo=ttk.Combobox(frame_doctores, values=["Cardiologia", "Neurologia","Pediatria","Traumatologia", "Ninguno"], state="readonly",textvariable=especialidad)
especialidadCombo.grid(row=2, column=1, padx=10, pady=10)
#Años de Experiencia
AñosExD=tk.Label(frame_doctores, text="Años de Experiencia:")
AñosExD.grid(row=3, column=0, padx=5, pady=5)
AñosExDSpin=tk.Spinbox(frame_doctores, from_=1, to=60)
AñosExDSpin.grid(row=3, column=1, padx=10, pady=10)
#Genero
Genero=ttk.Label(frame_doctores, text="Genero:")
Genero.grid(row=4, column=0, padx=5, pady=5, sticky="w")
rbGenero=tk.StringVar()
rbGenero.set("Masculino")
rbMasculino=ttk.Radiobutton(frame_doctores, text="Masculino", variable=rbGenero, value="Masculino")
rbMasculino.grid(row=4, column=1, padx=5, pady=5)
rbFemenino=ttk.Radiobutton(frame_doctores, text="Femenino", variable=rbGenero, value="Femenino")
rbFemenino.grid(row=5, column=1, padx=5, pady=5)
#Hospital
centroLabel=ttk.Label(frame_doctores, text="Centro Medico:")
centroLabel.grid(row=6, column=0, padx=5, pady=10, sticky="w")
Hospital=tk.StringVar()
centroCombo=ttk.Combobox(frame_doctores, values=["Clinica Norte", "Hospital General", "Centro del Sur"], state="readonly",textvariable=Hospital)
centroCombo.grid(row=6, column=1, padx=5, pady=10)
#Frame para los botones
btn_frame=ttk.Frame(frame_doctores)
btn_frame.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")
#boton registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarDoctores,bg="#008f39",fg="white")
btn_registrar.grid(row=8,column=0,padx=5)
#Crear TreeView 
treeviewD = ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad", "AñosEx","Genero","Hospital"),show="headings")
#Definir encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("AñosEx",text="Años de Experiencia")
treeviewD.heading("Genero",text="Genero")
treeviewD.heading("Hospital",text="Hospital")
#Definir anchos
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("AñosEx",width=100,anchor="center")
treeviewD.column("Genero",width=120,anchor="center")
treeviewD.column("Hospital",width=120,anchor="center")
#Ubicar el TreeView
treeviewD.grid(row=9,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar
scorll_y=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scorll_y.set)
scorll_y.grid(row=9,column=4,sticky="ns")
cargarArchivoDoctores()
ventana_principal.mainloop()
    
