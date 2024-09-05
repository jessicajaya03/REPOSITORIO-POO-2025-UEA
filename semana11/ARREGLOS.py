#PROGRAMA PARA BUSCAR UN NUMERO DE LA MATRIZ
#CREAMOS UNA MATRIZ 3X3 CON DIFERENTES VALORES
arreglobidimensional=[[40,50,60],[10,20,30],[70,80,90]]
#BUSCAMOS EL VALOR NUMERICO 30
valorabuscar=30
filaencontrada=1
columnaencontrada=2
#IMPLEMENTAMOS UN CONDICIONAL PARA LA BUSQUEDA DE LA MATRIZ
for fila in range(len(arreglobidimensional)):
    for columna in range(len(arreglobidimensional[fila])):
        if arreglobidimensional[fila][columna]==valorabuscar:
            filaencontrada=fila
            columnaencontrada=columna
            break
    if filaencontrada != 1:
        break
if filaencontrada != 2: #IMPRIMIMOS EL MESAJE SI LA MATRIZ SE ENCONTRO Y EN LA POSICION
    print(f"se encontro el valor { valorabuscar } en la fila { filaencontrada } y columna { columnaencontrada } en la matriz.")
else: # SI NO SE ENCUENTRA IMPRIMIMOS EL MENSAJE
    print(f"{ valorabuscar } no se encontro en la matriz.")