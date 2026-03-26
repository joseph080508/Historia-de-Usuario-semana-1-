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
  
