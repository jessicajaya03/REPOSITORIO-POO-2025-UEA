#VAMOS A CREAR UNA FUNCION QUE CALCULE EL PRECIO Y DESCUENTO EL USUARIO
#COLOCA EL PRECIO DEL PRODUCTO Y EL DESCUENTO QUE QUIERA
#DEFINIMOS NUESTRA FUNCION con los parametros a calcular
def calcular_descuento (monto_total,porcentaje_descuento):
    descuento=monto_total-(monto_total*porcentaje_descuento/100)
    return descuento
#inicializamos nuestra variable en cero
total=0
#pedimos al usuario que coloque el valor total de compra
numero=input("INGRESE EL MONTO TOTAL DE LA COMPRA: $")
#usamos el condicional if para que en caso de que numero sea vacio
#nos vuelva a pedir nuevamente el numero
if numero=="":
     print("INGRESE EL VALOR DEL PRODUCTO")
else:#si la condicion 1 se cumple pedimos al usuario que ingrese el porcentaje de descuento
    numero1=input("INGRESE EL PORCENTAJE DE DESCUENTO: %")
    #usamos nuevamente un condicional para asegurarnos que la respuesta no sea vacio
    if numero1=="":
          print("INGRESE EL VALOR DEL PRODUCTO")
    else:# aqui procedemos a llamar a la funcion ya que tenemos los dos datos
        #el precio final representa a la funcion con las variables de tipo flotante
     preciofinal=calcular_descuento(float(numero),float(numero1))
#imprimimos el precio nnrmal con el  precio final  con descuento
print(f"EL PRECIO DEL PRODUCTO ES: {numero}$ CON SU DESCUENTO ES:{preciofinal: .2f}$")

