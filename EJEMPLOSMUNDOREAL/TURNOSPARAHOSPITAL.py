#PROGRAMA PARA ESCOGER CITA MEDICA EN UN HOSPITAL
#definimos la clase turno
class turno:
    #inicializamos la clase
    def __init__(self):
        self.doctores=[]#creamos una lista que almacena la clase doctor
        self.turno=1#inicializamos la variable que asigna el numero de turnos
    def agregar_doctor(self,doctor):#definimos el metodo
        self.doctores.append(doctor)
    def escoger_turno(self,paciente,area):#definimos metodo para que se genere el turno
        for doctor in self.doctores: #utilizamos el bucle for para recorrer la lista de doctores
            if doctor.area==area: #usamos el condicional para que el area del doctor coincida con la seleccionada
                print(f'{paciente} agendo un turno con el Dr {doctor.nombre} en el area de {area} numero de turno {self.turno}')
                self.turno += 1#incrementa el numero de turnos
                return
        print(f"no existe doctor para el area seleccionada ")#si el area no coincide responde
#creamos la clase doctor
class doctor:
        def __init__(self,nombre,area):#inicializa la clase doctor
            self.nombre=nombre
            self.area=area
#creamos los objetos
Turno=turno()
Turno.agregar_doctor(doctor("luis Lopez","cardiologia"))
Turno.agregar_doctor(doctor("Jorge Perez","odontologia"))
Turno.escoger_turno("Dayana","cardiologia")
Turno.escoger_turno("Jose","odontologia")
Turno.escoger_turno("Juan","odontologia")
Turno.escoger_turno("Maria","medicina general")