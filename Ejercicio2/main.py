import pelicula
import pila
import almacen


def main():

    peliculas = pila.Pila()#Pila de Peliculas en general

    #Peliculas actualmente almacenadas
    peliculas.apilar(pelicula.Pelicula("The Avengers", ['accion','aventura','ciencia ficcion']))
    peliculas.apilar(pelicula.Pelicula("Thor: Ragnarok", ['accion','aventura','comedia']))
    peliculas.apilar(pelicula.Pelicula("It (Eso)", ['terror','suspenso']))
    peliculas.apilar(pelicula.Pelicula("La naranja mecánica", ['drama']))
    peliculas.apilar(pelicula.Pelicula("El Padrino", ['drama','crimen','gangsters']))    
    
    #Parametro de busqueda por genero en la Pila de peliculas
    busqueda = 'drama' 

    print('A continuacion se muestran las peliculas que pertenecen al genero: '+busqueda)
    myAlmacen=almacen.Almacen(peliculas)  
    myAlmacen.buscar_peliculas_por_genero(busqueda)

main()


