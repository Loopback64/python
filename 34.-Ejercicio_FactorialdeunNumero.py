# Presente el factorial de un número n.

"""  Escriba un programa que determine el factorial de un número.

Solución: (Análisis)
Dado un número n, debemos utilizar un lazo for para recorrer la serie de números que
intervienen en la acumulación de productos.
"""


n = int(input("Ingrese un número: "))
acum = 1 
for i in range(0,n):
    print((i+1),end =" ")
    acum = acum * (i+1)
print(" = ",acum)





