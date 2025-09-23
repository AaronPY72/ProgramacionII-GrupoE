import tkinter as tk
from tkinter import ttk, messagebox


signos_vitales_data = []

def guardarArchivoSV():
    with open("signos_vitales.txt", "w", encoding="utf-8") as archivo:
        for signo in signos_vitales_data:
            archivo.write(f"{signo['Paciente']}|{signo['Edad']}|{signo['FrecuenciaCardiaca']}|{signo['PresionSistolica']}|{signo['PresionDiastolica']}|{signo['SaturacionOxigeno']}|{signo['Temperatura']}\n")

def cargarArchivoSignosVitales():
    try:
        with open("signos_vitales.txt", "r", encoding="utf-8") as archivo:
            signos_vitales_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    signo = {
                        "Paciente": datos[0],
                        "Edad": datos[1],
                        "FrecuenciaCardiaca": datos[2],
                        "PresionSistolica": datos[3],
                        "PresionDiastolica": datos[4],
                        "SaturacionOxigeno": datos[5],
                        "Temperatura": datos[6]
                    }
                    signos_vitales_data.append(signo)
        cargar_treeviewSV()
    except FileNotFoundError:
        open("signos_vitales.txt", "w", encoding="utf-8").close()

def registrarSignosVitales():
    #Validacion de Datos del Paciente
    if not nombreEntrySV.get() or not edadEntry.get() or not fcEntry.get():
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")
        return
    
    try:
        fc = int(fcEntry.get())
        ps = int(psEntry.get())
        pd = int(pdEntry.get())
        so = int(soEntry.get())
        temp = float(tempEntry.get())
        
        if fc <= 0 or ps <= 0 or pd <= 0 or so < 0 or so > 100 or temp < 30 or temp > 45:
            raise ValueError("Valores fuera de rango")
            
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos")
        return
    #registro de datos 
    signo = {
        "Paciente": nombreEntrySV.get(),
        "Edad": edadEntry.get(),
        "FrecuenciaCardiaca": fcEntry.get(),
        "PresionSistolica": psEntry.get(),
        "PresionDiastolica": pdEntry.get(),
        "SaturacionOxigeno": soEntry.get(),
        "Temperatura": tempEntry.get()
    }
    
    signos_vitales_data.append(signo)
    guardarArchivoSV()
    cargar_treeviewSV()
    messagebox.showinfo("Éxito", "Signos vitales registrados correctamente")
    limpiar_camposSV()

def cargar_treeviewSV():
    for item in treeviewSV.get_children():
        treeviewSV.delete(item)
    for i, signo in enumerate(signos_vitales_data):
        treeviewSV.insert(
            "", "end", iid=str(i),
            values=(
                signo["Paciente"],
                signo["Edad"],
                signo["FrecuenciaCardiaca"],
                f"{signo['PresionSistolica']}/{signo['PresionDiastolica']}",
                signo["SaturacionOxigeno"],
                signo["Temperatura"]
            )
        )

def eliminarSignosVitales():
    seleccionado = treeviewSV.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar registro", f"¿Está seguro de eliminar el registro de '{treeviewSV.item(id_item, 'values')[0]}'?"):
            del signos_vitales_data[indice]
            guardarArchivoSV()
            cargar_treeviewSV()
            messagebox.showinfo("Eliminar registro", "Registro eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar registro", "No se ha seleccionado ningún registro")
        return

def limpiar_camposSV():
    nombreEntrySV.delete(0, tk.END)
    edadEntry.delete(0, tk.END)
    fcEntry.delete(0, tk.END)
    psEntry.delete(0, tk.END)
    pdEntry.delete(0, tk.END)
    soEntry.delete(0, tk.END)
    tempEntry.delete(0, tk.END)

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Monitoreo Médico")
ventana_principal.geometry("800x650")

pestanas = ttk.Notebook(ventana_principal)
frame_signos_vitales = ttk.Frame(pestanas)
pestanas.add(frame_signos_vitales, text="Signos Vitales")
pestanas.pack(expand=True, fill="both")

tituloSV = ttk.Label(frame_signos_vitales, text="Registro de Signos Vitales", font=("Arial", 14, "bold"))
tituloSV.grid(row=0, column=0, columnspan=2, pady=10)

