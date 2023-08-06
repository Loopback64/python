# Programa que simula una libreta escolar.
"""Escriba un programa que permita el ingreso de tres notas de una asignatura, calcule el promedio
y lo presenta en pantalla.

Solución: (Análisis)
Para este programa, el uso del contador está explícito, siendo tres el número de notas,
adicionalmente una variable está implícita, el acumulador de notas para luego obtener el
promedio. Claramente usted debe ir pensando en el uso de las variables que requiera para lograr
el resultado solicitado.

"""

print("#############################################################")
print("##################  LIBRETA ESCOLAR  ########################")
print("Asignatura: Programación")


acum = 0     # Inicializa un acumulador en 0 para sumar las notas.
i = 0        # Inicializa un contador o incrementador en 0 para llevar el seguimiento de cuántas notas se han ingresado.
promedio = 0.0  # Inicializa la variable promedio en 0.0.

while(i < 3):  # Inicia un bucle while que se repetirá mientras i sea menor que 3 (es decir, se ingresarán 3 notas).
    print("nota [",(i+1),"]",end=" ")  # Imprime el mensaje indicando el número de la nota que se está ingresando.
    nota = int(input("Ingrese: "))     # Solicita al usuario que ingrese la nota como un número entero.
    acum = acum + nota                 # Agrega la nota ingresada al acumulador.
    i = i + 1                           # Incrementa el contador en 1 para llevar el seguimiento de cuántas notas se han ingresado.

promedio = acum / i  # Calcula el promedio dividiendo la suma de las notas acumuladas entre la cantidad de notas ingresadas.
print("Promedio: ",promedio)  # Imprime el resultado del promedio calculado.























