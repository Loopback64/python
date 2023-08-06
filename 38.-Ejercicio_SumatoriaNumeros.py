# Sumatoria de los diez primeros números.
""" Escriba un programa que permita la sumatoria de los 10 primeros números. Utilice dos formas
de realizar el problema mediante las estructuras repetitivas conocidas.

Solución: (Análisis)
Es el problema es un común trabajo para un acumulador, éste debe estar inicializado en 0,
cuando es un acumulador de sumas o sumatoria se inicializa con 0, en el problema del factorial
tratado anteriormente, el acumulador es de productos y se lo inicializaba con 1. Ahora
presentaremos las acumulaciones a medida que recorren las repeticiones de número a número.


"""


print("Forma 1")
i = 1 
acum1 = 0

while(i<=10):
    acum1 = acum1 + i
    i = i + 1
    print(acum1,end =" ")

print(" ")
print("Forma 2")

acum2 = 0
for i in range(1,11,1):
    acum2 = acum2 + i
    print(acum2, end =" ")





