#Trabajando con números enteros y reales

#Muestre en pantalla un conjunto de números enteros o reales con sus operaciones comunes.

"""Solución: (Análisis)
El problema requiere mostrar operaciones de evaluación con números, por ejemplo, división
con números enteros obtendremos números reales. Conocer los operadores como división
entera o residuo serán útiles más adelante. Otras operaciones pueden ser desarrolladas con
métodos o funciones existentes como la potencia de un números u operaciones a nivel bits."""

x = 7/5
y = 17/3     # Division con decimales
z = 17//3    # Sin redondeo - Division entera
w = 17%3     # Residuo de la division
v = 17**2    # Potencia de un número
u = 7^2      # Evaluacion de numeros a nivel de bits =realiza la operación XOR entre los números 7 y 2. A nivel de bits, la representación binaria de estos números es:  

"""
7  = 0111
2  = 0010

Ahora, apliquemos el operador XOR bit a bit:

    0111 (7)
XOR 0010 (2)
---------
    0101 (5)

| A (binario) | B (binario) | A XOR B (binario) |
|-------------|-------------|-------------------|
|     0       |     0       |        0          |
|     0       |     1       |        1          |
|     1       |     0       |        1          |
|     1       |     1       |        0          |

"""
print(x)
print(y)
print(z)
print(w)
print(v)
print(u)

