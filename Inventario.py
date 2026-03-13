#Inventory of the product and asks the user for the product name, price and quantity. 
product = str(input("Enter the product name: "))
price = float(input("Enter the product price: "))
quantity = int (input("Enter the product quantity: "))
#Validating that the price and quantity are non-negative and that the product name contains only letters
if price < 0 or quantity < 0:
     print("The price and quantity must be non-negative. Please try again.")
elif product.isalpha() == False:
        print("The product name must contain only letters. Please try again.")
#Show the total cost of the product        
Costo_total = price * quantity
print("The total cost of the product is: ", Costo_total)
# Mostrar los datos de ingreso y total 
print ("The product is: ", product)
print ("The price is: ", price)
print ("The quantity is: ", quantity)
print ("The total cost of the product is:  ", Costo_total)
 
 #the program should also display the total cost of the product, which is calculated by multiplying the price by the quantity.
 