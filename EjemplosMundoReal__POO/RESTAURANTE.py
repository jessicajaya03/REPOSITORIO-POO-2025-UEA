#creamos un programa que nos muestre el precio de los combos y su valor total
class restaurante:#creamos la clase restaurante
    def __init__(self,combo1,combo2,combo3):#definimos el constructor
        self.combo1=combo1
        self.combo2 = combo2
        self.combo3 = combo3
        self.total=0
    #definimos el precio de cada combo
    def precio_combo1 (self):
        self.total += self.combo1
        print(f'EL COMBO 1 PAPAS + POLLO CUESTA {self.total} $.')
    def precio_combo2 (self):
        self.total = self.combo2
        print(f'EL COMBO 2 HAMBURGUESA + POLLO CUESTA {self.total}$.')
    def precio_combo3 (self):
        self.total = self.combo3
        print(f'EL COMBO 3 PIZZA + POLLO CUESTA {self.total}$.')
    #calculamos el valor total de los 3 combos
    def mostrar_total(self):
        return (self.combo1+self.combo2+self.combo3)

restaurante=restaurante(4,3,8)#creamos las instancias de la clase
restaurante.precio_combo1()
restaurante.precio_combo2()
restaurante.precio_combo3()
restaurante.mostrar_total()
print(f'EL PRECIO TOTAL ES:{restaurante.mostrar_total()}$')