# APLICACION DE GESTOR DE TAREAS CON ATAJOS DE TECLADO
# Utilizamos la libreria tkinter para la interfaz de usuario
import tkinter as tk
from tkinter import messagebox

# Creamos la ventana principal de la aplicación
root = tk.Tk()
root.title("GESTOR DE TAREAS")
root.geometry("500x500")

# Creamos el campo de entrada para escribir las tareas
entrada_tarea = tk.Entry(root, font=("Arial", 12))
entrada_tarea.pack(pady=10)

# Creamos la lista donde se mostrara las tareas
lista_tareas = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
lista_tareas.pack(expand=True, fill="both", padx=10, pady=10)

# Creamos la función para agregar una nueva tarea
def Agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Primero escribe una tarea.")

# Creamos la funcion para completar la tarea
def Completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("X"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "X " + tarea)

# creamos la funcion para poder eliminar la tarea seleccionada
def Eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])

# creamos una funcion para cerrar la aplicacion
def Salir(event=None):
    root.quit()

# Creamos un marco horizontal para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# creamos un boton para agregar la tarea
btn_agregar = tk.Button(frame_botones, text="Agregar", command=Agregar_tarea, bg="#FFB74D", fg="black", width=12)
btn_agregar.pack(side="left", padx=5)

# creamos un boton para completar la tarea
btn_completar = tk.Button(frame_botones, text="Completar", command=Completar_tarea, bg="#81C784", fg="black", width=12)
btn_completar.pack(side="left", padx=5)

# creamos un boton para eliminar la tarea
btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=Eliminar_tarea, bg="#64B5F6", fg="black", width=12)
btn_eliminar.pack(side="left", padx=5)

# Implementamos un atajo de teclado para marcar la tarea seleccionada con la tecla enter
entrada_tarea.bind("<Return>", Agregar_tarea)

# Implementamos un atajo de teclado para marcar la tarea seleccionada como completada con la letra c
root.bind("<c>", Completar_tarea)

# Implementamos un atajo de teclado para eliminar la tarea con la letra d
root.bind("<d>", Eliminar_tarea)
root.bind("<Delete>", Eliminar_tarea)

# Implementamos un atajo para salir de la aplicacion utilizando la tecla de Esc
root.bind("<Escape>", Salir)

# Inicializamos la aplicacion
root.mainloop()