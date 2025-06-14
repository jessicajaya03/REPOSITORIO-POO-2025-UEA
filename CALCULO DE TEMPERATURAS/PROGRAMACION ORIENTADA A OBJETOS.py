#A TRAVEZ DE TECNICAS DE PROGRAMACION COMO HERENCIA Y POLIMORFISMO VAMOS A CALCULAR EL PROMEDIO SEMANAL
#DE TEMPERATURAS DE 3 CIUDADES
#SE APLICA LA TECNICA DE POLIMORFISMO YA QUE LAS 3 CLASES OBTIENEN RESULTADOS DISTINTOS
#PERO USAN LOS MISMOS METODOS PARA EL CALCULO DE SUS PROMEDIOS
#SE APLICA LA TECNICA DE HERENCIA YA QUE LAS CLASES HEREDAN LOS MISMOS METODOS QUE LAS ANTERIORES
class temperaturas:#DEFINIMOS NUESTRA CLASE TEMPERATURA
    def __init__(self,ciudad):#USAMOS EL METODO CONSTRUCTOR
        self.ciudad=ciudad
    def calcular_promedio1(self):#DEFINIMOS EL METODO QUE NOS AYUDA A CALCULAR EL PROMEDIO
        pass
    def calcular_promedio2(self):#DEFINIMOS EL METODO PARA LA SEMANA2
        pass
    def calcular_promedio3(self):#DEFINIMOS EL METODO PARA LA SEMANA3
        pass
    def calcular_promedio4(self):#DEFINIMOS EL METODO PARA LA SEMANA4
        pass
class temciudad1(temperaturas):#CREAMOS UNA NUEVA CLASE que clacula las temperaturas dela ciudad 1
    def __init__(self,ciudad,semana1,semana2,semana3,semana4):
        super().__init__(ciudad)#llamamos al constructor de la clase base
        self.semana1 = semana1#asignamosparametros para las semanas
        self.semana2 = semana2
        self.semana3 = semana3
        self.semana4 = semana4
    def calcular_promedio1(self):#usamos este metodo para calcular le promedio de la semana 1
        return round(sum(self.semana1)/len(self.semana1),2)
    def calcular_promedio2(self):
        return round(sum(self.semana2)/len(self.semana2),2)
    def calcular_promedio3(self):
        return round(sum(self.semana3)/len(self.semana3),2)
    def calcular_promedio4(self):
        return round(sum(self.semana4)/len(self.semana4),2)
class temciudad2(temperaturas):#creamos otra clase llamada ciudad 2
    def __init__(self,ciudad,semana1,semana2,semana3,semana4):
        super().__init__(ciudad)
        self.semana1 = semana1
        self.semana2 = semana2
        self.semana3 = semana3
        self.semana4 = semana4
    def calcular_promedio1(self):#calculamos los promedios para cada semana
        return round(sum(self.semana1)/len(self.semana1),2)
    def calcular_promedio2(self):
        return round(sum(self.semana2)/len(self.semana2),2)
    def calcular_promedio3(self):
        return round(sum(self.semana3)/len(self.semana3),2)
    def calcular_promedio4(self):
        return round(sum(self.semana4)/len(self.semana4),2)
class temciudad3(temperaturas):#DEFINIMOS LA CLASE PARA CALCULAR LAS TEMPERATUTRAS DE LA CIUDAD 3
    def __init__(self,ciudad,semana1,semana2,semana3,semana4):
        super().__init__(ciudad)
        self.semana1 = semana1
        self.semana2 = semana2
        self.semana3 = semana3
        self.semana4 = semana4
    def calcular_promedio1(self):
        return round(sum(self.semana1)/len(self.semana1),2)
    def calcular_promedio2(self):
        return round(sum(self.semana2)/len(self.semana2),2)
    def calcular_promedio3(self):
        return round(sum(self.semana3)/len(self.semana3),2)
    def calcular_promedio4(self):
        return round(sum(self.semana4)/len(self.semana4),2)

temciudad1=temciudad1("QUITO", [15, 27, 34, 29, 13, 23, 19], #CREAMOS LAS INSTANCIAS DE LA CLASE
                    [14, 23, 27, 12, 17, 25, 27],
                    [14, 23, 27, 12, 17, 25, 27],
                    [12, 24, 17, 18, 19, 25, 23])
temciudad2=temciudad2("GUAYAQUIL",[15,23,22,16,11,27,23],#INSTANCIAS DE LA CLASE
          [12,22,21,27,21,22,13],
          [17,18,22,26,13,18,21],
          [16,13,23,18,22,18,23])
temciudad3=temciudad3("CUENCA",[12,27,12,27,12,19,23],#INSTANCIAS DE LA CLASE
        [16,13,18,23,22,19,23],
        [22,21,16,18,21,19,25],
        [21,18,15,19,22,24,13])
print("PROMEDIO DE LA CIUDAD DE QUITO POR CADA SEMANA")
print(f" semana1 es {temciudad1.calcular_promedio1()}°")#IMPRIMIMOS EL PROMEDIO SEMANAL DE CADA CIUDAD
print(f" semana2 es {temciudad1.calcular_promedio2()}°")
print(f" semana3 es {temciudad1.calcular_promedio3()}°")
print(f" semana4 es {temciudad1.calcular_promedio4()}°")
print("PROMEDIO DE LA CIUDAD DE GUAYAQUIL POR CADA SEMANA")
print(f" semana1 es {temciudad2.calcular_promedio1()}°")
print(f" semana2 es {temciudad2.calcular_promedio2()}°")
print(f" semana3 es {temciudad2.calcular_promedio3()}°")
print(f" semana4 es {temciudad2.calcular_promedio4()}°")
print("PROMEDIO DE LA CIUDAD DE CUENCA POR CADA SEMANA")
print(f" semana1 es {temciudad3.calcular_promedio1()}°")
print(f" semana2 es {temciudad3.calcular_promedio2()}°")
print(f" semana3 es {temciudad3.calcular_promedio3()}°")
print(f" semana4 es {temciudad3.calcular_promedio4()}°")


