def show_inventory(inventory):
     print("-------INVENTORY--------")
     for item in inventory:
         print ("The product is: ", item["product"])
         print ("The price is: ", item["price"])
         print ("The quantity is: ", item["quantity"])
         print("---------------------")