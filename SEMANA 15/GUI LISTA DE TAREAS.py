# GUI DE LISTA DE TAREAS
# Importamos la libreria Tkinter
import tkinter as tk
# Usamos messagebox para mostrar mensajes de alertas
from tkinter import messagebox

# Creamos la ventana principal
root = tk.Tk()
# Colocamos el titulo y tamaño de la ventana
root.title("LISTA DE TAREAS")
root.geometry("500x500")

# Colocamoa una funcion para añadir una tarea a la lista
def Añadir_Tarea():
    tarea = entry_tarea.get().strip()
# Si existe una tarea realizamos
    if tarea:
# Añadimos la tarea al final de la lista
        listbox_tareas.insert(tk.END, tarea)
# Limpiamos el campo de entrada
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("ADVERTENCIA", "ESCRIBE UNA TAREA.")
# Definimos una funcion para marcar una tarea como completada
def Marcar_Completada():
# Obtenemos el indice de la tarea seleccionada
    seleccion = listbox_tareas.curselection()
# Si existe una seleccion
    if seleccion:
        tarea = listbox_tareas.get(seleccion)
        if not tarea.startswith("X"):
            listbox_tareas.delete(seleccion)
            listbox_tareas.insert(seleccion, f"X {tarea}")
    else:
        messagebox.showinfo("Info", "Selecciona una tarea para marcar.")
# Definimos una funcion para eliminar una tarea de la lista
def Eliminar_Tarea():
# Obtenemos la seleccion
    seleccion = listbox_tareas.curselection()
# Eliminamos la seleccion
    if seleccion:
        listbox_tareas.delete(seleccion)
    else:
        messagebox.showinfo("Info", "SELECCIONA UNA TAREA DE LA LISTA PARA ELIMINARLA.")

# Creamos un campo de entrada para escribir nuevas tareas
entry_tarea = tk.Entry(root, width=40, font=("Arial", 12))
entry_tarea.pack(pady=10)
# Al presionar enter nos permitira añadir una nueva tarea
entry_tarea.bind("<Return>", lambda event: Añadir_Tarea())

# Creamos un contenedor para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)
# Creamos los bontones para añadir tarea
btn_añadir = tk.Button(frame_botones, text="Añadir Tarea", width=15, command=Añadir_Tarea)
btn_añadir.grid(row=0, column=0, padx=5)
# Creamos botones para marcar tarea como completada
btn_completar = tk.Button(frame_botones, text="Marcar como Completada", width=20, command=Marcar_Completada)
btn_completar.grid(row=0, column=1, padx=5)
# Creamos botones para eliminar la tarea
btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", width=15, command=Eliminar_Tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Creamos una lista para mostrar las tareas
listbox_tareas = tk.Listbox(root, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
listbox_tareas.pack(pady=10)

# Ejecutamos la aplicacion
root.mainloop()