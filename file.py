import csv

def save_csv(inventory, path):
    if len(inventory) == 0:
        print("No data to save")
        return

    try:
        file = open(path, "w", newline="")
        writer = csv.writer(file)

        writer.writerow(["product", "price", "quantity"])

        for item in inventory:
            writer.writerow([item["product"], item["price"], item["quantity"]])

        file.close()
        print("Saved")

    except:
        print("Error saving file")
  
def load_csv(path):
    inventory = []

    try:
        file = open(path, "r")
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            try:
                product = row[0]
                price = float(row[1])
                quantity = int(row[2])

                data = {
                    "product": product,
                    "price": price,
                    "quantity": quantity
                }

                inventory.append(data)

            except:
                print("Error in row")

        file.close()
        print("Loaded")

        return inventory

    except:
        print("Error loading file")
        return []
