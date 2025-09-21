#APLICACION DE AGENDA PERSONAL
import tkinter as tk
# Importa la librería principal para crear interfaces gráficas

from tkinter import ttk, messagebox
# Importa  cuadros de mensaje (messagebox)

from tkcalendar import DateEntry
# Importa el selector de fechas tipo calendario

# Creamos la ventana principal
root = tk.Tk()
# Inicializa la ventana principal de la aplicación

root.title("AGENDA PERSONAL")
# Asigna el título a la ventana

root.geometry("700x400")
# Definimos el tamaño de la ventana

# Organización con contenedores
frame = tk.Frame(root)
# Crea un contenedor (Frame) para organizar visualmente la tabla de eventos

frame.pack(pady=30)
# Colocamos el Frame en la ventana con espacio vertical

# Treeview para mostrar eventos
columns = ("Fecha", "Hora", "Evento")
# Definimos las columnas que tendrá la tabla de eventos

tree = ttk.Treeview(frame, columns=columns, show="headings")
# Creamos la tabla TreeView con las columnas definidas

for col in columns:
    tree.heading(col, text=col)
    # Asigna el nombre visible a cada columna

tree.pack()
# Muestra la tabla en la pantalla

# Organización con contenedores: Frame para botones
btn_frame = tk.Frame(root)
# Crea otro contenedor para los botones de acción

btn_frame.pack(pady=10)
# Lo coloca debajo con espacio vertical

#  MANEJO DE EVENTOS: Función para agregar un nuevo evento
def agregar_evento():
    ventana_agregar = tk.Toplevel(root)
    # Creamos una ventana secundaria para ingresar los datos del evento

    ventana_agregar.title("Agregar Evento")
    # Asignamos el título a la ventana emergente

    #  COMPONENTES AVANZADOS: Etiqueta y campo para seleccionar la fecha
    tk.Label(ventana_agregar, text="Fecha:").grid(row=0, column=0)
    # Etiqueta para  colocar la fecha

    fecha_entry = DateEntry(ventana_agregar, width=12, background='pink', foreground='pink', borderwidth=2)
    # Campo para seleccionar la fecha

    fecha_entry.grid(row=0, column=1)
    # Colocamos el campo de fecha en la ventana

    tk.Label(ventana_agregar, text="Hora:").grid(row=1, column=0)
    # Etiqueta para el campo de hora

    hora_entry = tk.Entry(ventana_agregar)
    # Campo de texto para ingresar la hora

    hora_entry.grid(row=1, column=1)
    # Colocamos el campo de hora en la ventana

    tk.Label(ventana_agregar, text="Evento:").grid(row=2, column=0)
    # Etiqueta para el campo de descripción del evento

    evento_entry = tk.Entry(ventana_agregar)
    # Campo de texto para ingresar el nombre o descripción del evento

    evento_entry.grid(row=2, column=1)
    # Colocamos el campo de evento en la ventana

    # Función para guardar el evento en la tabla
    def guardar():
        fecha = fecha_entry.get()
        # Obtiene la fecha seleccionada

        hora = hora_entry.get()
        # Obtiene la hora ingresada

        evento = evento_entry.get()
        # Obtiene el texto del evento

        if not fecha or not hora or not evento:
            # Verifica que todos los campos estén llenos

            messagebox.showerror("Error", "Todos los campos son obligatorios")
            # Muestra un mensaje de error si falta algún dato

            return
            # Sale de la función sin guardar

        tree.insert("", "end", values=(fecha, hora, evento))
        # Inserta el evento en el TreeView

        ventana_agregar.destroy()
        # Cierra la ventana de agregar evento

    tk.Button(ventana_agregar, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2)
    # Botón para guardar el evento ingresado

# MANEJO DE EVENTOS
# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    # Obtiene el elemento seleccionado en la tabla

    if not seleccionado:
        # Verifica si no hay selección

        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")
        # Muestra una advertencia si no se ha seleccionado ninguna opcion

        return
        # Sale de la función

    tree.delete(seleccionado)
    # Elimina el evento seleccionado del TreeView

# Botones principales
tk.Button(btn_frame, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=5)
# Creamos el botón para Agregar Evento

tk.Button(btn_frame, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side="left", padx=5)
# Creamos el botón para Eliminar Evento Seleccionado

tk.Button(btn_frame, text="Salir", command=root.quit).pack(side="left", padx=5)
# Creamos el botón Salir para cerrar la aplicacion

#  INTERFAZ GRÁFICA
root.mainloop()
# Inicia el bucle principal de la aplicación manteniendo la ventana abierta
