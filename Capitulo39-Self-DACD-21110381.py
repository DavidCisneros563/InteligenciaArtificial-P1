#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Jugadores:
    def __init__(Jugador, nombre, posicion):
        Jugador.nombre = nombre
        Jugador.posicion = posicion

    def muestradatos(datos):
        print("El nombre del jugador es: " + datos.nombre, datos.posicion)

jugador1 = Jugadores("Chicharito", "Delantero")
jugador1.muestradatos()

jugador1.posicion = "Falso '9'"
jugador1.muestradatos()
        