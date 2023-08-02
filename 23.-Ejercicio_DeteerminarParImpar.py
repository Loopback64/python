# Determine si un número es par o impar
# Escriba un programa que permita el ingreso de un número y determine si es par o impar,
# asuma el cero como par.

""" Solución: (Análisis)
Utilizaremos la estructura selectiva doble. Adicionalmente evaluaremos con el operador del
módulo o resto, si obtenemos cero, por verdadero tendremos un número par, caso contrario un
número impar. Con la aparición del else: cambia la identación al nivel del if, recuerde los dos
puntos.  """

x = int(input("Ingrese un número: "))

if (x % 2 == 0):
    print(x,"es par ")
else :
    print (x, "es impar")




 

 




