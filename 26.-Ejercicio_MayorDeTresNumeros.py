# El mayor de tres números enteros con operadores relacionales

# Escriba un programa que permita visualizar cuál es el mayor de tres números enteros ingresados por teclado.

""" Solución: (Análisis)
Dado el diagrama de flujo para su comprensión, hay que recordar que la validación entre
números depende de las condiciones que agreguemos para ir filtrando cada posibilidad de
comparación. A medida que se desee validar más números, más bifurcaciones.   """


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

if(a>>b):
    if(a>c):
        print(a," es mayor ")
    else:
        print(c," es mayor ")

else:
    if(b>c):
        print(b, "es mayor")
    else:
        print(c, "es mayor")


    
