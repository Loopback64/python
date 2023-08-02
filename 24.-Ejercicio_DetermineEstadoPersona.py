# Determine el estado de la persona según su edad

""" Escriba un programa que permita el ingreso de un número que represente la edad.

Solución: (Análisis)
Utilizaremos edad < 0, bebé, edad < 12, niño, edad < 18, menor de edad, edad < 25, adolescente,
edad < 60, adulto, caso contrario adulto mayor. Menor a cero no es admitido.


"""

edad = int(input("Ingrese su edad :" ))
if(edad < 0):
    print("eres bebé")
elif(edad < 12):
    print("eres niño")
elif(edad < 25):
    print("adolescente")
else:
    if(edad < 60):
        print("adulto")
    else:
        print("adulto mayor")

    







