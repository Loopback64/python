# Determine si divisible para dos
"""Escriba un programa que permita el ingreso de un número entero, y luego determine si el
número ingresado es divisible para dos. 


Solución: (Análisis)
Si analiza el problema, sobre el valor ingresado debe realizarse una operación aritmética y sobre
su resultado, cumplir una condición, que su residuo deba ser 0, con esto sólo se verifica el
número n, siendo n divisible para dos. En Python los dos puntos indican el inicio de una secuencia
de código de una estructura o bloque de sentencias. """


num = int(input("Ingrese un numero: "))

op = num % 2

if (op == 0 ):
    print(num, "es un numero divisible para 2" )


else:
    print(num, "no es un numero divisible para 2")

