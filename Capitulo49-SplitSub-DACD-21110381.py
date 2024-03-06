#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import re

texto = "Arriba las poderosisimas chivas rayadas del Guadalajara"

resultado = re.sub(" " , "---" ,texto, 4)

print(resultado)