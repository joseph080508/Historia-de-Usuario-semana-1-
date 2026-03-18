

inventario = []

print("Welcome The inventory")

is_running = True

while is_running:
    print("\n1. Add product")
    print("\n2. Show Inventory")
    print("\n3. calculate statistics")
    print("\n4. Exit")
    
    try:
        option = int(input("Enter the option: "))
        
        if option == 1:
            product = str(input("Enter the product name: "))
            price = float(input("Enter the product price: "))
            quantity = int (input("Enter the product quantity: "))
            
            if price < 0 or quantity < 0:
                print("The price and quantity must be non-negative. Please try again.")
                
            elif not product.isalpha():
                print("The product name must contain only letters. Please try again.")
            
            elif product.strip():  # Verifica que no esté vacío
                sale = {
                 "product": product,
                 "price": price,
                 "quantity": quantity
                 }
                inventario.append(sale)
                print(f"Product added successfully!")
                
        elif option == 2:
            if not inventario:
                print ("Inventory is empty ")
            else:
                print("-------INVENTORY--------")
                for item in inventario:
                    print ("The product is: ", item["product"])
                    print ("The price is: ", item["price"])
                    print ("The quantity is: ", item["quantity"])
                    print("---------------------")
            
            
        elif option == 3:
            if not inventario:
                print ("No products to caculate")   
            else:   
                total = 0 
                print("----------TOTAL----------")
                print()
        
                for item in inventario:
                    costo = item["price"] * item ["quantity"]
                    total += costo
                    print ("The product is: ", item["product"])
                    print ("The price is: ", item["price"])
                    print ("The quantity is: ", item["quantity"])
                    print ("The total:  ", costo)
            
                    print ("TOTAL INVENTORY VALUE: ", total)
            
             
                
           
            
             
        elif option == 4:
            print("Goodbye!")
            is_running = False
        else:
            print("Please choose 1,2,3 or 4")
            
    except ValueError:
        print("Please write a valid number") 
                        
                        
    