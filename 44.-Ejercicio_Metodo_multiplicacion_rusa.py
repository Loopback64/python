# Método de multiplicación rusa
"""Escriba un programa que permita multiplicar dos números mediante el método ruso de la
multiplicación.
Solución: (Análisis)
Si ingresamos los números 11 como primer número y 12 como segundo número, debemos
entender que el método realiza divisiones por dos sobre el primero y multiplicaciones por dos
sobre el segundo, luego en el transcurso de cada proceso verifica si el primer número y sus
respectivos cocientes, son impares (desde el primer número ingresado), si es verdadera esta
condición, acumula en un sumador los respectivos segundos números o productos generados
(del primer segundo número o segundo número ingresado)
Mientras que al primer número se lo divide (división entera) para dos, al segundo número se lo
multiplica por dos, hasta que el primer número tienda a 1, en cada proceso sí el primer número
(cocientes) es impar se sumará su correspondiente segundo número (productos).
Finalmente, la acumulación de los productos debe sumar al mismo valor que si hubiéramos
multiplicados los dos primeros números. Para comprobar el resultado, invierta los números
ingresados, es decir, primero el 12 y luego el 11, como se puede observar el 12 no es impar, se
verificará en los siguientes cocientes.


"""


acum = 0
n1 = int(input("Ingrese primer número: "))
nn1 = n1
n2 = int(input("Ingrese segundo número: "))
nn2 = n2

while(n1 >= 1):
    print(n1," ",n2)
    if( n1 % 2 == 1):
        acum = acum + n2 
    n1 = n1 // 2
    n2 = n2 * 2
print("\n", nn1, " por ", nn2 ,
            " es " ,(nn1*nn2)," = ", acum)
            














