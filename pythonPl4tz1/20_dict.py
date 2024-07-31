print("****************************************************************************************")
print("                                                                  ")
print("Mostramos los valores cargados en el diccionario llamado person")
print("                                                                  ")
print("****************************************************************************************")


person = {
    'name'            : 'nico',
    'last_name'       : 'molina',
    'langs'           : ['python', 'javascript'],
    'age'             : 99
}



print("                                                                  ")
print("---------------------------------------------------------------------------------------")
print(person)
print("---------------------------------------------------------------------------------------")

print("                                                                  ")
print("***************************************************************************************")
print("                                                                  ")
print("Ahora cambiamos el valor name a santi --- a la edad le restamos 50 , agregamos rust al final de la lista")
print("y mostramos el resultado")
print("                                                                  ")
print("***************************************************************************************")
print("                                                                  ")
person['name'] = 'santi'   # cambia el valor del atributo name , que en este caso es nico cambiado a santi
person['age'] -= 50        # al valor actual del atributo le restamos 50
person['langs'].append('rust')    # Usamos el metodo .append para agregar un valor al final de la lista del atributo.

print(person)
print(person)
del person['last_name']    # eliminamos el atributo
person.pop('age')          # pop es un metodo que elimina un elemento del diccionario , simepre hay darle un argumento
print("---------------------------------------------------------------------------------------")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("               ")
print(person)
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print('items')
print("                                                                  ")
print()
print(person.items())       # imprime todos los items del diccionario 
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("                                                                  ")
print("    ")
print("   ")
print("   ")
print("")
print("    ")





print('name3')
print('name4')
print('name5')


