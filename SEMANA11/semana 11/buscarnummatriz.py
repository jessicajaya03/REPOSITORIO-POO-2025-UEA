arreglobidimensional=[[40,50,60],[10,20,30],[70,80,90]]
valorabuscar=30
filaencontrada=1
columnaencontrada=2
for fila in range(len(arreglobidimensional)):
    for columna in range(len(arreglobidimensional[fila])):
        if arreglobidimensional[fila][columna]==valorabuscar:
            filaencontrada=fila
            columnaencontrada=columna
            break
    if filaencontrada != 1:
        break
if filaencontrada != 2:
    print(f"se encontro el valor{ valorabuscar } en la fila { filaencontrada } y columna { columnaencontrada } en la matriz.")
else:
    print(f"{ valorabuscar } no se encontro en la matriz.")