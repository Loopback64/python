# Método de multiplicación rusa usando arreglos

""" Escriba un programa que permita multiplicar dos números por el método ruso, utilice arreglos
para almacenar la secuencia de números que se van generando.


Solución: (Análisis)
Observamos el problema presentado, requiere de dos arreglos, que llamaremos n1 y n2,
aplicaremos el mismo procedimiento visto para la multiplicación rusa sin arreglos, manipulando
los índices que se van creando a medida que requeriremos espacio de almacenamiento. Se
usarán las variables de almacenamiento como se muestra en la figura, finalmente se
compararán los valores almacenados en las primeras posiciones con el acumulador de productos
obtenido.
Cabe recordar que para la lista n1 se dividen sus elementos para dos, la lista n2 sus elementos
se multiplican por dos. Revise el código anteriormente elaborado para comprender el cambio al
uso de arreglos en este mismo problema.


"""



n1 = [0]
n2 = [0]

i = 0
acum = 0

n1[i]= int(input("Ingrese primer numero: "))

n2[i] = int(input("Ingrese segundo numero: "))

while(n1[i] >= 1):
    print(n1[i]," ",n2[i])
    if(n1[i] % 2 == 1):
        acum = acum + n2[i]
    n1.append(n1[i] // 2)
    n2.append(n2[i] * 2)
    i = i + 1

print("\n", n1[0], "por" , n2[0], 
        "es", (n1[0]*n2[0]),"=",acum)  

    































