# Escriba un programa que permita almacenar los diez primeros números en un arreglo.
# usando tuplas

""" Se definen dos tuplas, una de diez elementos y otra de tres elementos. """


tupla1 = (1,2,3,4,5,6,7,8,9,10)
tupla2 = "192.168.1.1" , "IP" , "red"
print("Toda la tupla 1: ")
print(tupla1)
print("Elementos de la tupla2: ")

for i in tupla2:
    print(i, end=" ")

print()
print("Usando range..")
print("Indices de la tupla 1: ")

for i in range(len(tupla1)):
    print(i,end=" ")

print()
print("Contenido en tupla1[3]:",tupla1[3]) 
print("Condenido en tupla2[-3]:",tupla2[-3])

print("Longitud de la tupla 2: ", end=" ")
print(len(tupla2))

algo1, algo2, algo3 = tupla2
print(algo1, " ",algo2," ",algo3)