#Nombre
nombreLabelSV = ttk.Label(frame_signos_vitales, text="Nombre del Paciente:")
nombreLabelSV.grid(row=1, column=0, padx=10, pady=5, sticky="w")
nombreEntrySV = ttk.Entry(frame_signos_vitales, width=30)
nombreEntrySV.grid(row=1, column=1, padx=10, pady=5)
#Edad
edadLabel = ttk.Label(frame_signos_vitales, text="Edad:")
edadLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
edadEntry = ttk.Entry(frame_signos_vitales, width=30)
edadEntry.grid(row=2, column=1, padx=10, pady=5)
#Frecuencia Cardiaca
fcLabel = ttk.Label(frame_signos_vitales, text="Frecuencia Cardíaca (lpm):")
fcLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
fcEntry = ttk.Entry(frame_signos_vitales, width=30)
fcEntry.grid(row=3, column=1, padx=10, pady=5)
#Presion Arterial
presionLabel = ttk.Label(frame_signos_vitales, text="Presión Arterial:")
presionLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")
#Crear un frame para las entradas de presión arterial
frame_presion = ttk.Frame(frame_signos_vitales)
frame_presion.grid(row=4, column=1, padx=10, pady=5, sticky="w")
# Entradas para sistólica
psEntry = ttk.Entry(frame_presion, width=8)
psEntry.pack(side="left")#Left para que se alineen horizontalmente
separador = ttk.Label(frame_presion, text="/")
separador.pack(side="left")
#Entradas para diastólica
pdEntry = ttk.Entry(frame_presion, width=8)
pdEntry.pack(side="left")
mmHgLabel = ttk.Label(frame_presion, text="mmHg")
mmHgLabel.pack(side="left", padx=5)
#Saturacion de Oxigeno
soLabel = ttk.Label(frame_signos_vitales, text="Saturación de Oxígeno (%):")
soLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
soEntry = ttk.Entry(frame_signos_vitales, width=30)
soEntry.grid(row=5, column=1, padx=10, pady=5)
#Temperatura
tempLabel = ttk.Label(frame_signos_vitales, text="Temperatura (°C):")
tempLabel.grid(row=6, column=0, padx=10, pady=5, sticky="w")
tempEntry = ttk.Entry(frame_signos_vitales, width=30)
tempEntry.grid(row=6, column=1, padx=10, pady=5)
# Frame para los botones
btn_frameSV = ttk.Frame(frame_signos_vitales)
btn_frameSV.grid(row=7, column=0, columnspan=2, pady=15)

# Botón registrar
btn_registrarSV = tk.Button(btn_frameSV, text="Registrar", command=registrarSignosVitales, bg="#008f39", fg="white")
btn_registrarSV.grid(row=0, column=0, padx=5)

# Botón eliminar
btn_eliminarSV = tk.Button(btn_frameSV, text="Eliminar Registro", command=eliminarSignosVitales, bg="#d9534f", fg="white")
btn_eliminarSV.grid(row=0, column=2, padx=5)

# Crear TreeView para signos vitales
treeviewSV = ttk.Treeview(frame_signos_vitales, columns=("Paciente", "Edad", "FC", "Presión", "SatO2", "Temp"), show="headings")

# Definir encabezados
treeviewSV.heading("Paciente", text="Paciente")
treeviewSV.heading("Edad", text="Edad")
treeviewSV.heading("FC", text="Frec. Cardíaca")
treeviewSV.heading("Presión", text="Presión Arterial")
treeviewSV.heading("SatO2", text="Sat. Oxígeno")
treeviewSV.heading("Temp", text="Temperatura")

# Definir anchos
treeviewSV.column("Paciente", width=120)
treeviewSV.column("Edad", width=60, anchor="center")
treeviewSV.column("FC", width=100, anchor="center")
treeviewSV.column("Presión", width=100, anchor="center")
treeviewSV.column("SatO2", width=100, anchor="center")
treeviewSV.column("Temp", width=100, anchor="center")

# Ubicar el TreeView
treeviewSV.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Scrollbar
scroll_ySV = ttk.Scrollbar(frame_signos_vitales, orient="vertical", command=treeviewSV.yview)
treeviewSV.configure(yscrollcommand=scroll_ySV.set)
scroll_ySV.grid(row=8, column=2, sticky="ns")


cargarArchivoSignosVitales()

ventana_principal.mainloop()