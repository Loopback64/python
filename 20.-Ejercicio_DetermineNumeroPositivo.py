# Determine si un número en positivo
""" Escriba un programa que permita el ingreso de un número entero, y el programa determine si
es positivo.


Si analiza el problema, el valor que debe ser ingresado, debe cumplir una condición, que n > 0,
con esto sólo se verifica si el número n, es mayor que cero y con esto, la respuesta es: positivo.

En Python la identación o tabulación es importante observe las lineas  del código.


"""


n = int(input("Ingrese un numero: "))
if n > 0:
    print(n, "es positivo")
else:
    print(n, "es negativo")



