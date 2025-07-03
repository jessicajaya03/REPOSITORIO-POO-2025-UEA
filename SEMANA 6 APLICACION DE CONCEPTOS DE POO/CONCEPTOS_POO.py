#programa de una tienda que vende computadoras aplicando conceptos de POO
# definimos nuestra clase principal computadora
class computadora:
# usamos el metodo constructor para inicializar los atributos
    def __init__(self, marca,modelo,memoria,costo):
        self.marca=marca
        self.modelo=modelo
        self.memoria=memoria
        self.costo=costo
# usamos este metodo para aplicar polimorfismo en las clases heredadas
    def imprimir_informacion(self):
        pass
# aplicamos la herencia de la clase computadora
class laptop(computadora):
    def __init__(self,marca, modelo, memoria,costo,generacion):
# llamada al constructor de la clase
        super().__init__(marca,modelo,memoria,costo)
        self.generacion=generacion
# usamos el metodo imprimir informanformacion
    def imprimir_informacion(self):
        return f" LAPTOP {self.marca} modelo {self.modelo} de {self.memoria} RAM de {self.generacion}"
# aplicamos la herencia de la clase computadora
class computadora_escritorio(computadora):
    def __init__(self,marca, modelo, memoria,costo,procesador):
# llamamos al constructor de la clase padre
        super().__init__(marca,modelo,memoria,costo)
        self.procesador=procesador
# usamos el mismo metodo imprimir informacion pero con distintos resultados aqui aplicamos polimorfismo
    def imprimir_informacion(self):
       return f" COMPUTADORA DE ESCRITORIO {self.marca} modelo {self.modelo} de {self.memoria} RAM con procesador {self.procesador}"
# creamos una nueva clase para el comprador
class comprador:
# usamos el metodo constructor para inicializar los atributos de comprador
    def __init__(self, nombre,dinero):
        self.nombre=nombre
# aplicamos encapsulacion en el atributo dinero
        self.__dinero=dinero
# usamos el metodo get para acceder al valor del atributo dinero de forma controlada
    def get_dinero(self):
        return self.__dinero
# usamos el metodo set para modificar el valor del atributo dinero de forma controlada
    def set_dinero(self,dinero):
        self.__dinero=dinero
# usamos el metodo para poder comprar la computadora
    def comprar_computadora(self,computadora):
        if self.__dinero>=computadora.costo:
            cambio=self.__dinero-computadora.costo
            self.__dinero=cambio
# en esta linea de codigo llamamos al metodo imprimir informacion del objeto computadora
# que puede ser laptop o computadora de escritorio  aqui se aplica polimorfismo
            print(f"{self.nombre} compro la {computadora.imprimir_informacion()} por un costo de  {computadora.costo}$ y le sobro {cambio: .2f}$")
        else:
            print(f"{self.nombre} no tiene dinero para comprar la computadora")

# creamos los objetos de las clases
laptop=laptop("LENOVO","ideapad","16GB",800,"QUINTA GENERACION")
computadora_escritorio=computadora_escritorio("HP","HP All-In-One","8GB",589,"Intel Core i3",)
# instancias de la clase comprador
juan=comprador("juan",1500)
maria=comprador("maria",1600)
# llamamos al metodo comprar computadora de la clase comprador para cada instancia
juan.comprar_computadora(laptop)
maria.comprar_computadora(computadora_escritorio)