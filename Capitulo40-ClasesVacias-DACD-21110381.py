#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Jugadores:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def muestradatos(self):
        print("El nombre del jugador y su posicion es: " + self.nombre,self.posicion)
 
jugador1 = Jugadores ("Chicharito", "Delantero")

print(jugador1.nombre, jugador1.posicion)

del jugador1.posicion

print(jugador1.nombre, jugador1.posicion)
        