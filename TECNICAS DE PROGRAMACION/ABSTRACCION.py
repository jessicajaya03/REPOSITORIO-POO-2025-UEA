#CREAREMOS LA CLASE CINE QUE MOSTRATA INFORMACION DEL MISMO
#LA TECNICA DE ABSTRACCION NOS PERMITE MOSTRAR, MODIFICAR
#MEDIANTE EL USO DE METODOS
class cine:# PRIMERO CREAMOS LA CLASE CINE
    def __init__(self, nombre, ubicacion,peliculas,costo,atencion):#colocamos los atributos para inicializar elobjeto
        self.nombre=nombre # implementamos el metodo constructor
        self.ubicacion=ubicacion
        self.peliculas=peliculas
        self.costo=costo
        self.atencion=atencion

    def atributos(self):  # escribimos una funcion que nos muestra los atributos y self para tener acceso a ellos
        print(self.nombre, ":", sep="")
        print("ESTA UBICADO EN:", self.ubicacion)
        print("CUENTA CON LAS SIGUIENTES PELICULAS:", self.peliculas)
        print("EL COSTO DE CADA UNA ES:", self.costo)
        print("HORA DE ATENCION:", self.atencion)
    def cine_sucursal (self,nombre,ubicacion,peliculas ,costo,atencion):#DEFINIMOS NUEVOS METODOS
        self.nombre = nombre  # implementamos el metodo constructor
        self.ubicacion = ubicacion
        self.peliculas = peliculas
        self.costo = costo
        self.atencion = atencion
    def ver_peliculas(self,peliculas):
        self.peliculas=peliculas
    def hora_atencion(self,atencion):
        self.atencion=atencion
        if self.atencion==("8:00am-16:00pm"):
            print("EL CINE ESTA ABIERTO")
        else:
            print("esta cerrado")
#creamos las instancias de la clase cine
cine=cine("CINEPLUS", "QUITO","ACCION DRAMA TERROR COMEDIA","5$","LUNES A SABADOS")
cine.hora_atencion("8:00am-16:00pm")
cine.atributos()
#creamos instancias donde podemos modifical los atributos y cambiarlos
cine.cine_sucursal("CINEPLUS","GUAYAQUIL", "ACCION ANIMADA COMEDIA ROMANTICA","6$","LUNES A SABADO")
cine.hora_atencion("8:00am-16:00pm")
cine.atributos()
