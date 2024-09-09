#PRIMERO VAMOS A DEFINIR LAS CIUDADES SEMANAS Y DIAS
nombres_ciudades= ["QUITO","GUAYAQUIL","CUENCA"]
semana=["semana1","semana2","semana3","semana4"]
dias= ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
#CREAMOS UNA MATRIZ 3D QUE VA HA REPRESENTAR LAS TEMPERATURAS EN CADA DIA
matriz3D=[
    [#ciudad1 QUITO
        [15,27,34,29,13,23,19],#semana1
        [14,23,27,12,17,25,27],#semana2
        [14,23,27,12,17,25,27],#semana3
        [12,24,17,18,19,25,23]#semana4
    ],
    [  # ciudad2 GUAYAQUIL
        [15,23,22,16,11,27,23],#semana1
        [12,22,21,27,21,22,13],#semana2
        [17,18,22,26,13,18,21],#semana3
        [16,13,23,18,22,18,23]#semana4
    ],
    [
        # ciudad3 CUENCA
        [12,27,12,27,12,19,23],#semana1
        [16,13,18,23,22,19,23],#semana2
        [22,21,16,18,21,19,25],#semana3
        [21,18,15,19,22,24,13]#semana4
    ]
]
#USAMOS UN BUCLE FOR PARA IMPRIMIR LAS CIUDADES EN PANTALLA
#EL INDICE ES i DEBIDO A QUE SE ENCUENTRA EN LA PRIMERA DIMENSION
for i in range(len(nombres_ciudades)):
    print(f"{nombres_ciudades[i]} :")# PARA IMPRIMIR LAS CIUDADES
    # USAMOS EL BUCLE FOR PARA ITERAR LOS ELEMENTOS DE LA SEMANA
    for j in range(len(semana)):
        #REALAIZAMOS LA SUMA SE LAS TEMPERATURAS DE CADA CIUDAD POR CADA SEMANA
        #Y SACAMOS EL PROMEDIO DIVIDIENDO PARA LOS 7 DIAS DE LA SEMANA
            suma=sum(matriz3D[i][j])
            promedio=suma/len(dias)
            print(f"{semana[j]}:EL PROMEDIO DE TEMPERATURAS ES DE = {promedio}ºC ")
    #IMPRIMIMOS LAS 4 SEMANAS DE CADA CIUDAD CON SU PROMEDIO DE TEMPERATURAS POR CADA SEMANA







