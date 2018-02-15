import cola

class Dependencia:
    #clase que indica en donde se debe atender al paciente con su nombre y la sala de espera que es una cola de pacientes
    def __init__(self, nombre):
        self.nombre = nombre
        self.sala = cola.Cola()
    
    def atender_pacientes(self):
        if self.sala.es_vacia():
            pass
            #print('la sala de ' + self.nombre + ' esta vacia ')
        else:
            paciente=self.sala.desencolar()
            print('Se ha atendido al paciente ' + paciente.nombre + ' en ' + self.nombre)
            self.atender_pacientes()
            
    
    def agregar_a_sala(self, paciente):
        self.sala.encolar(paciente)