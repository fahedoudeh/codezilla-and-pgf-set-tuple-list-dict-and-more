products = {
    "T-Shirt": {"price": 300, "quantity": 10},
    "Shirt": {"price": 250, "quantity": 20},
    "Pants": {"price": 300, "quantity": 15},
    "Shoes": {"price": 400, "quantity": 5},
    "Socks": {"price": 25, "quantity": 7},
    "Hat": {"price": 50, "quantity": 8},
    "Gloves": {"price": 50, "quantity": 10},
    "Sweater": {"price": 500, "quantity": 20},
    "Jacket": {"price": 900, "quantity": 15},
    "Coat": {"price": 1000, "quantity": 5},
    "Scarf": {"price": 110, "quantity": 2},
    }
# get user input
while True:
    user_input = input("Enter the product name (press enter to exit)").strip().title()
    if user_input == "":
        break
    
    # print product details if availble 
    product = user_input
    price = products.get(user_input, {}).get("price", "Price Not available")
    quantity = products.get(user_input, {}).get("quantity", "Quantity NOt Available")
    print(f"Product: {product}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
print("Thanks for choosing Codezilla!")
  