# Usando Numpy
""" Se define una lista de elementos enteros y, mediante la biblioteca de Numpy, con el objeto np,
se utilizan los métodos o funciones disponibles para trabajar sobre la lista. """


import numpy as np
lista  = [4, 6 ,5 , 10 , 1, 9 ,8 , 3 , 7 , 2]

maximo = np.amax(lista)
minimo = np.amin(lista)
lista1 = np.sort(lista)

print("Lista: ", lista)
print("Valor Maximo: ",maximo)
print("Valor Minimo: ",minimo)

print("Ordenado; ", lista1)
print("Sumatoria: " , np.sum(lista) )



