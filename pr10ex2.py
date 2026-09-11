def inventory_manager(products):
    item = input("Enter product name: ")

    if item in products:
        index = products.index(item)
        print(f"{item} is available at index {index}.")
    else:
        print(f"{item} is not available in the inventory.")


# Example product catalog
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

inventory_manager(products)