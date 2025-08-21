# PROGRAMA DE GESTION DE INVENTARIOS MEJORADO
# El programa utiliza un archivo "txt" para recuperar y almacenar
# y recuperar la informacion del inventario y manejo de excepciones

# Creamos la clase inventario
class Inventario:
# Definimos el metodo constructor
# Creamos la variable archivo con valor inventario.txt en este archivo se almacenara el inventario
    def __init__(self,archivo="inventario.txt"):
# Utilizamos un diccionario para almacenar los productos del inventario
        self.productos={}
        self.archivo=archivo
        self.cargar_inventario()
# 1. RECUPERACION DE INVENTARIOS DESDE ARCHIVOS

# Definimos el metodo que se encarga de leer el archivo de texto
    def cargar_inventario(self):
# Usamos la estructura de control try para excepciones y errores en el codigo
        try:
# Abrimos el archivo en modo lectura "r"
            with open(self.archivo,"r") as archivo:
# El bucle for lee cada linea del archivo
                for linea in archivo:
# Utilizamos el metodo strip para borrar espacios al comienzo y final de cada linea
                    linea=linea.strip()
# Verifica si la linea existe
                    if linea:
# Utilizamos el metodo split como separador y la dividimos en 3 partes con el caracter ","
                        codigo,nombre,cantidad=linea.split(",")
# Almacenamos cada producto en el diccionario
                        self.productos[codigo]={"nombre":nombre,"cantidad":int(cantidad)}
# Captura la excepcion si el archivo no existe
        except FileNotFoundError:
            print(f"No se encontro el archivo {self.archivo}.Por tanto crearemos uno nuevo")
# Abrimo un nuevo archivo en modo escritura
            open(self.archivo,"w").close()
# Captura si se produce otra excepcion
        except Exception as e:
            print(f"Error al cargar el Inventario: {e}")

# 2. ALMACENAMIENTO DE DATOS EN ARCHIVOS

# Definimos el metodo guardar inventario
    def guardar_inventario(self):
# Usamos try para para excepciones y errores
        try:
# Abrimos el archivo en modo lectura
            with open(self.archivo,"w") as archivo:
                for codigo, producto in self.productos.items():
# Escribe una linea en el archivo con el codigo nombre cantidad separado por comas
                    archivo.write(f"{codigo},{producto['nombre']},{producto['cantidad']}\n")
# Imprime que el inventario se ha guardado
                    print("Inventario Guardado Exitosamente")
# Usamos excepciones pra controlar permisos
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo}.")
# Captura si ocurre una excepcion en la ejecucion del programa
        except Exception as e:
            print(f"Error al guardar el iventario: {e}")

# Definimos un metodo para agregar productos
    def agregar_producto(self,codigo,nombre,cantidad):
# Usamos try para manejo de errores y excepciones
        try:
            self.productos[codigo]={"nombre":nombre, "cantidad":cantidad}
            self.guardar_inventario()
            print(f"Producto {nombre} agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar el producto {e}")
# Definimos el metodo para actualizar productos
    def actualizar_producto(self,codigo,nombre=None, cantidad=None):
# Uso del try para manejo de errores y excepciones
        try:
            if codigo in self.productos:
                if nombre:
                    self.productos[codigo]["nombre"]=nombre
                if cantidad:
                    self.productos[codigo]["cantidad"]=cantidad
                self.guardar_inventario()
                print(f"Producto {codigo} actualizado exitosamente.")
            else:
                print(f"No se encontro el producto {codigo}.")
        except Exception as e:
            print(f"Error al actualizar el producto {e}")
# Definimos el metodo para actualizar productos
    def eliminar_producto(self,codigo):
# Usamos try para manejo de errores y excepciones
        try:
            if codigo in self.productos:
                del self.productos[codigo]
                self.guardar_inventario()
                print(f"Producto {codigo} eliminado exitosamente.")
            else:
                print(f"No se encontro el producto {codigo}.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
# Definmos el metodo para mostrar los productos
    def mostrar_productos (self):
# Usamos try para manejo de errores y excepciones
        try:
            for codigo, producto in self.productos.items():
                print(f"Codigo {codigo},Nombre:{producto['nombre']},Cantidad:{producto['cantidad']}")
        except Exception as e:
            print(f"Error al mostrar los productos: {e}")
# Creamos el objeto inventario
inventario=Inventario()
# Inicializamos el bucle que nos muestra el menu de opciones
while True:
    print("-MENU DE OPCIONES-")
    print ("1. Agregar Producto")
    print("2. Actualizar Producto")
    print("3. Eliminar Producto")
    print("4. Mostrar Productos")
    print("5. Salir")
# El usuario elige una opcion y solicita que coloque la informacion que desea el usuario
    opcion=input("Seleccione una Opcion:")
    if opcion=="1":
        codigo=input("Ingrese el codigo del producto:")
        nombre=input("Ingrese el nombre del producto:")
        cantidad=int(input("Ingrese la cantidad del producto:"))
        inventario.agregar_producto(codigo,nombre,cantidad)
    elif opcion=="2":
        codigo=input("Ingrese el codigo del producto")
        nombre=input("Ingrese el nuevo nombre del producto (opcional):")
        cantidad=input("Ingrese la nueva cantidad del producto (opcional):")
        if cantidad:
            cantidad=int(cantidad)
        else:
            cantidad=None
        if nombre=="":
            nombre=None
        inventario.actualizar_producto(codigo,nombre,cantidad)
    elif opcion=="3":
        codigo=input("Ingrese el codigo del producto")
        inventario.eliminar_producto(codigo)
    elif opcion=="4":
        inventario.mostrar_productos()
    elif opcion=="5":
        break
    else:
        print("Opcion invalida intente nuevamente")
