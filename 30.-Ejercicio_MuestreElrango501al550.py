# Escriba un programa que permita mostrar los números del 501 al 550 en bloques de 10.

"""  Solución: (Análisis)
Cuando conocemos el número de repeticiones, es decir el inicio y fin de la secuencia de
iteraciones, usaremos el lazo para o for."""

# Utilizando un bucle for para iterar desde 501 hasta 550 (ambos inclusive)
for i in range(501, 551):
    print(i, end=" ")  # Imprimir el valor actual de 'i' sin saltar de línea
    
    # Verificar si 'i' es un múltiplo de 10
    if i % 10 == 0:
        print()  # Imprimir una línea en blanco para formatear la salida cuando 'i' sea múltiplo de 10












