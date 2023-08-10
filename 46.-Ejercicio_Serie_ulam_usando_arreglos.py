# Serie de Ulam con arreglos
# Escriba un programa que permita almacenar la serie de Ulam un arreglo.

""" Solución: (Análisis)
En python los vectores son llamados listas, como se ha trabajado hasta este momento, ahora
debemos ir almacenando en una lista la serie de números de Ulam que se generan. Usaremos
métodos o funciones que permitan almacenar, recorrer e insertar elementos de forma sencilla.   """

lista = [0]

i = 0 

lista[i]  = int(input("Ingrese un numero: "))

while(lista[i]>1):
    if(lista[i] % 2 == 0):
        lista.append(lista[i] // 2)
    else :
        lista.append(lista[i] * 3 + 1 )
    i = i + 1

print(lista, end=" ")


    
