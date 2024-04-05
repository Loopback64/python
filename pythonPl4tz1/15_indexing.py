text = "Ella sabe Python"
print(text[0])
print(text[1])

# print(text[999])


size = len(text)
print('size =>',size)

print(text[size - 1]) # se resta el ultimo valor 1 por que inicia en 0
print(text[-1])

# slicing

print(text[0:5])     #saca una parte
print(text[10:16])   #saca una parte del texto
print(text[:10])     #saca una parte el inicio hasta donde se indica
print(text[5:])      #saca desde el 5 a el final
print(text[:])       # saca desde el inicio hasta el final


#Los saltos

print(text[10:16:1])#Da saltos de lo que toma , es decir si toma de 10 a 16 .salta 1 es decir no varia el resultado
print(text[10:16:2])#Da saltos con el valor de 2   P^-^t^-^o^ Pto
print(text[::2])    #Da saltos con el valor de 2 y va de inicio al final.










