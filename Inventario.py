Validation = True

while Validation: 
    try:
        product = str(input("Enter the product name: "))
        price = float(input("Enter the product price: "))
        quantity = int (input("Enter the product quantity: "))
    
    
        if price < 0 or quantity < 0:
            print("The price and quantity must be non-negative. Please try again.")
        elif not product.isalpha():
            print("The product name must contain only letters. Please try again.")
        else:
            Costo_total = price * quantity
            print("The total cost of the product is: ", Costo_total)
            print ("The product is: ", product)
            print ("The price is: ", price)
            print ("The quantity is: ", quantity)
            print ("The total cost of the product is:  ", Costo_total)
            
            validation = False
    except ValueError: 
        print("invalid input, please enter name, price or quantity")
