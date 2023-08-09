# Serie de Ulam
""" Escriba un programa que permita mostrar la serie de Ulam a partir de número entero ingresado
por teclado.

Solución: (Análisis)

En esta ocasión, el problema indica que para la nueva generación de un número de la serie de
Ulam debe aplicar un proceso diferente, las condiciones son de par e impar, luego se aplicar el
proceso descrito. Hay que observar el valor de n, para las siguientes iteraciones/repeticiones en
el bucle, se perderá hasta llegar al valor base o final que será 1 para esta serie.


"""

n = int(input("Ingrese un número: "))

while(n>1):
    if(n % 2 == 0):
        n = n // 2
    else:
        n = n * 3 + 1 
    print(n, end=" ")










