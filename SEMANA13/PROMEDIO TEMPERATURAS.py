
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

def calcular_promedio_temperatura(matriz3D):
    ciudades=len(matriz3D)
    semanas =len(matriz3D[0])
    dias=len(matriz3D[0][0])
    promedios=[]


    for i in range(ciudades):
        for j in range(semanas):
            for k in range(dias):
                suma_temperaturas = sum(matriz3D[i][j][k])
                promedio=suma_temperaturas/(semanas*dias)
                promedios.append(promedio)
                return promedios












