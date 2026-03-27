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
    errors = 0 

    try:
        file = open(path, "r")
        reader = csv.reader(file)

        header = next(reader)
        
        # validar encabezado
        if header != ["product", "price", "quantity"]:
            print("Header is not correct")
            return []


        for row in reader:
               # validar columnas
            if len(row) != 3:
                errors += 1
                continue
            try:
                product = row[0]
                price = float(row[1])
                quantity = int(row[2])
                
                 # validar negativos
                if price < 0 or quantity < 0:
                    errors += 1
                    continue

                data = {
                    "product": product,
                    "price": price,
                    "quantity": quantity
                }

                inventory.append(data)

            except:
                errors +=1

        file.close()
        
        print("Products loaded:", len(inventory))
        print("Rows with error:", errors)
        
        return inventory
    
    except FileNotFoundError:
        print("File not found")

    except:
        print("Error loading file")
        return []
