import cola
import dependencia

class Ips:
    def __init__(self, pacientes):
        self.pacientes= pacientes
        self.dependencias= []

    def atender_clientes(self):
        #comienza a atender a la cola de pacientes
        if self.pacientes.es_vacia():
            print ("No hay mas pacientes para atender en recepcion.")
            print ("_______________________________________________")
        else:
            #Si no existe la dependencia a la que va el cliente la crea y envia el paciente a esa dependencia

            paciente=self.pacientes.desencolar()#obtiene el 1er paciente de la lista de pacientes
            print("atendiendo en recepcion a " + paciente.nombre)
            if not self.existe_dependencia(paciente):#comprueba si existe la dependencia, sino lo agrega
                self.agregar_dependencia(paciente.destino)
            
            for dependencia in self.dependencias:#agrega el paciente a su respectiva dependencia
                if dependencia.nombre == paciente.destino:
                    dependencia.agregar_a_sala(paciente)
            
            self.atender_clientes()# llama recursivamente a la funcion para atender a los clientes que siguen en cola.
        
        
        

        

    def atender_en_sala(self):# Se encarga de hacer el procedimiento interno de atencion para cada dependencia.
        for dependencia in self.dependencias:
            dependencia.atender_pacientes()
            print("--")
        
        


    def agregar_dependencia(self, nombre_dependencia):#Agrega una dependencia a la lista de dependencias.
        self.dependencias.append(dependencia.Dependencia(nombre_dependencia))

    def existe_dependencia(self, paciente):
        #Comprueba si existe o no la dependencia
        existe=False
        for dependencia in self.dependencias:
            if dependencia.nombre == paciente.destino:
                existe=True
        
        return existe

    
