import cola
import pila

class Expresion:
    """Clase encargada de traducir y operar la expresion postfija """
    def __init__(self, cadena):
        self.cadena = cadena
        self.pila = pila.Pila()
        self.expre = cola.Cola()
    
    def string_to_cola(self):
        #Separa la cadena por espacios y lo agrega a una cola
        print("La cadena es: ")
        print(self.cadena)
        elementos_cadena=self.cadena.split()

        for elemento in elementos_cadena:
            self.expre.encolar(elemento)
        
    
    def comprobar_expre(self):
        #Comprueba si los elementos en la cola quedaron guardados de manera correcta
        if self.expre.es_vacia():
            print("No hay mas elementos en la expresion")

        else:
            print(self.expre.desencolar())
            self.comprobar_expre()

        
    
    def operar(self):
        """Una vez se tenga la expresion en la cola se empieza a realizar las operaciones
        mediante una pila, en donde si el elemento a agregar a la pila es un numero, se apila
        si es un operador se hace la respectiva operacion y el resultado se apila. Al final el elemento
        que quede en la pila es el resultado final"""

        if self.expre.es_vacia() :
            print("Operacion terminada")
        else:
            dato = self.expre.desencolar()
            if (dato == '+' or dato == '-' or dato == '*' or dato == '/'):
                if dato == '+':
                    self.realizarSuma()
                elif dato == '-':
                    self.realizarResta()
                elif dato == '*':
                    self.realizarProducto()
                elif dato == '/':
                    self.realizarDivision()
            else:
                self.pila.apilar(float(dato))
            self.operar()



    def realizarSuma(self):
        #Si el operador es + se realiza una suma
        #Y el resultado se apila
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b+a
        self.pila.apilar(r)
    
    def realizarResta(self):
        #Si el operador es - se realiza una resta
        #Y el resultado se apila
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b-a
        self.pila.apilar(r)

    def realizarProducto(self):
        #Si el operador es * se realiza una multiplicacion
        #Y el resultado se apila
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b*a
        self.pila.apilar(r)

    def realizarDivision(self):
        #Si el operador es / se realiza una division
        #Y el resultado se apila
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b/a
        self.pila.apilar(r)
    

    def realizar_operacion(self):
        #Interface que llama a los metodos que realizan las operaciones de conversion y operacion de la expresion

        #Convierte la expresion string dada en una cola
        self.string_to_cola()
        #self.comprobar_expre()


        #Opera una vez se haya convertido la expresion a una cola
        # Si la longitud final de la cola es de 1, ese es el valor
        # Si la longitud final de la cola es diferente de 1 es probable que el usuario haya ingresado una expresion erronea
        self.operar()
        if len(self.pila.items) == 1:
            print ('El valor de la operacion es: ' + str(self.pila.desapilar()))
        else:
            print ("El usuario ingreso una expresion erronea") 







        
            

            