#Este ejemplo vamos a calcular el promedio de dos estudiantes.
#aplicamos el polimorfismo los dos objetos en este caso estudiante1 y estudiante 2
#obtienen diferentes resultados pero usando el mismo metodo que es promedio final
class estudiante: #definimos la clase estudiante
    def __init__(self, nombre):# aplicamos el metodo constructor
        self.nombre=nombre
    def calcular_promedio(self):# definimos un metodo
        pass
class estudiante1(estudiante):# creamos la clase estudiante1 heredado de la clase estudiante
    def __init__(self,nombre,nota_examen,nota_tareas):
        super().__init__(nombre)#llamamos al constructor de la clase base
        self.nota_examen = nota_examen#asignamos nuevos parametros
        self.nota_tareas = nota_tareas
    def calcular_promedio(self):
        return (self.nota_examen + self.nota_tareas) / 2# calculamos el promedio
class estudiante2(estudiante):#creamos la clase estudiante2
    def __init__(self,nombre,nota_examen,nota_tareas):
        super().__init__(nombre)#llamamos al constructor de la clase base
        self.nota_examen = nota_examen
        self.nota_tareas = nota_tareas
    def calcular_promedio(self):#usamos nuevamente el metodo calcular promedio
        return (self.nota_examen + self.nota_tareas) / 2
estudiante1=estudiante1("David",9,8)#creamos instancias de las clases
estudiante2=estudiante2("Alejandro",10,9)
print(f"PROMEDIO FINAL DE {estudiante1.nombre}:{estudiante1.calcular_promedio()}")#calcula e imprime la nota final
print(f"PROMEDIO FINAL DE {estudiante2.nombre}:{estudiante2.calcular_promedio()}")#se llama dorma polimorfica al metodo calcular promedio