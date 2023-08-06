# Valide un número dentro de un rango.
""" Escriba un programa que, en un determinado rango, se valide un número. Utilice varias formas
de escribir el mismo programa usando los operadores de relación y operadores lógicos.

Solución: (Análisis)
Nos piden validar si un número es menor a cero (sin incluir), que esté entre 0 (inclusive) a 5
(inclusive) y si es mayor a 5 (sin incluir).

"""



num1 = int(input("Ingrese el número: "))

if(num1>=0 and num1<=5):
    print("Buen ingreso")
else:
    print("Mal ingreso")

if(num1<0 or num1>5):
    print("Mal ingreso")
else:
    print("Buen ingreso")

### Bloque 2

if(num1>-1 and num1<6):
    print("Buen ingreso")
else:
    print("Mal ingreso")

if(num1<=-1 or num1>=6):
    print("Mal ingreso")
else:
    print("Buen ingreso")


### Bloque 3


if not(num1>-1 and num1<6):
    print("Mal ingreso")
else:
    print("Buen ingreso")

if not(num1<0 or num1>5):
    print("Buen ingreso")
else:
    print("Mal ingreso")







































