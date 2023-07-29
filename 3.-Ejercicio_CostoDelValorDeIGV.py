#Cobro del valor de IGV de un producto comprado

"""Calcular el valor a cancelar de un producto que cuesta $ 1 SOL, el programa debe mostrar
cómo se presenta en una factura, subtotal (cantidad por precio), IGV (del subtotal) y total a
pagar (la suma del subtotal + el IGV). Use de IGV el 12%."""

"""Solución : El problema requiere de fórmulas específicas, una de ellas es IGV = 𝑠𝑢𝑏𝑡𝑜𝑡𝑎𝑙 ∗ 0.12
Se ingresa al programa la cantidad de un producto comprado, por ejemplo 1 litro de leche, que
cuesta $ 1 sol , el subtotal sería cantidad por lo que cuesta."""


cantidad = int ( input( "   Ingrese la cantidad de compra del  producto : "))
precio = 1 
subtotal = cantidad*precio
IGV =  subtotal*0.12

total =  subtotal + IGV

print("Subtotal: ", subtotal)
print( "IGV: ", IGV   )
print("Total: ", total   ) 












