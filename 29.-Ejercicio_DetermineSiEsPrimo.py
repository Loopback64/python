# Determine si un número es primo.

""" Escriba un programa que permita ingresar un número y determinar si es un número primo o no.
Para ello debe recordar que, un número primo es aquel que es divisible para sí mismo y para la
unidad.

Solución: (Análisis)
Puede realizar con distintas estructuras de repetición. Usaremos mientras. Adicionalmente se
pueden anidar estructuras unas con otras. En este ejemplo tenemos un while dentro de otro
debido a que uno avanza con los números del 1 al 100 y el otro permite realizar las divisiones
del 1 hasta el mismo número, verificando que el residuo sea cero, si es cero es divisible.
Recuerde divisible para uno para sí mismo.



"""

num = 1   # Inicialización de la variable 'num' a 1
con = 0   # Inicialización de la variable 'con' (contador) a 0

while num <= 100:   # Bucle while que se ejecuta mientras 'num' sea menor o igual a 100
    if num % 10 == 0:   # Si el número es un múltiplo de 10, imprime una línea en blanco
        print("")
    
    p = num   # Asignación del valor de 'num' a la variable 'p'
    i = 1     # Inicialización de la variable 'i' a 1
    
    while i <= p:   # Bucle while anidado que se ejecuta mientras 'i' sea menor o igual a 'p'
        r = p % i   # Calcula el residuo de la división de 'p' entre 'i'
        if r == 0:   # Si el residuo es 0, significa que 'p' es divisible por 'i'
            con = con + 1   # Incrementa el contador 'con'
        i = i + 1   # Incrementa 'i' en 1 en cada iteración
    
    if con <= 2:   # Si el contador 'con' es menor o igual a 2 (es decir, 'p' tiene solo 2 divisores)
        print("\t", p, end=" ")   # Imprime 'p' con una tabulación y sin saltar de línea
    
    con = 0   # Reinicia el contador 'con' a 0 para el próximo número
    i = 0     # Reinicia 'i' a 0 para el próximo número
    num = num + 1   # Incrementa 'num' en 1 para pasar al siguiente número
     

























