x = 3.3
print(x)
print("------------------")
y = 1.1 + 2.2
print(y)
print(type(y))
print("------------------")

print(x == y)
print("------------------")

y_str = format(y, ".2g")   # Ya se convirtió en string

print(type(y_str))
print("------------------")
print("------------------")
print(y_str)
print("------------------")

print('str =>' , y_str)

# print(int(y_str) == x)

print( y_str == str(x))
print('*' * 10)

print(y,x)

tolerance = 0.00001
print(abs(x - y)  < tolerance)




