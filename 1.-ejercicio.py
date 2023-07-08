



import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Las raíces son reales y diferentes.")
        print("Raíz 1:", raiz1)
        print("Raíz 2:", raiz2)
    elif discriminante == 0:
        raiz = -b / (2*a)
        print("Las raíces son reales e iguales.")
        print("Raíz:", raiz)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminante) / (2*a)
        print("Las raíces son complejas e imaginarias.")
        print("Raíz 1:", real_part, "+", imaginary_part, "i")
        print("Raíz 2:", real_part, "-", imaginary_part, "i")

# Solicitar coeficientes al usuario
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

# Calcular y mostrar las raíces
calcular_raices(a, b, c)

