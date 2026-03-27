from services import *
from validations import *
from file import *

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
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")
    
    try:
        option = valid_positive_int("Enter the option: ")
        
        if option == 1:
           
            product = valid_text("Enter the product name: ")
            price = valid_positive_float("Enter the product price: ")
            quantity = valid_positive_int("Enter the product quantity: ")
            register_of_product(inventory, product, price, quantity)
                
        elif option == 2:
            show_inventory(inventory)
                
        elif option == 3:
            product = input("Enter product to find: ")
            find_product(inventory, product)
        
        elif option == 4:
            product = valid_text("Enter product to update: ")
            price = valid_optional_float("New price (-1 to skip): ")
            quantity = valid_optional_int("New quantity (-1 to skip): ")
            
            new_price = price if price >= 0 else None
            new_quantity = quantity if quantity >= 0 else None
            
            update_product(inventory, product, new_price, new_quantity)
            
        elif option == 5:
            product = valid_text("Enter product to delete: ")
            delete_product(inventory, product)
            
        elif option == 6:
            calculate_statistics(inventory)
            
        elif option == 7:
            path = valid_text("Enter file name: ")
            save_csv(inventory, path)
            
        elif option == 8:
            path = valid_text("Enter file name: ")
            new_data= load_csv(path)
            
            if len(new_data) > 0:
                choice = input("Overwrite inventory? (S/N): ")

            if choice.lower() == "s":
                inventory = new_data
                print("Inventory replaced")
            
            else:
                for new_item in new_data:
                    exists = False

                    for item in inventory:
                        if item["product"].lower() == new_item["product"].lower():
                            item["quantity"] += new_item["quantity"]
                            item["price"] = new_item["price"]
                            exists = True

                    if not exists:
                        inventory.append(new_item)

                print("Inventory merged")

            

       
        elif option == 9:
            print("Goodbye!")
            is_running = False
            
        else:
            print("Invalid option")
            
    except ValueError:
        print("Please write a valid number")
