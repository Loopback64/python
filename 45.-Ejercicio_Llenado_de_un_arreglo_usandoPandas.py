# Usando Pandas
"""Se define una lista de elementos enteros y, mediante la biblioteca de Numpy, con el objeto np,
se utilizan los métodos o funciones disponibles para trabajar sobre la lista."""

import pandas as pd
lista = ["Do" , "Re" , "Mi" , "Fa" , "Sol", "La" , "Si" ]

index = [1, 2,3,4,5,6,7 ]
serie = pd.Series(lista,index)

print("Presenta: \n%s" % serie)

