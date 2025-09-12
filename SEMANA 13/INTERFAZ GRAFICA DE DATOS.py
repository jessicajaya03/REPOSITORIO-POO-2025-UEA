#Aplicacion De Interfaz Grafica de Usuario GUI que permite interactuar con el usuario agregando informacion
# 1. Primero importamos la libreria tkinter

import tkinter as tk
from tkinter import messagebox


# 2. Agregamos una funcion  para agregar datos
def agregar_dato():
    # verificamos si el campo no esta vacio
    dato = entrada.get()
    if dato:
        # se agregan los datos al final de la lista
        lista_datos.insert(tk.END, dato)
        # se limpia el campo de entrada
        entrada.delete(0, tk.END)
    # se muestra una advertencia si el campo esta vacio
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío.")

# 3. Agregamos una función para limpiar datos
def limpiar_datos():
    # borra todos los elementos de la lista
    lista_datos.delete(0, tk.END)
    entrada.delete(0, tk.END)

# 4. Creamos la ventana principal
root = tk.Tk()
# colocamos el titulo de la ventana
root.title("Software de recopilacion de datos")
# colocamos el tamaño de la ventana
root.geometry("400x300")

# 5. creamos la etiqueta de texto
label = tk.Label(root, text="Ingrese sus datos :")
label.pack(pady=5)

# 6. Creamos un campo de entrada de texto
entrada = tk.Entry(root, width=40)
entrada.pack(pady=5)

# 7. Creamos un contenedor frame para agrupar los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)
# 8. Creamos el boton agregar y lo vinculamos con la funcion agregar dato
btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_dato)
btn_agregar.pack(side=tk.LEFT, padx=5)
# 9. Creamos el boton limpiar y lo vinculamos con la funcion limpiar datos
btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(side=tk.LEFT, padx=5)

# 10. Creamos una etiqueta para mostrar la lista de informacion
label_lista = tk.Label(root, text="Lista de informacion:")
label_lista.pack(pady=5)
# 11. Creamos la lista listbox donde se mostrara los datos ingresados
lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=5)

# 11. Ejecutamos el bucle principal de eventos de la aplicacion que permite a la ventana estar abierta
root.mainloop()
