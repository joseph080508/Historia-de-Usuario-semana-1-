def register_of_product(inventory, product, price, quantity):
    #Create product on the list
    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }
    inventory.append(sale)
    print("Product added successfully!")


def show_inventory(inventory):
    #Show all products
    print("-------INVENTORY--------")
    
    for item in inventory:
        print("Product:", item["product"])
        print("Price:", item["price"])
        print("Quantity:", item["quantity"])
        print("---------------------")


def find_product(inventory, product):
    #search product
    for item in inventory:
        if item["product"].lower() == product.lower():
            print("Product found:")
            print("Product:", item["product"])
            print("Price:", item["price"])
            print("Quantity:", item["quantity"])
            return item

    print("Product not found")
    return None


def update_product(inventory, product, new_price=None, new_quantity=None):
    #update data
    for item in inventory:
        if item["product"].lower() == product.lower():

            if new_price is not None:
                item["price"] = new_price

            if new_quantity is not None:
                item["quantity"] = new_quantity

            print("Product updated successfully")
            return True

    print("Product not found")
    return False


def delete_product(inventory, product):
    #delete product
    for item in inventory:
        if item["product"].lower() == product.lower():
            inventory.remove(item)
            print("Product deleted successfully")
            return True

    print("Product not found")
    return False


def calculate_statistics(inventory):
    #calculate all products
    total = 0
    total_unit = 0

    print("----------TOTAL----------\n")

    for item in inventory:
        costo = item["price"] * item["quantity"]
        total += costo
        total_unit += item["quantity"]

        print("Product:", item["product"])
        print("Price:", item["price"])
        print("Quantity:", item["quantity"])
        print("Subtotal:", costo)
        print()

    most_expensive = max(inventory, key=lambda x: x["price"])
    highest_stock = max(inventory, key=lambda x: x["quantity"])

    print("TOTAL INVENTORY VALUE:", total)
    print("TOTAL UNIT VALUE:", total_unit)
    print("MOST EXPENSIVE:", most_expensive["product"], "-", most_expensive["price"])
    print("HIGHEST STOCK:", highest_stock["product"], "-", highest_stock["quantity"])

    return {
        "Total unit": total_unit,
        "Total value": total,
        "Most expensive": most_expensive,
        "Highest stock": highest_stock}