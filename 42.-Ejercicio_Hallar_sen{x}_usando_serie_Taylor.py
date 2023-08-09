# Hallar sen (x) usando la serie de Taylor
""" Escriba un programa que permita obtener el resultado de la serie de Taylor, sen(x).
Solución: (Análisis)
El problema es similar al anterior, pero ahora debemos considerar la alternancia de los signos y
los números de las potencias y factorial son impares, se puede observar que cuando nos
encontramos en la iteración i, de valor impar, los términos deben restar y cuando estamos en la
iteración i, de valor par, los términos deben sumarse, al acumulador de sumas (términos).
Además, en el programa anterior el valor de i debió multiplicarse por dos para simular el inicio
de los números pares, ahora son impares y empiezan en tres. Usaremos la siguiente expresión
matemática, ii = i * 2 + 1  """

x = int(input("Ingrese x: ")) # x = 1
n = int(input("Ingrese n: ")) # n = 3

acum = 0
for i in range(1, (n),1):
    ii = i * 2 + 1
    # la potencia
    pot = 1
    for  j in range(1, (ii + 1), 1 ):
        pot = pot * x 
    # factorial
    fac = 1 
    for j in range(1, (ii +1), 1 ):
        fac = fac * j 
    if(i % 2 ==1):
        acum = acum - (pot/fac)
    else:
        acum = acum + (pot/fac)
print("e^x = ",(acum +1))




