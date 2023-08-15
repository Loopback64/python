# Escriba un programa que permita visualizar una matriz cuadrada de cinco por cinco, con los
# valores tal como se muestran en la figura a continuación.

"""  Para estos ejercicios usaremos código con el uso de las bibliotecas, estándar de Python y Numpy."""

matriz1 = [  [0,0,0,0,0] , [ 0,0,0,0,0] , [0,0,0,0,0], [0,0,0,0,0] , [0,0,0,0,0] ] 

print("\nmatriz1:  " )

print(matriz1)

print("\nmatriz1: ")

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j], end=" ")
    print()

