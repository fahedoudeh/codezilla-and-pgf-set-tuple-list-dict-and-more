pizzas = {
    "Margherita": 100,
    "Pepperoni": 120,
    "Meat Lovers": 150,
    "Chicken": 130,
    "Cheese": 100,
    "Veggie": 120,
    "Hawaiian": 150,
        }

# a list of pizzas to print
pizzas_to_print= ["Pepperoni", "Chicken", "Hawaiian" ]



# loop through the list and print the price of each pizza
 
for pizza in pizzas_to_print:
    print(f"{pizza} pizza costs {pizzas[pizza]}")


drinks = {
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30,
    "Tea": 20,
    "Coffee": 25,
    "Orange Juice": 30,
    "Mango Juice": 30
}

# coke mango juice tea coffie

# make drinks to print list

drinks_to_print = ["Coke", "Mango Juice", "Tea", "Coffee"]

for drink in drinks_to_print:
    print(f"\n{drink} \ncost:{drinks[drink]}")

print("\n\n")

menu = {
    "Cheese pizza": 100,
    "Veggie pizza": 120,
    "Hawaiian pizza": 150,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30
}


# # add Ice Cream - 30
# Chocolate Cake - 60
# Cheese Cake - 70
# Brownie - 40
# Donut - 30

menu.update({"Ice Cream": 30,
             "Chocolate Cake": 60,
             "Cheese Cake": 70,
             "Brownie": 40,
             "Donut": 30
             })


print(menu)

print("\n\n")



menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}

# Increase the prices of pizzas by 20 percent then print
# the restaurant menu.


# new_price = {(name, price * 1.20) for name, price in menu.items()}

# print(new_price)

for product, price in menu.items():
    if "pizza" in product:
        menu[product] = price * 1.20
print(menu)        


print("\n\n")


drinks = {
    "Latte": 30,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30,
    "Tea": 20,
    "Coffee": 25,
    "Orange Juice": 30,
    "Mango Juice": 30
    }

#Print soda items from the following menu.
 
 # a list of soda items
soda_items = ["Coke", "Sprite", "Fanta", "Pepsi"] 
# loop through the drinks menu
for soda in soda_items:
    if soda in drinks:
        print(soda, drinks[soda])
# check if the item is a soda and print the item

print("\n\n")


# Make a Pizza program that asks the user about the
# wanted pizza, and if available, it prints the pizza and
# its price. otherwise, you should print a sorry
# message.

pizzas = {"Margherita": 100, "Pepperoni": 120,
"Meat Lovers": 150, "Chicken": 130}

order = input("What Pizza do you like to order?\n:").title()


if order in pizzas:
    print(f"Great! {order} Pizza is available! it costs {pizzas[order]} ")
else:
    print(f"Oops! we don't make {order} Pizza.\nHere is a list of the available pizzas:\n{pizzas}")

# increase the pizza price by 20%

print("\nNew Prices:\n")
for pizza, price in pizzas.items():
    pizzas[pizza] *= 1.20
print(pizzas)        
        

print("\n\n")        

#print all pizzas and the prices in  an ordered manner

for pizza, price in pizzas.items():
    print(f"{pizza} Pizza Costs{price}")


#     Using the following information make a program
# that allows the user to get the school of the student
# when they enter the student name or the student id.


schools = {
    "Codezilla School":
    {'1100':"Mohamed Gouda", '1101':"Islam Hesham",
    '1102':"Ayman Mohamed", '1103':"Ahmed Khaled"},
    "Al Dorra School":
    {'2100':"Ahmed Hassan", '2101':"Mahmoud Ali",
    '2102':"Adham Wael", '2103':"Khaled Ali"},
    "Mostafa Kamel School":
    {'3105':"Hazem Ahmed", '3106':"Omar Mohamed",
    '3107':"Hussein Kamal", '3109':"Ali Ahmed"}
}

name_id = input("Enter the name or ID of a student to find his school:\n")

if name_id in schools["Al Dorra School"]:
    print(f"The student with name or ID: {name_id} is in Al Dorra School")
elif name_id in schools["Codezilla School"]:
    print(f"The student with name or ID: {name_id} is in Codezilla School")
elif name_id in schools["Mostafa Kamel School"]:
    print(f"The student with name or ID: {name_id} is in Mostafa Kamel School")
else:
    print(f"The name or ID entered is unknown!\n")    
    

employees = {
    "Ahmed Hassan": 12_000,
    "Mohamed Ahmed": 20_000,
    "Ali Ahmed": 15_000,
    "Khaled Ali": 10_000,
    "Omar Mohamed": 13_000,
    "Hazem Ahmed": 24_000,
    }
# increase the employees salaries 40%

for name, salary in employees.items():
    employees[name] = salary * 1.40
    print(f"{name}'s new salary is {employees[name]}")

    