#Inventario del producto y pregunta al usuario por el nombre del producto, precio y cantidad. 
producto = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))
cantidad = int (input("Ingrese la cantidad del producto: "))
#Validando que el precio y la cantidad sean no negativos y que el nombre del producto contenga solo letras
if precio < 0 or cantidad < 0:
     print("El precio y la cantidad deben ser no negativos. Por favor, intente de nuevo.")
elif producto.isalpha() == False:
        print("El nombre del producto debe contener solo letras. Por favor, intente de nuevo.")
#Mostrabndo el costo total del producto        
Costo_total = precio * cantidad
print("el costo total del producto es: ", Costo_total)
# Mostrar los datos de ingreso y total 
print ("el producto es: ", producto)
print ("el precio es de: ", precio)
print ("la cantidad es: ", cantidad)
print ("el costo total del producto es: ", Costo_total)
 
#Bueno el codigo es breve de explicar, se pide al usuario que productos, precio y cantidad desea para luego calcular el costo total del producto y mostrar los datos ingresados y el costo total. Se valida que el precio y la cantidad sean no negativos y que el nombre del producto contenga solo letras.