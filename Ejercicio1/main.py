import paciente
import ips
import cola


def main():

    pacientes = cola.Cola()#Cola inicial de clientes

    #clientes que llegan a la recepcion
    pacientes.encolar(paciente.Paciente("Rodrigo", "Medicina General"))
    pacientes.encolar(paciente.Paciente("Mauricio", "Odontologia"))
    pacientes.encolar(paciente.Paciente("Yulean", "Cardiologia"))
    pacientes.encolar(paciente.Paciente("Orlando", "Medicina General"))
    
    #Inicia el proceso de atencion a esa lista de clientes
    myIps=ips.Ips(pacientes)
    myIps.atender_clientes()
    myIps.atender_en_sala()#Atiende a los clientes que se encuentran en la Sala.

main()