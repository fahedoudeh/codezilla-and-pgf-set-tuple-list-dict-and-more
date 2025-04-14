# available treatments
inventory = {
    "Paracetamol": {"price":25, "quantity":10},
    "Aspirin": {"price":15, "quantity":20},
    "Ibuprofen": {"price":20, "quantity":15},
    "Cough Syrup": {"price":30, "quantity":5},
    "Augmentin": {"price":100, "quantity":7},
    "Amoxicillin": {"price":80, "quantity":8},
    "Panadol": {"price":25, "quantity":10},
    "Zinc": {"price":15, "quantity":20},
    "Vitamin C": {"price":20, "quantity":15},
    "Fucidin": {"price":30, "quantity":5},
    "Kolanog": {"price":100, "quantity":2},
    }

# get the user input
while True:
    user_input = input("Enter treatment name(press Enter to exit): ").title()
    # if the user pressed enter
    if user_input == "":
        break
    # get item information from the dictionary    
    item = inventory.get(user_input, "Not available")
    # print the item information    
    if item != "Not available":
        print(f"Item: {user_input}")
        print(f"Price: {item["price"]}")
        print(f"Quantity: {item["quantity"]}")
    else:
        print(f"{user_input} {item}")    


