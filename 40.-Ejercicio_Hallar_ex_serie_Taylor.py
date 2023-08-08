# Hallar ex usando la serie de Taylor
"""

Escriba un programa que permita obtener el resultado de la serie de Taylor, e^x.

Solución: (Análisis)
En el problema, se ingresan dos números, el primero puede ser el valor de x, y el valor n, que
representará el enésimo término de la serie de Taylor a evaluar. Para estos problemas, usaremos
el valor de x en 1, para comprender la lógica programática involucrada. 

Se debe evaluar el segundo y tercer término de la serie, debido a que el primer término su valor
es 1, es decir podemos realizar la evaluación a partir del segundo término y al final sumaremos
1 al resultado obtenido.
.

"""

x = int(input("Ingrese x: "))  # x = 1
n = int(input("Ingrese n: "))  # n = 3

acum = 0
for i in range(1, (n), 1):
    # potencia 
    pot = 1
    for j in range(1, (i+1), 1):
        pot = pot * x
    # factorial
    fac = 1
    for j in range(1, (i+1), 1):
        fac = fac * j
    acum = acum + (pot/fac)

print("e^x = ", (acum+1))











