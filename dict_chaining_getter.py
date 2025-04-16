# 1. Define a dictionary called 'inventory' containing treatments with their prices and quantities.

inventory = {"Paracetamol": {"price":25, "quantity":10},
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

# 2. Start an infinite loop to allow repeated user input.
while True:

# 3. Prompt the user to enter treatment names separated by commas.
    user_input = input("Enter the treatment names separated by comma(press enter to Exit):\n")

# 4. If the user input is empty, exit the loop.
    if user_input == "":
        break

# 5. Split the input string into individual treatment names using the comma as a separator.
    split_list = user_input.split(",")
   
# 6. Create an empty list called 'treatments'.
    treatments = []

# 7. For each item in the split list:
#    - Remove extra spaces from the name.
#    - Convert it to title case (first letter capitalized).
#    - Add it to the 'treatments' list.
    for item in split_list:
        item = item.strip().title()
        treatments.append(item)
   
# 8. Loop through each treatment in the 'treatments' list:
#    - If the treatment exists in the 'inventory' dictionary:
#        - Retrieve its price and quantity.
#        - Display the treatment's name, price, and quantity.
#    - Else:
#        - Display a message saying the treatment is not available.
    for treatment in treatments:
        if treatment in inventory:
            info = inventory.get(treatment, {})
            price = info.get("price", "Not Available")
            quantity = info.get("quantity", "Not Available")
            print(f"Item: {treatment}")
            print(f"Price: {price}")
            print(f"Quantity: {quantity}")
            print("-" * 30)
        else:
            print(f"Item: {treatment}\nPrice: Not available\nQuantity: not available")
            print("-" * 30)

# 9. Repeat steps 3–8 until the user exits.
