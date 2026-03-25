from services import *

inventory = []

print("Welcome The inventory")

is_running = True

while is_running:
    print("\n1. Add product")
    print("\n2. Show Inventory")
    print("\n3. Find product")
    print("\n4. update product")
    print("\n5. Delete product")
    print("\n6. calculate statistics")
    print("\n7. Exit")
    
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
               register_of_product(inventory,product, price, quantity)
                
        elif option == 2:
            if not inventory:
                print ("Inventory is empty ")
            else:
                show_inventory(inventory)
                
        elif option == 3:
            find_product(inventory, product)
        
        elif option == 4:
            update_product(inventory, product, new_price=None, new_quantity=None)  
            
        elif option == 5:
            delete_prodcut(inventory,product)
            
            
            
        elif option == 6:
            if not inventory:
                print ("No products to caculate")
            else:
                calculate_statistics(inventory)
                
             
        elif option == 7:
            print("Goodbye!")
            is_running = False
        else:
            print("Please choose 1,2,3 or 4")
            
    except ValueError:
        print("Please write a valid number") 
                        
                        