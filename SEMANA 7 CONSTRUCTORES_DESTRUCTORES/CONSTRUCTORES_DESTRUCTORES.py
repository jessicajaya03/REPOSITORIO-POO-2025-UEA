# Creamos un programa que muestre la informacion de un Cine con dos peliculas disponibles
# Usaremos constructores y destructores
# Creamos la clase pelicula
class pelicula:
# Utilizamos el constructor __init__ para inicializar los atributos de la clase pelicula
    def __init__(self, titulo,genero,autor):
        self.titulo=titulo
        self.genero=genero
        self.autor=autor
        print(f"Se ha crado un objeto pelicula con titulo {titulo}, genero {genero} y autor {autor}")
# Utilizamos el destructor __del__para realizar la limpieza de recursos
    def __del__(self):
        print(f"Se ha destruido el objeto Pelicula con titulo {self.titulo}")
# Usamos un metodo que nos muestre la informacion de las peliculas disponibles
    def mostrar_informacion(self):
        print(f"Titulo : {self.titulo}")
        print(f"Genero : {self.genero}")
        print(f"Autor  : {self.autor}")
# Creamos la clase cine
class cine:
# Utilizamos el constructor __init__ para inicializar los atributos de la clase cine
    def __init__(self,nombre,capacidad,salas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.salas = salas
        print(f"Se ha crado un objeto cine con nombre: {nombre},capacidad para {capacidad} personas con {salas} salas")
# Utilizamos el destructor __del__para realizar la limpieza de recursos
    def __del__(self):
        print(f"Se ha destruido el objeto Cine con nombre {self.nombre}")
# Usamos un metodo para mostrar la informacion del Cine
    def mostrar_informacion(self):
        print(f"Nombre : {self.nombre}")
        print(f"Capacidad : {self.capacidad}")
        print(f"Salas  : {self.salas}")

# Creamos nuestros objetos

Cine=cine("Multicines",200,5)
pelicula1=pelicula("Avatar","Accion","James Cameron")
pelicula2=pelicula("Transformers","Accion","Michaell Bay")

# Mostramos la informacion de las peliculas disponibles

Cine.mostrar_informacion()
print("PELICULAS DISPONIBLES EN CARTELERA")
pelicula1.mostrar_informacion()
print()
pelicula2.mostrar_informacion()

# Eliminamos objetos

del cine
del pelicula1
del pelicula2


