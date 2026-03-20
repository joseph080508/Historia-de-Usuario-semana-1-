def show_inventory(inventario):
     print("-------INVENTORY--------")
     for item in inventario:
         print ("The product is: ", item["product"])
         print ("The price is: ", item["price"])
         print ("The quantity is: ", item["quantity"])
         print("---------------------")