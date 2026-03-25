from services import *

inventory = []

print("Welcome The inventory")

is_running = True

while is_running:
    print("\n1. Add product")
    print("2. Show Inventory")
    print("3. Find product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Calculate statistics")
    print("7. Exit")
    
    try:
        option = int(input("Enter the option: "))
        
        if option == 1:
            product = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the product quantity: "))
            
            if price < 0 or quantity < 0:
                print("The price and quantity must be non-negative.")
                
            elif not product.isalpha():
                print("The product name must contain only letters.")
            
            elif product.strip():
                register_of_product(inventory, product, price, quantity)
                
        elif option == 2:
            show_inventory(inventory)
                
        elif option == 3:
            product = input("Enter product to find: ")
            find_product(inventory, product)
        
        elif option == 4:
            product = input("Enter product to update: ")
            price = float(input("New price (-1 to skip): "))
            quantity = int(input("New quantity (-1 to skip): "))
            
            new_price = price if price >= 0 else None
            new_quantity = quantity if quantity >= 0 else None
            
            update_product(inventory, product, new_price, new_quantity)
            
        elif option == 5:
            product = input("Enter product to delete: ")
            delete_product(inventory, product)
            
        elif option == 6:
            calculate_statistics(inventory)
                
        elif option == 7:
            print("Goodbye!")
            is_running = False
            
        else:
            print("Invalid option")
            
    except ValueError:
        print("Please write a valid number")