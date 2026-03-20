def calculate_statistics(inventory):
     total = 0 
     print("----------TOTAL----------")
     print()
        
     for item in inventory:
            costo = item["price"] * item ["quantity"]
            total += costo
            print ("The product is: ", item["product"])
            print ("The price is: ", item["price"])
            print ("The quantity is: ", item["quantity"])
            print ("The total:  ", costo)
                    
            print ("TOTAL INVENTORY VALUE: ", total)
                    
                    
                   

