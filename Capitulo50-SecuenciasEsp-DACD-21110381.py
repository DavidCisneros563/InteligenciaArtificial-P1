#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import re

texto = "Arriba las poderosisimas chivas rayadas del Guadalajara"

resultado = re.findall("[a-p]" , texto)

print(resultado)