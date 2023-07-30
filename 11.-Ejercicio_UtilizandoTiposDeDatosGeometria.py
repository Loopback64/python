# Utilizando tipos de datos para geometría
# Escriba un programa que calcule el área y el perímetro de unpentágono regular

"""Solución: (Análisis)
El problema nos pide el uso de fórmulas para encontrar el perímetro y área de una figura
geométrica regular, para ello hay que recordar las fórmulas requeridas

n = 5 por el número de lados
Para el perímetro tenemos: 𝑝 = 𝑙𝑎𝑑𝑜 𝑥 𝑛
Para el área tenemos: 𝐴 = 𝑝 𝑥 𝑎 /2 donde a es la apotema """

lado = 3
n = 5
ap = 2 
p = lado*n
A = (p*ap)/2

print("Perímetro en metros",p)
print("Área en metros cuadrados",A)

