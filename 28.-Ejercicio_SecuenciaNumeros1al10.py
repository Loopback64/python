# Muestre la secuencia de números del 1 al 10
"""

Escriba un programa que permita visualizar los números del 1 al 10 de forma ascendente y luego
descendente.


Solución: (Análisis)
Para el uso de la estructura repetitiva requiere de una variable de control, inicializada en un
valor y luego incrementada o decrementada dependiendo de una cantidad, 1 generalmente.

"""




# Inicialización de la variable 'i' con el valor 1
i = 1

# Bucle while que se ejecuta mientras 'i' sea menor o igual a 10
while i <= 10:
    print(i, end=" ")  # Imprimir el valor actual de 'i' sin saltar de línea
    i += 1  # Incrementar 'i' en 1 en cada iteración

print()  # Imprimir una línea en blanco para separar las dos secuencias

# Reasignación de la variable 'i' con el valor 10
i = 10

# Bucle while que se ejecuta mientras 'i' sea mayor o igual a 0
while i >= 0:
    print(i, end=" ")  # Imprimir el valor actual de 'i' sin saltar de línea
    i -= 1  # Decrementar 'i' en 1 en cada iteración














