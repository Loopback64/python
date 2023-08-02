# Presente una tabla de multiplicar.

""" Escriba un programa que, dado un número entero, permita mostrar una tabla de multiplicar.

Solución: (Análisis)
El ingreso por teclado de un valor entero, debe permitir generar sucesivas multiplicaciones, de
0 a 12, simulando una tabla de multiplicar. """


    
# Solicitar al usuario ingresar un número
n = int(input("Ingrese un numero: "))

# Utilizando un bucle for para iterar desde 0 hasta 11 (12 no inclusive)
for i in range(0, 12):
    # Imprimir la multiplicación de 'i' y 'n' en un formato descriptivo
    print(i, "", i, "por", n, "es", (i * n))

# El bloque 'else' en este contexto no está relacionado con el bucle for
# y siempre se ejecutará después de que el bucle termine
else:
    print("Finalizamos")  # Imprimir un mensaje al finalizar






