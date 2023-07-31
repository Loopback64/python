#  El uso de formateo en números decimales
# Escriba un programa que calcule el cociente dados dos números enteros, muestre el resultado con varios dígitos decimales.

""" El problema nos pide el ingreso de dos valores enteros
por teclado y luego obtener el cociente con distintas
cantidades de decimales, dos, tres, cuatro, etc.

Un primer valor será el dividendo, el otro será el divisor, luego se obtendrá el cociente de ellos
mediante el uso del operador / y seguido usaremos un formateo para mostrar su resultado
dependiendo de la cantidad de dígitos que obtengamos, finalmente usaremos tres nuevas
funciones de redondeo, redondeo hacia arriba y hacia abajo. """

import math

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))

cociente1 = n1/n2
cociente2 = int(n1/n2)              # parte entero sin redondeo
cociente3 = math.ceil(n1/n2)        # redondeo hacia arriba
cociente4 = math.floor(n1/n2)       # Redondeo hacia abajo 
cociente5 = round(n1/n2)

print("Cociente1:  ",cociente1  )
print("Cociente2 SR :  ",cociente2 )
print("Cociente3 CRArriba: ",cociente3)
print("Cociente4 CRAbajo:  ",cociente4)
print("Cociente5 CR: ",cociente5)

print("{:23.6f}".format(cociente1))
print("{:10.5f}".format(cociente1 )) # espaciosn blancos
print("{:010.5f}".format(cociente1)) # con ceros

print("{:21d}".format(cociente2)) # espacios blancos
print("{:4d}".format(cociente2))
print("{:3d}".format(cociente2))
print("{:2d}".format(cociente2))
print("{:1d}".format(cociente2))

print("{:04d}".format(cociente2)) # con ceros
print("{:03d}".format(cociente2))
print("{:02d}".format(cociente2))
print("{:01d}".format(cociente2))

""" [200~Línea 8: Cociente1 es la división normal.
Línea 9: Cociente2 es la división sin redondeo.
Línea 10: Cociente3 con redondeo hacia arriba.
Línea 11: Cociente4 con redondeo hacia abajo.
Línea 12: Cociente5, división con redondeo.
Línea 18: Contabiliza 23 espacios para todo el
número obtenido con 6 dígitos decimales.
Línea 19: Utiliza 10 espacios para todo el
número obtenido incluyendo el punto decimal, y
llena con espacios en blanco de ser necesario a la
izquierda.
Línea 20: Utiliza 10 espacios para todo, llenando
con ceros a la izquierda si faltase.
Línea 21: Utiliza 21 espacios para todo el
número, llena con espacios en blanco.
Línea 22: Utiliza 4 espacios para todo el número,
llena con espacios en blanco a la izquierda.
Línea 23: Utiliza 3 espacios para todo el número,
llena con espacios en blanco a la izquierda.
Línea 26: Utiliza 4 espacios para todo el número,
llena con ceros a la izquierda.
Línea 27: Utiliza 3 espacios para todo el número,
llena con espacios en blanco a la izquierda"""


























