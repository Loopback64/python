"""  
Llenado de matriz de 5x5 versión 3
Escriba un programa que permita visualizar una matriz cuadrada de cinco por cinco, con los
valores tal como se muestran en la figura a continuación.
"""
#  


matriz3 = [                                                                             
            
            [0,0,0,0,0 ],  
            [0,0,0,0,0 ],  
            [0,0,0,0,0 ],  
            [0,0,0,0,0 ],  
            [0,0,0,0,0 ],  
                           ]

print("\nmatriz3:" )
print(matriz3)

print("\nmatriz3:      "  )


for i in range(len(matriz3)):
    for j in range(len(matriz3[i])):
        if(i == 0):
            matriz3[i][j] = 1
        if(i == 4):
            matriz3[i][j] = 1
        if(i == 0):
            matriz3[i][j] = 1
        if(j == len(matriz3)-1):
            matriz3[i][j]=1
        print(matriz3[i][j], end=" " ) 

    print()

            






