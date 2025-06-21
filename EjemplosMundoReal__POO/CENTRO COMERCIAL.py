# el programa representa los centros comerciales de quito sus caracteristicas y encargados de cada uno de ellos
class centro_comercial: # definimos la clase principal que es centro comercial
    def __init__(self,nombre,ubicacion,almacenes):#iniciamos nuestro constructor
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.almacenes=almacenes

    def asignar_encargado (self,persona):#definimos el metodo
        if isinstance(persona, Persona):
            self.encargado=persona
    def __str__(self):
        return f'CENTRO COMERCIAL {self.nombre} ubicado en {self.ubicacion} con {self.almacenes} dirigido por {self.encargado.nombre2}.'

class Persona:#construimos la clase persona
    def __init__(self,nombre2,profesion):#le damos caracteristicas
        self.nombre2=nombre2
        self.profesion=profesion
    def __str__(self):
        return f'Persona {self.nombre2} con profesion {self.profesion}.'
#creamos los objetos para nuestra clase
centro_comercial1=centro_comercial('CONDADO SHOPPING','NORTE DE QUITO','47 alamcenes')
centro_comercial2=centro_comercial('EL RECREO','SUR DE QUITO','50 almacenes')
centro_comercial3=centro_comercial('PORTAL SHOPPING','NORTE DE QUITO','65 almacenes')
#asignamos un encargado para cada centro comercial y su profesion
persona1=Persona('JUAN','INGENIERO EN SISTEMAS')
persona2=Persona('MARIA','ADMINISTRADORA DE EMEPRESAS')
persona3=Persona('DAVID','INGENIERO EN MARKETING')
#imprimimos
centro_comercial1.asignar_encargado(persona1)
centro_comercial2.asignar_encargado(persona2)
centro_comercial3.asignar_encargado(persona3)
print(centro_comercial1)
print(centro_comercial2)
print(centro_comercial3)
print(persona1)
print(persona2)
print(persona3)