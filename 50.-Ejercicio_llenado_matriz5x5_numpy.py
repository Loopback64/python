# Llenado de matriz de 5x5 versión 1  usando numpy
#
#



import numpy as np

matriz1 = np.zeros((5,5))
print("\nmatriz1:")
print(matriz1)


print("\nmatriz1:")

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
            print(int(matriz1[i][j]), end=" ")

    print() 


