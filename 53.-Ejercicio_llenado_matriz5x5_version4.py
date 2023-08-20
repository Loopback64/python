#  
#
#


import numpy as np

matriz4 = np.zeros((5,5))

print("\nmatriz4:")

print(matriz4)

print("\nmatriz4:")


for i in range(len(matriz4)):
    for j in range(len(matriz4[i])):
        if(j == 4-i):
            matriz4[i][j] = 1;
        print(int(matriz4[i][j]), end= " ")

    print() 









