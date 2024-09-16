# VAMOS A CREAR UNA FUNCION QUE CALCULE EL PROMEDIO DE  TEMPERATURAS
#USANDO FUNCIONES
#PRIMERO CREAMOS NUESTRA MATRIZ 3D DONDE SE ALMACENARA LAS TEMPERATURAS
#POR 4 SEMANAS CADA 1

QUITO=[[15,27,34,29,13,23,19],#semana1
       [14,23,27,12,17,25,27],#semana2
       [14,23,27,12,17,25,27],#semana3
       [12,24,17,18,19,25,23]]
GUAYAQUIL=[[15,23,22,16,11,27,23],#semana1
          [12,22,21,27,21,22,13],#semana2
          [17,18,22,26,13,18,21],#semana3
          [16,13,23,18,22,18,23]]#semana4
CUENCA=[[12,27,12,27,12,19,23],#semana1
        [16,13,18,23,22,19,23],#semana2
        [22,21,16,18,21,19,25],#semana3
        [21,18,15,19,22,24,13]]#semana4


temperaturas=[QUITO , GUAYAQUIL, CUENCA]
nombres_ciudades= ["QUITO","GUAYAQUIL","CUENCA"]
#DEFINIMOS NUESTRA FUNCION PARA CALCULAR EL PROMEDIO
def calcular_promedio_semana(semana):
    return sum(semana)/len(semana)
#DEFINIMOS LA FUNCION PARA CALCULAR LOS PROMEDIOS DE CADA CIUAD POR SEMANA
def calcular_promedios_semanales(ciudad):
    return [calcular_promedio_semana(semana) for semana in ciudad]
#DEFINIMOS LA FUNCION PARA CALCULAR LE PROMEDIO DE TEMPERATURAS
#SEMANALES POR CADA CIUDAD
def calcular_promedios_semanales_todas_ciudades(temperaturas):
    return [calcular_promedios_semanales(ciudad) for ciudad in temperaturas]
promedios_semanales_todas_ciudades=calcular_promedios_semanales_todas_ciudades(temperaturas)
#UTILIZAMOS EL BUCLE FOR PARA ACCEDER A LA LISTA QUE CONTIENE EL
#NOMBRE DE LAS CIUDADES
for i in range(len(nombres_ciudades)):
    #IMPRIMIMOS LAS CIUDADES
    print(f"{nombres_ciudades[i]} :")
    #USAMOS EL INDICE J QUE NOS INDICA LAS SEMANAS Y EL PROMEDIO
    #QUE VAMOS A CALCULAR DE CADA CIUDAD
    for j in range(len(promedios_semanales_todas_ciudades[i])):
        #IMPRIMIMOS LA SEMANA Y EL PROMEDIO
        print(f"Semana{j + 1}:PROMEDIO {promedios_semanales_todas_ciudades[i][j]:.2f}ª:")