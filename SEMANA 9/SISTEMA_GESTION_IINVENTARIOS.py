#PROGRAMA DE GESTION DE INVENTARIOS SIMPLE PARA UNA TIENDA
#NOS PERMITE AÑADIR,ACTUALIZAR,BUSCAR,ELIMINAR Y BUSCAR PRODUCTOS
#USAMOS UNA ESTRUCTURA DE DATOS PERSONALIZADA
# 1. Utilizamos la clase Producto
class Producto:
# 2. Inicializamos el constructor con los atributos
    def __init__(self,ID_PRODUCTO,NOMBRE,CANTIDAD,PRECIO):
        self.ID_PRODUCTO=ID_PRODUCTO
        self.NOMBRE=NOMBRE
        self.CANTIDAD=CANTIDAD
        self.PRECIO=PRECIO

# 3. Usamos el metodo Getters para poder acceder a los atributos de la clase de forma controlada
    def get_ID_PRODUCTO(self):
        return self.ID_PRODUCTO
    def get_NOMBRE(self):
        return self.NOMBRE
    def get_CANTIDAD(self):
        return self.CANTIDAD
    def get_PRECIO(self):
        return self.PRECIO

# 4. Creamos la clase inventario
class INVENTARIO:
# 5. Definimos nuestro metodo constructor
    def __init__(self):
# 6. Inicializamos el diccionario donde se almacena los productos del inventario
        self.productos={}

# 7. Definimos un metodo que nos permite añadir un producto
    def añadir_nuevoproducto(self,PRODUCTO):
        if PRODUCTO.get_ID_PRODUCTO() in self.productos:#verifica si el producto ya existe
            print("Error: Producto ya existe.")
        else:# si el producto no existe lo agrega al inventario
            self.productos[PRODUCTO.get_ID_PRODUCTO()]=PRODUCTO
            print("Producto Agregado con exito")

# 8. Definimos un metodo que nos permite eliminar un producto po ID
    def eliminar_procuctoporID(self,ID_PRODUCTO):
        if ID_PRODUCTO in self.productos: # verifica el producto por ID
            del self.productos[ID_PRODUCTO] # usamos del para eliminar el producto
            print("Producto eliminado con exito")
        else:# si no encuentra el ID del producto imprime el mensaje
            print("Error:Producto no encontrado")

# 9. Usamo el metodo para actualizar los productos
    def actualizar_producto(self,ID_PRODUCTO,CANTIDAD=None,PRECIO=None):
        if ID_PRODUCTO in self.productos:# verifica si el producto ya existe
            if CANTIDAD:# actualizamos la cantidad del producto
                self.productos[ID_PRODUCTO].set_cantidad(CANTIDAD)
            if PRECIO:# actualizamos el precio del producto
                self.productos[ID_PRODUCTO].set_precio(PRECIO)
            print("Producto Actualizado con Exito.")
        else:# si el producto no existe se imprime
            print("Error:Producto no encontrado")

# 10. Usamos un metodo para buscar el producto
    def buscar_producto(self,NOMBRE):
# creamos una lista
# usamos el metodo values para obtener una lista de todos los productos del inventario
# usamos el metodo lower para ignorar mayusculas y minusculas al momento de buscar el producto
        resultados=[PRODUCTO for PRODUCTO in self.productos.values() if NOMBRE.lower() in PRODUCTO.get_NOMBRE().lower()]
        if resultados:
            for PRODUCTO in resultados: # iteramos sobre la lista de productos que coinciden con la busqueda
                print(f"ID:{PRODUCTO.get_ID_PRODUCTO()}, NOMBRE:{PRODUCTO.get_NOMBRE()}, CANTIDAD:{PRODUCTO.get_CANTIDAD()}, PRECIO:{PRODUCTO.get_PRECIO()}")
        else:#  si los productos no se encuentran se imprime
            print("No se encontraron productos con el nombre especificado")

# 11. creamos el metodo para mostrar inventario
    def mostrar_inventario(self):
        if self.productos: # verifica si el inventario contiene productos
            for PRODUCTO in self.productos.values(): # itera sobre la lista de productos en el inventario
                # imprime las especificaciones de cada produto
                print(f"ID: {PRODUCTO.get_ID_PRODUCTO()}, NOMBRE:{PRODUCTO.get_NOMBRE()}, CANTIDAD:{PRODUCTO.get_CANTIDAD()}, PRECIO:{PRODUCTO.get_PRECIO()}")
        else: # si el inventario esta vacio imprime
            print("No hay productos en el inventario.")

# 12. definimos la funcion llamada menu
def menu():
    inventario=INVENTARIO() # creamos el objeto inventario
# 13. inicializamos el bucle while que muestra el menu de opciones
    while True:
        print("-Menu de Opciones-:")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion=input("Ingrese la opcion que desea:")

#14. deacuerdo a la opcion que ingrese el usuario permite su interaccion con el usuario
        if opcion=="1":
# solicita al usuario que ingrese la informacion del producto
            ID_PRODUCTO=input("Ingrese el ID del Producto:")
            NOMBRE=input("Ingrese el nombre del producto:")
            CANTIIDAD=int(input("Ingrese la cantidad del producto:"))
            PRECIO=float(input("Ingrese el precio del producto:"))
# crea el objeto producto con la informacion que proporciona el usuario
            producto=Producto(ID_PRODUCTO,NOMBRE,CANTIIDAD,PRECIO)
# agrega el producto al inventario
            inventario.añadir_nuevoproducto(producto)
        elif opcion=="2":
            ID_PRODUCTO=input("Ingrese el ID del producto a eliminar:")
            inventario.eliminar_procuctoporID(ID_PRODUCTO)
        elif opcion=="3":
            ID_PRODUCTO=input("Ingrese el ID del producto a actualizar:")
            CANTIIDAD=input("Ingrese la nueva cantidad:")
            PRECIO=input("Ingrese el nuevo precio")
            if CANTIIDAD and PRECIO:
                inventario.actualizar_producto(ID_PRODUCTO,int(CANTIIDAD),float(PRECIO))
            elif CANTIIDAD:
                inventario.actualizar_producto(ID_PRODUCTO,int(CANTIIDAD))
            elif PRECIO:
                inventario.actualizar_producto(ID_PRODUCTO,float(PRECIO))
            else:
                print("No se especificaron cambios.")
        elif opcion=="4":
            NOMBRE=input("Ingrese el nombre del producto a buscar:")
            inventario.buscar_producto(NOMBRE)
        elif opcion=="5":
            inventario.mostrar_inventario()
        elif opcion=="6":
            break
        else:
            print("Opcion invalida.Por favor intente nuevamente.")

# 15. ejecutamos la funcion menu
if __name__ == "__main__":
    menu()

