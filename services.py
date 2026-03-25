
def register_of_product(inventory, product, price, quantity):
     sale = {
                 "product": product,
                 "price": price,
                 "quantity": quantity
                 }
     inventory.append(sale)
     print(f"Product added successfully!")



def show_inventory(inventory):
     print("-------INVENTORY--------")
     
     
     for item in inventory:
         print ("The product is: ", item["product"])
         print ("The price is: ", item["price"])
         print ("The quantity is: ", item["quantity"])
         print("---------------------")
         


def find_product(inventory, product):
     for item in inventory:
          if item["product"].lower() == product.lower():
               print("Product found: ")
               print("Product: ", item["product"])
               print("Price: ", item["price"])
               print ("Quantity: ", item["quantity"])
               return item
     print("Product not found")
     return None
 
 
    
def update_product(inventory, product, new_price=None, new_quantity=None):
     for item in inventory:
          if item["product"].lower() == product.lower():
               if new_price is not None:
                    item["price"] = new_price
               if new_quantity is not None:
                    item["quantity"] = new_quantity
               print("product update successfully")
               return True
     print("Product not found")
     return False




def delete_prodcut(inventory, product):
     for item in inventory:
          if item ["product"].lower() == product.lower():
               inventory.remove(item)
               print("product deleted successfully")
               return True
     
          
     
     
         
def calculate_statistics(inventory):
     total = 0 
     total_unit = 0 
     print("----------TOTAL----------")
     print()
        
     for item in inventory:
            costo = item["price"] * item ["quantity"]
            total += costo
            total_unit += ["quantity"]
            
            print ("The product is: ", item["product"])
            print ("The price is: ", item["price"])
            print ("The quantity is: ", item["quantity"])
            print ("The subtotal:  ", costo)
            
            
            most_expisive = max(inventory, key=lambda x: x["price"])
            highest_stock = max(inventory, key= lambda x: x["quantity"]) 
                    
            print ("TOTAL INVENTORY VALUE: ", total)
            print("TOTAL UNIT VALUE: ", total_unit)
            print("MOST EXPENSIVE PRODUCT: ", most_expisive["product"], "-", most_expisive["price"])
            print ("THE HIGHEST STOCK PRODUCT: ", highest_stock["product"], "-", highest_stock["quantity"])
            
            return{
                 "Total unit": total_unit,
                 "Total value": total,
                 "Most expensive": most_expisive,
                 "Highest stock": highest_stock
            }
                    