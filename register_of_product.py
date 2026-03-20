
def register_of_product(inventory, product, price, quantity):
     sale = {
                 "product": product,
                 "price": price,
                 "quantity": quantity
                 }
     inventory.append(sale)
     print(f"Product added successfully!")