"""
Escriba un programa que permita presentar el factorial de un número, utilice una función.


Utilizaremos el código anteriormente usado para el cálculo del factorial. Recordemos primero
que es un acumulador de productos (acum = 1) y que se utiliza un lazo for para el recorrido.
Matemáticamente, el factorial de 1 y 0 es siempre 1, no hay factorial para números negativos.

"""

def factorial(n):
    acum = 1
    for i in range(n):
        v = i + 1
        acum = acum * v
    return acum

n = int(input("Ingrese n:"))

print("Factorial de ", n)
print("es ", factorial(n))























