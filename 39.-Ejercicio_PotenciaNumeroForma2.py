# La potencia de un número.
"""Escriba un programa que permita el ingreso de dos números enteros, uno representa la base y
el otro el exponente de la operación matemática conocida como potenciación.
"""


base = int(input("Base: "))

expo = int(input("Exponente: "))

acum = 1

for i in range(expo):
    acum = acum * base
else:
    print(acum)





