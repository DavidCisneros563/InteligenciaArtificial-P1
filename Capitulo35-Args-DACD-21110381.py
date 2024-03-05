#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

def ChivEqp ( DT, Sustituos, *args):
    print("DT: " + DT)
    print("Sustitutos: " + Sustituos)
    for x in args:
        print("Jugadores: " + x)

ListJug = ["Chicharito", "JJ Macias", "Erick Gutierrez", "Pocho Guzman"]

ChivEqp("Fernando Gago", "Ricardo Marín", *ListJug)
