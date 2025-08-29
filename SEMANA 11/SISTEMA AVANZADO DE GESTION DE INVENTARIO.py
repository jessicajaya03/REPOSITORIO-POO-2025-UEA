#SISTEMA AVANZADO DE GESTION DE INVENTARIO
#1. Primero definimos la lcase producto
class Producto:
# Inicializamos los atributos de la clase
    def __init__(self,id_producto,nombre,cantidad,precio):
        self.id_producto=id_producto
        self.nombre=nombre
        self.cantidad=cantidad
        self.precio=precio
#Colocamos los metodos de la clase producto
#Usamos metodos get y set para poder acceder y modificar los atributos
    def get_id_producto(self):
        return self.id_producto
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad
    def set_precio(self,precio):
        self.precio=precio
# Usamos el metodo str que devuelve una representacion en cadena del objeto
    def __str__(self):
        return f"ID:{self.id_producto}, NOMBRE:{self.nombre}, CANTIDAD: {self.cantidad}, PRECIO: {self.precio}"
#2. Creamos la clase inventario
class Inventario:
    def __init__(self):
# Creamos un diccionario donde se almacenaran los productos
        self.productos={}
# Realizamos los metodos de la clase inventario
# Este metodo nos permite agregar un producto al inventario
# toma un objeto producto y lo agrega al diccionario productos utiliza el ID del producto como clave
    def agregar_producto(self,producto):
        self.productos[producto.get_id_producto()] = producto
# Este metodo se usa para eliminar objetos del inventario
# toma el id del producto y lo busca en el diccionario si se encuentra en el lo elimina
    def eliminar_producto(self,id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(" NO SE ENCONTRO EL PRODUCTO SELECCIONADO.")
# Este metodo nos permite actualizar la cantidad del producto
# Con el id del producto y la cantidad busca en el diccionario y permite actualizar la cantidad
    def actualizar_cantidad(self,id_producto,cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(cantidad)
        else:
            print("EL PRODUCTO NO SE ENCONTRO")
# Este metodo nos permite actualizar el precio
# toma el id del producto lo busca en el diccionario y actualiza el precio
    def actualizar_precio(self,id_producto,precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(precio)
        else:
            print("NO SE ENCONTRO EL PRODUCTO SELECCIONADO")
# 3. Usamos el almacenamiento de datos en archivos
# Este metodo se utiliza para buscar un producto en el inventario por nombre
    def buscar_producto(self,nombre):
        for producto in self.productos.values():
            if producto.get_nombre().lower()==nombre.lower():
                return producto
        return None
# Utilizamos este metodo para mostrar todos los productos del inventario
    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)
# Utilizamos este metodo para guardar el inventario en un archivo
    def guardar_inventario(self,archivo):
# Abrimos el archivo en moso lectura
        with open(archivo,'w') as f:
            for producto in self.productos.values():
                f.write(f"{producto.get_id_producto()}, {producto.get_nombre()},{producto.get_cantidad()}, {producto.get_precio()}\n")
# Utilizamos este metodo para cargar el inventario desde un archivo
# Usamos metodos try para manejo de excepciones y errores
    def cargar_inventario(self,archivo):
        try:
            with open(archivo,'r') as f:
                for linea in f.readlines():
                    id_producto,nombre,cantidad,precio=linea.strip().split(',')
                    producto=Producto(id_producto,nombre,int(cantidad),float(precio))
                    self.agregar_producto(producto)
        except FileNotFoundError:
            print("ARCHIVO NO ENCONTRADO")
def main():
# Creamos un objeto inventario
    inventario=Inventario()
    while True:
# Creamos un menu de opciones para que el usuario elija una opcion
        print("-MENU DE OPCIONES-")
        print("1. AGREGAR PRODUCTO.")
        print("2. ELIMINAR PRODUCTO.")
        print("3. ACTUALIZAR CANTIDAD.")
        print("4. ACTUALIZAR PRECIO.")
        print("5. BUSCAR PRODUCTO.")
        print("6. MOSTRAR PRODUCTOS.")
        print("7. GUARDAR INVENTARIO.")
        print("8. CARGAR INVENTARIO.")
        print("9. SALIR.")
        opcion=input("INGRESE LA OPCION QUE DESEA")
        if opcion=='1':
            id_producto=input("INGRESE EL ID DEL PRODUCTO:")
            nombre=input("INGRESE EL NOMBRE DEL PRODUCTO:")
            cantidad=int(input("INGRESE LA CANTIDAD DEL PRODUCTO:"))
            precio=float(input("INGRESE EL PRECIO DEL PRODUCTO:"))
            producto=Producto(id_producto,nombre,cantidad,precio)
            inventario.agregar_producto(producto)
        elif opcion=='2':
            id_producto=input("INGRESE EL ID DEL PRODUCTO QUE DESEA ELIMINAR")
            inventario.eliminar_producto(id_producto)
        elif opcion=='3':
            id_producto=input("INGRESE EL ID DEL PRODUCTO QUE DESEA ACTUALIZAR")
            cantidad=int(input("INGRESE LA NUEVA CANTIDAD:"))
            inventario.actualizar_cantidad(id_producto,cantidad)
        elif opcion=='4':
            id_producto=input("INGRESE EL ID DEL PRODUCTO A ACTUALIZAR")
            precio=float(input("INGRESE EL NUEVO PRECIO:"))
            inventario.actualizar_precio(id_producto,precio)
        elif opcion=='5':
            nombre=input("INGRESE EL NOMBRE DEL PRODUCTO A ACTUALIZAR")
            producto_encontrado=inventario.buscar_producto(nombre)
            if producto_encontrado:
                print(producto_encontrado)
            else:
                print("PRODUCTO NO ENCONTRADO")
        elif opcion=='6':
            inventario.mostrar_productos()
        elif opcion=='7':
            archivo=input("INGRESE EL NOMBRE DEL ARCHIVO:")
            inventario.guardar_inventario(archivo)
        elif opcion=='8':
            archivo=input("INGRESE EL NOMBRE DEL ARCHIVO:")
            inventario.cargar_inventario(archivo)
        elif opcion=='9':
            break
        else:
            print("OPCION NO VALIDA")
if __name__ == "__main__":
    main()



