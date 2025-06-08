#EN ESTE EJEMPLO VAMOS A MOSTRAR INFORMACION DE UNA UNIVERSIDAD CON TECNICA DE HERENCIA
#USAREMOS LA CLASE UNIVERSIDAD DONDE SUS CLASES HIJAS HEREDAN METODOS Y ATRIBUTOS DE LA CLASE MADRE
class universidad:# definimos la clase universidad
    def __init__(self,nombre,ubicacion):#usamos el metodo constructor
        self.nombre=nombre #definimos los atributos
        self.ubicacion=ubicacion

    def presentacion (self):#usamos un metodo para la presentacion
        print("EL NOMBRE DE LA UNIVERSIDAD ES:",self.nombre)
        print("ESTA UBICADA EN:", self.ubicacion)
class rector(universidad): #creamos una nueva case
    def __init__(self, nombre, ubicacion,nombre2):#agregamos nuevos atributos
        super().__init__(nombre,ubicacion)
        self.nombre2=nombre2
    def presentacion(self):
        super().presentacion()
        print("EL NOMBRE DEL RECTOR ES:", self.nombre2)
class estudiantes(rector):#esta nueva clase hereda los metodos y atrubtos
    def __init__(self, nombre, ubicacion,nombre2,total):#agregamos nuevos atributos
        super().__init__(nombre,ubicacion,nombre2)
        self.total=total
    def presentacion(self):
        super().presentacion()
        print("CUENTA CON:", self.total)
class maestros(estudiantes):#creamos otra clase que hereda los atributos de la anterior
    def __init__(self, nombre, ubicacion,nombre2,total,total2):
        super().__init__(nombre,ubicacion,nombre2,total)
        self.total2=total2
    def presentacion(self):
        super().presentacion()
        print("CUENTA CON:", self.total2)
class facultades(maestros):#creamos nueva clase heredando atributos y metodos de la anterior
    def __init__(self, nombre, ubicacion,nombre2,total,total2,total3):
        super().__init__(nombre,ubicacion,nombre2,total,total2)
        self.total3=total3
    def presentacion(self):
        super().presentacion()
        print("CUENTA CON:", self.total3)
#definimos las instancias
facultades=facultades("U QUITO","QUITO","JUAN LOPEZ","2000 ESTUDIANTES","200 INGENIEROS","15 FACULTADES")
facultades.presentacion()#imprime la presentacion
