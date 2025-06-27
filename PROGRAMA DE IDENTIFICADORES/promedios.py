#ejemplo de identificadores para calcular el promedio de estudiantes
# el programa calcula el promedio final de 3 estudiantes y nos indica si aprobo o reprobo de año
# y la categoria en la que se encuentran segun su promedio

# creamos la clase estudiante
class estudiante:
# identificador que indica el numero de estudiantes
    numero_estudiantes = 3
    print(f"NUMERO DE ESTUDIANTES {numero_estudiantes} ")
# definimos los atributos de la clase estudiante
    def __init__(self, nombre,curso,nota1,nota2,nota3):
        self.nombre=nombre
        self.curso=curso
        self.nota1=nota1
        self.nota2 = nota2
        self.nota3 = nota3
    #identificador para calcular el promedio
    def Calcular_promedio(self):
        promedio=(self.nota1+self.nota2+self.nota3)/3
        return promedio
    #identificador para una funcion que indica si el estudiante pasa de año o no
    def Pase_deaño(self):
        promedio=self.Calcular_promedio()
        if promedio>7:
            return "APROBADO"
        else:
            return "REPROBADO"
    # identificador para la funcion que muestra la categoria donde se encuentra el estudiante
    def Categoria_Estudiante(self):
        promedio = self.Calcular_promedio()
        if promedio >= 9:
            return "EXELENTE"
        elif promedio>=7<9:
            return "MUY BUENO"
        else:
            return "REGULAR"

# instancias de la clase estudiante

estudiante1=estudiante("Juan","primero BGU", 7.25,6.25,5.25)
estudiante2=estudiante("Maria","segundo de BGU", 7.25,7.85,7.25)
estudiante3=estudiante("David","tercero de BGU", 9.25,9.25,9.25)

# Uso de los identificadores en un contexto de código

print(f'El estudiante {estudiante1.nombre} de {estudiante1.curso} tiene un promedio de: {estudiante.Calcular_promedio(estudiante1):.2f} por lo tanto ha {estudiante.Pase_deaño(estudiante1)} el año')
print(f'EL ESTUDIANTE {estudiante1.nombre} SE ENCUENTRA EN LA CATEGORIA {estudiante.Categoria_Estudiante(estudiante1)}')
print(f'El estudiante {estudiante2.nombre} de {estudiante2.curso} tiene un promedio de: {estudiante.Calcular_promedio(estudiante2):.2f} por lo tanto ha {estudiante.Pase_deaño(estudiante2)} el año')
print(f'EL ESTUDIANTE {estudiante2.nombre} SE ENCUENTRA EN LA CATEGORIA {estudiante.Categoria_Estudiante(estudiante2)}')
print(f'El estudiante {estudiante3.nombre} de {estudiante3.curso} tiene un promedio de: {estudiante.Calcular_promedio(estudiante3):.2f} por lo tanto ha {estudiante.Pase_deaño(estudiante3)} el año')
print(f'EL ESTUDIANTE {estudiante3.nombre} SE ENCUENTRA EN LA CATEGORIA {estudiante.Categoria_Estudiante(estudiante3)}')