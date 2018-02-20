import pila

class Almacen:
    def __init__(self, peliculas):
        self.peliculas= peliculas

    def buscar_peliculas_por_genero(self,busqueda):        
        #se empieza a buscar el genero entre el almacen de peliculas
        if self.peliculas.es_vacia():
            print ("No hay mas peliculas para mostrar.")
            print ("_______________________________________________")
        else:           

            pelicula=self.peliculas.desapilar()#obtiene la primera pelicula de toda la pila            
            
            for genero in pelicula.genero:                
                if busqueda==genero:
                    print(pelicula.titulo)            

            self.buscar_peliculas_por_genero(busqueda)# llama recursivamente a la funcion para seguir buscando peliculas
        
