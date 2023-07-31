# Números Armstrong de cuatro cifras

""" Escriba un programa que permita el ingreso de un número de cuatro dígitos y determine si es
un número Armstrong [19][20]. Como el número que se ingresa posee 4 dígitos, la suma de
cada uno de sus dígitos elevado a 4 debe ser igual al número. 


Ejemplo: si ingreso el 8208 es igual a 84 + 24 + 04 + 84= 4096 + 16 + 0 + 4096 = 8208.
El número 8208 es un número Armstrong.  """

num = int(input("Ingrese un numero de cuatro cifras: "))

u = int( num % 10 )
d = int( num % 100/10)
c = int( (num / 100) %10)
m = int( num/1000)

print("unidad: ",u)
print("decena: ",d)
print("centena: ",c)
print("miles: ",m)

Arms = u*u*u*u + d*d*d*d + c*c*c*c + m*m*m*m

print("Número: ",num," = ", Arms)

print("!Es Angstrom ¡¡¡")








