
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
            product = input("Write the product name: ")
            if product.strip():  # Verifica que no esté vacío
                inventario.append(product)
                print(f"Product '{product}' added successfully!")
            else:
                print("Please write something")
                
        elif option == 2:
            print (inventario)
            
        elif option == 3:
            def calcular():
                total = 0 
                
           
            
             
        elif option == 4:
            print("Goodbye!")
            is_running = False
        else:
            print("Please choose 1 or 4")
            
    except ValueError:
        print("Please write a valid number") 
                        