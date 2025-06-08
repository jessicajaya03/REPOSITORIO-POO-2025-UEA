#VAMOS A CREAR UNA CLASE LLAMADA REGISTRO DONDE MOSTRAREMOS INFORMACION
# COMO EL NOMBRE CIUDAD CEDULA CUENTA Y CONTRASEÑA
#USAREMOS LA TECNICA DE ENCAPSULACION PARA OCULTAR DATOS PRIVADOS
#EL NUMERO DE CUENTA Y CONTRASEÑA
class registro:#CREAMOS LA CLASE LLAMADA REGISTRO
    def __init__(self, nombre, ciudad,cedula,cuenta,contraseña):#creamos el constructor
        self.nombre=nombre
        self.ciudad=ciudad
        self.cedula=cedula
        self.__cuenta=cuenta
        self.__contraseña=contraseña
    def get_cuenta (self):#usamos este metodo para encapsular el numero de cuenta
        return "........."
    def set_cuenta (self,cuenta):
        self.__cuenta=cuenta
    def get_contraseña (self):#encapsulamos la contraseña
        return "........."
    def set_cuenta (self,contraseña):
        self.__contraseña=contraseña

#definios las instancias de la clase registro
registro=registro("ANDREA","QUITO","1724569874","2541365","ABC256")
print("SE HA REGISTRADO EXITOSAMENTE")
print("SU NOMBRE ES:",registro.nombre)
print("CIUDAD DE RESIDENCIA:",registro.ciudad)
print("SU NUMERO DE CEDULA ES:",registro.cedula)
print("SU NUMERO DE CUENTA:",registro.get_cuenta())
print("SU CONTRASEÑA ES:",registro.get_cuenta())
