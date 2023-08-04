# Presente el factorial de un número n, usando recursividad.

""" 
Solución: (Análisis)
La recursividad es una forma elegante de desarrollar un problema iterativo. Dado un número n,
debemos utilizar un método o función con multiplicaciones sucesivas invocadas hacia la misma
función.







"""



def factorial(n):
    if (n>0):
        return (n*factorial(n-1))
    else:
        return 1

n = int(input("Ingrese un número: "))

for i in range(1,n+1):
    print(factorial(i))






        

