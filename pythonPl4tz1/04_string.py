name = "Nicolas"
last_name = "Molina Monroy"
edad = "21" 
print(name)
print(last_name)

###################################################################################################3

full_name = name + " "  + last_name
print(full_name)


quote = 'I am Nicolas'
print(quote)

quote2=' She said "Hello"  '
print(quote2)

# format
template = "Hola, mi nombre es " + name +   "  y mi apellido es " + last_name
print('V1', template )

template = "Hola, mi nombre es {} y mi apellido es {}" .format(name,last_name)
print('V2', template)


template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('V3' , template)


template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y tengo {edad} años de edad "
print('V4' , template)



















