# La potencia de un número.

"""Escriba un programa que permita el ingreso de dos números enteros, uno representa la base y
el otro el exponente de la operación matemática conocida como potenciación.

Solución: (Análisis)

En el problema dado, se ingresan dos números, el primero puede ser la base y el segundo puede
ser el exponente. Con ello debe repetir la acumulación de exponente veces base.

"""


print("Base: ", end = " " )
base = int(input())
# hola = int(input(" Hola:"))
print("Exponente: ", end= " " )
expo = int(input())
acum = 1
for i in range(1, (expo+1),1  ):
    acum = acum * base

else:
    print(acum)




# print("El valor de hola es: ",hola)







