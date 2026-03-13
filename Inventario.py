#Inventario del producto y pregunta al usuario por el nombre del producto, precio y cantidad. 
product = str(input("Enter the product name: "))
price = float(input("Enter the product price: "))
quantity = int (input("Enter the product quantity: "))
#Validando que el precio y la cantidad sean no negativos y que el nombre del producto contenga solo letras
if price < 0 or quantity < 0:
     print("The price and quantity must be non-negative. Please try again.")
elif product.isalpha() == False:
        print("The product name must contain only letters. Please try again.")
#Mostrabndo el costo total del producto        
Costo_total = price * quantity
print("The total cost of the product is: ", Costo_total)
# Mostrar los datos de ingreso y total 
print ("The product is: ", product)
print ("The price is: ", price)
print ("The quantity is: ", quantity)
print ("The total cost of the product is:  ", Costo_total)
 
#Bueno el codigo es breve de explicar, se pide al usuario que productos, precio y cantidad desea para luego calcular el costo total del producto y mostrar los datos ingresados y el costo total. Se valida que el precio y la cantidad sean no negativos y que el nombre del producto contenga solo letras.