#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Jugadores:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
    
    def muestraDatos(self):
        print("El nombre del jugador es: " + self.nombre, "Y juega de: ", self.posicion)

jugador1 = Jugadores("Chicharito", "Delantero")

jugador1.muestraDatos()

class Jugador_Titular(Jugadores):
    pass

Jugador2 = Jugador_Titular("Ricardo Marín", "Delantero")

Jugador2.muestraDatos()

        