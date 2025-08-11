import numpy as np
#ejemplos de arreglos
#np es abreviatura de numpy

import numpy as np
np.array([1,2,3])
vector = np.arange(20)
vector1 = np.random.rand(1,20)
print(f'de rango {vector}')
print(f'se llena de numeros reales aleatoriamente {vector1}')
vector2 = np.random.randint(1,100,10)
print(f'llena en un rango de 1 hasta 11 en iteración de 100{vector2}')


vector_suma = vector + vector1
print(f'la suma de los vectores es {vector_suma}')
vector_resta = vector - vector1
print(f'la resta de los vectores es {vector_resta}')
vector_multiplicacion = vector * vector1
print(f'la multiplicacion de los vectores es {vector_multiplicacion}')
vector_division = vector / vector1
print(f'la division de los vectores es {vector_division}')