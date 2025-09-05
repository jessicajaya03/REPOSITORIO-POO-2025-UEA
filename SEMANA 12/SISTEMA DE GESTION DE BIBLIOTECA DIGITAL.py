#SISTEMA DE GESTION DE BIBLIOTECA DIGITAL
# El sistema permite administrar los libros disponibles, las categorías de libros, los usuarios registrados y el historial de préstamos.

#Primero creamos la clase libro
class Libro:
    #Definimos los atributos de nuestra clase
    def __init__(self, titulo, autor, categoria, isbn):
        # el título y autor se guardan como tupla inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"
#Creamos la clase usurio que permite el registro de las personas en la biblioteca
class Usuario:
    # Creamos los atributos de nuestra clase
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        #Creamos una lista vacia donde se almacenara los libros que tomen prestados los usuarios
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

# Creamos la clase biblioteca
class Biblioteca:
    def __init__(self):
        #creamos un diccionario donde se guardan los libros disponibles
        self.libros = {}
        # creamos un diccionario donde se gusrdan los usuarios registrados
        self.usuarios = {}
        # utilizamos un conjunto set para guardar los ids de los usuarios y no repetirlos
        self.ids_registrados = set()

    # Utilizamo el metodo para agregar libros
    def agregar_libro(self, libro):
    # verifica si el isbn del libro no existe
        if libro.isbn not in self.libros:
            # Si no existe lo agrega a la biblioteca
            self.libros[libro.isbn] = libro
            print(f"Libro agregado con exito : {libro}")
        else:
            print(" El libro ya existe en la biblioteca.")
    # Usamos el metodo para quitar libros de la biblioteca
    def quitar_libro(self, isbn):
    # Si el isbn del libro se encuentra en la biblioteca lo borra
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado de la biblioteca con exito: {eliminado}")
        else:
            print(" El libro no se encuentra en la biblioteca.")

    # metodo para registrar a los usuarios
    def registrar_usuario(self, usuario):
    # Revisa si el id de usurio ya existe en la biblioteca
        if usuario.user_id not in self.ids_registrados:
    # guarda al usuario en el diccionario usuarios añadiendo su id
            self.usuarios[usuario.user_id] = usuario
            self.ids_registrados.add(usuario.user_id)
            print(f"Usuario registrado exitosamente: {usuario}")
        else:
            print("El ID de usuario ya existe.")
    # metodo para dar de baja a un usuario
    def dar_baja_usuario(self, user_id):
    # busca si el usurio existe
        if user_id in self.usuarios:
    # si el usuario existe lo elimina del diccionario y del conjunto
            eliminado = self.usuarios.pop(user_id)
            self.ids_registrados.remove(user_id)
            print(f"Usuario eliminado de la biblioteca: {eliminado}")
        else:
            print(" Usuario no encontrado.")

    # metodo que permite prestar los libros
    def prestar_libro(self, user_id, isbn):
        # el usuario debe estra registrado
        if user_id not in self.usuarios:
            print("El Usuario no se encuentra registrado.")
            return
        # si el isbn del libro no existe no se puede hacer el prestamo
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return
        # sacamos el libro del diccionario de la biblioteca
        libro = self.libros.pop(isbn)
        # añadimos el libro a la lista de libros prestados
        self.usuarios[user_id].libros_prestados.append(libro)
        print(f" El Libro : {libro.info[0]} fue prestado  a {self.usuarios[user_id].nombre}")
    # metodo para devolver un libro prestado
    def devolver_libro(self, user_id, isbn):
        # comprobamos que el usuario si existe
        if user_id not in self.usuarios:
            print("Usuario no se encuentra registrado.")
            return

        usuario = self.usuarios[user_id]
        for libro in usuario.libros_prestados:
            # encuentra el isbn del libro en la lista de libros prestados
            if libro.isbn == isbn:
            # quita el libro de la lista y lo devuelve a la lista de libros disponibles
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # vuelve a estar disponible
                print(f"Libro Devuelto a la Biblioteca: {libro.info[0]} por el {usuario.nombre}")
                return
        print(" El usuario no tiene este libro en préstamo.")

    # metodo para buscar un libro por titulo
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]
        return resultados
    # metodo para buscar un libro por autor
    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]
        return resultados
    # metodo para buscar un libro por categoria
    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # metodo para ver que libros dispone el usuario
    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no se encuentra registrado.")
            return
        usuario = self.usuarios[user_id]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"   - {libro}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


if __name__ == "__main__":
# creamos una biblioteca vacia
    biblioteca = Biblioteca()

# creamos 3 libros
    libro1 = Libro("El señor de los Anillos", "J.J.R Tolkien", "Fantasia", "13345")
    libro2 = Libro("El Codigo Da Vinci", "Dan Brown", "Misterio", "67890")
    libro3 = Libro("La sombra del Viento", "Carlos Luis Zafon", "Ficcion", "54321")

# añadimos los libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

# creamos a 2 usuarios
    usuario1 = Usuario("Luis Perez", "1256")
    usuario2 = Usuario("Maria Lopez", "2589")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

# asumimos que los dos usuarios acceden a dos liros de la biblioteca
    biblioteca.prestar_libro("1256", "13345")
    biblioteca.prestar_libro("2589", "67890")

# se enlistan los libros que pidio cada uno
    biblioteca.listar_libros_prestados("1256")
    biblioteca.listar_libros_prestados("2589")
# asumimos que un usuario devuelve el libro
    biblioteca.devolver_libro("1256", "13345")

# cuando busquemos un libro po autor
    print("\n Búsqueda por autor 'Dan Brown':")
    resultados = biblioteca.buscar_por_autor("Dan Brown")
    for libro in resultados:
        print(libro)