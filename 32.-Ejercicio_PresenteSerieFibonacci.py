# Presente la serie de Fibonacci.
"""Escriba un programa que, dado un número entero, permita mostrar los enésimos números de
la sucesión de Fibonacci.

La espiral de Fibonacci, "Designed by Freepik"



Solución: (Análisis)
Se realiza el ingreso de un número entero por teclado, luego se presenta la sucesión.
"""

n = int(input("Ingrese n: "))
a = -1
b = 1
for i in range (1, n+1 ):
    c = a + b
    print(c,end=" ")

    a = b
    b = c


    print("   \t ")













