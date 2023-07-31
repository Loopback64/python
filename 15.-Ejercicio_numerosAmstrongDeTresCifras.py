# Números Armstrong de tres cifras
"""
Escriba un programa que permita el ingreso de un número de tres dígitos y determine si es un
número Armstrong [17][18]. Como el número que se ingresa posee 3 dígitos, la suma de cada
uno de sus dígitos elevado a 3 debe ser igual al número.


Ejemplo si ingreso el 153 es igual a 13 + 53 + 33 = 1 + 125 + 27 = 153.
El número 153 es un número Armstrong.

"""


num = int(input("Ingrese un numero de tres cifras: "))
u = int(num % 10)
d = int(num % 100/10)
c = int(num /100)

print("Unidad: ",u)
print("Decena: ",d)
print("Centena: ",c)

Arms = u*u*u + d*d*d + c*c*c
print("Numero: " ,num ," = " ,Arms)
print("¡Es Angstrom !" )








