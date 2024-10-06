#operaciones de lectura y escritura en archivos de texto Phyton
#PRIMERO CREAMOS UN ARCHIVO LLAMADO my_notes.txt
# DONDE GUARDAREMOS LAS NOTAS RESPECTO A LA MATERIA DE PROGRAMACION
#abrimos nuestro archivo en modo escritura
archivo=open("my_notes.txt","w")
#ESCRIBIMOS 3 LINEAS DE NOTAS PERSONALES
notas=[
    "NOTA 1: REALIZAR LOS DEBERES DE PROGRAMACION.\n",
    "NOTA 2: REAKIZAR LA EVALUCION DE PROGRAMACION.\n",
    "NOTA 3: REALIZAR EL PRACTICO EXPERIMENTAL.\n"

]
#USAMOS EL METDDO WRITELINES() PARA ESCRIBIR UNA LISTA DE LINEA
archivo.writelines(notas)
#CERRAMOS EL ARCHIVO DE ESCRITURA
archivo.close()
#IMPRIMIMOS EL TITULO DE LAS NOTAS
print("NOTAS DE LA MATERIA DE PROGRAMACION")
print("----------------")
#USAMOS EL METODO DE APERTURA r para lectura
#abrimos el archivo que creamos
archivo=open("my_notes.txt","r")
# leemos el contenido
linea=archivo.readline()
#usamos while para leer linea a linea el contenido del archivo
while linea:
    print(linea.strip())
    linea=archivo.readline()
archivo.close()#cerramos el archivos despues de leer
