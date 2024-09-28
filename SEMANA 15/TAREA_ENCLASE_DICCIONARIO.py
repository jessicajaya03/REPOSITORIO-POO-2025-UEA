
i=0
while True:
    NOMBRE_LIBRO = input("INGRESE EL NOMBRE DEL LIBRO:")
    CATEGORIA = input("INGRESE LA CATEGORIA:")
    AÑO_DE_PUBLICACION = input("SELECCIONE EL AÑO DE PUBLICACION DEL LIBRO:")
    NUMERO_DE_HOJAS = input("INGRESE EL NUMERO DE HOJAS DEL LIBRO:")
    AUTOR = input("INGRESE EL NOMBRE DEL AUTOR:")
    libros = [{"NOMBRE DEL LIBRO": NOMBRE_LIBRO, "CATEGORIA": CATEGORIA, "AÑO DE PUBLICACION": AÑO_DE_PUBLICACION,
               "NUMERO DE HOJAS": NUMERO_DE_HOJAS, "AUTOR": AUTOR}

              ]
    respuesta=input("¿DESEA CONTINUAR AGREGANDO MAS LIBROS ESCRIBA SI O NO? ")
    if respuesta!="si":
        break
print("lista de libros")
for i in range(len(libros)):
    print(libros[0]["NOMBRE DEL LIBRO"])
    print(libros[0]["CATEGORIA"])
    print(libros[0]["AÑO DE PUBLICACION"])
    print(libros[0]["NUMERO DE HOJAS"])
    print(libros[0]["AUTOR"])