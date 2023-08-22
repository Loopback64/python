"""
Función para el método de multiplicación rusa

Escriba un programa que permita ingresar dos números y obtener el producto mediante el
método ruso de la multiplicación, utilice una función.


Solución: (Análisis)


Recordemos el código de la multiplicación rusa para usarlo. Mientras un primer número se
dividía para dos, al segundo se multiplicaba por dos tantas veces hasta obtener el último
cociente 1. Por cada cociente impar se sumaba su correspondiente producto obtenido. Luego la
sumatoria de esos productos debe ser el mismo resultado, como si hubiera multiplicado los dos
primeros números. Usaremos una lista para el paso de parámetros.

"""

def ruso(lista):
    i = 0
    acum = 0
    while(lista[i]>=1):
        a = lista[i]
        b = lista[i+1]
        if(a%2 == 1):
            acum = acum + b
        lista.append(a//2)  # ubica al final
        lista.append(b*2)   # ubica al final
        i = i + 2
    return acum

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))

resultado = ruso([n1,n2])

print("Respuesta es: ", resultado)











