# sucesión de Fibonacci

"""
En la secuencia o sucesión de Fibonacci, se deben analizar sus diversas formas de solución y que
se pueden encontrar en distintos lugares o libros. Una forma de entender la generación de esta
sucesión es retrocediendo desde los dos primeros números 0 y 1, y encontrar una forma en
retrospectiva de obtenerlos, la imagen siguiente se encuentra una explicación.

Estructuras recursivas

Las estructuras recursivas permiten el uso de lo que conocemos como funciones o métodos que
los utilizaremos más adelante. Por ahora representaremos funciones recursivas sencillas para
entender su diseño.


"""

def fibonacci(n):

    if (n==0):
        return 0
    if (n==1):
        return 1
    return ( fibonacci(n-1) + fibonacci(n-2))

n = int(input("Ingrese n: "))
for i  in range(0,n):
   # print(fibonacci(i), end =" ")
   
    #print("%d" ,i)
    #print(fibonacci(i), end ="")
    print("%d: %d" % (i, fibonacci(i)))













