
def registro_de_product(inventario, product, price, quantity):
     sale = {
                 "product": product,
                 "price": price,
                 "quantity": quantity
                 }
     inventario.append(sale)
     print(f"Product added successfully!")