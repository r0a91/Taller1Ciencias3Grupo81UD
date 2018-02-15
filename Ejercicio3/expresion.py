import cola
import pila

class Expresion:

    def __init__(self, cadena):
        self.cadena = cadena
        self.pila = pila.Pila()
        self.expre = cola.Cola()
    
    def string_to_cola(self):
        print("La cadena es: ")
        print(self.cadena)
        for char in self.cadena:
            #print(char)
            self.expre.encolar(char)
    
    def comprobar_expre(self):
        
        if self.expre.es_vacia():
            print("No hay mas elementos en la expresion")

        else:
            print(self.expre.desencolar())
            self.comprobar_expre()

        
    
    def operar(self):
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
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b+a
        self.pila.apilar(r)
    
    def realizarResta(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b-a
        self.pila.apilar(r)

    def realizarProducto(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b*a
        self.pila.apilar(r)

    def realizarDivision(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        r = b/a
        self.pila.apilar(r)
    

    def realizar_operacion(self):
        self.string_to_cola()
        #self.comprobar_expre()
        self.operar()
        if len(self.pila.items) == 1:
            print ('El valor de la operacion es: ' + str(self.pila.desapilar()))
        else:
            print ("El usuario ingreso una expresion erronea") 







        
            

            