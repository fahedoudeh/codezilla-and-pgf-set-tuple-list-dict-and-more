students = {
    "Mohamed": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},
        "school": "Codezilla"
    },
    "Ahmed": {"grades": {
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94},
        "school": "Codezilla"
    },

    "Ali": {"grades": {
        "math": 85,
        "english": 83,
        "science": 87,
        "arabic": 100,
        "history": 90},
        "school": "Al-Azhar"
    },
"Sara": {"grades": {
        "math": 100,
        "english": 94,
        "science": 98,
        "arabic": 100,
        "history": 100},
        "school": "Al-Azhar"
    }
}


print(f"\n\nMohamed's grades in Math and English:\nMath: {students['Mohamed']["grades"]["math"]}\nEnglish: {students['Mohamed']['grades']['english']}")
print(f"Mohamed's school: \n{students['Mohamed']["school"]}\n")
print(f"Ahmad's grades in Math, Science and Arabic:\nMath: {students['Ahmed']["grades"]['math']}")
print(f"Science: {students['Ahmed']["grades"]["science"]}")
print(f"Arabic: {students['Ahmed']["grades"]["arabic"]}")

print(f"\nAli's school and grades in History, Science and Arabic: \nSchool: {students['Ali']["school"]}")
print(f"History: {students['Ali']["grades"]['history']}")
print(f"Science: {students['Ali']["grades"]['science']}")
print(f"Arabic: {students['Ali']["grades"]['arabic']}")

print(f"\nSara's grades in Math, Science and History: ")
print(f"Math: {students['Sara']["grades"]['math']}")
print(f"Science: {students['Sara']["grades"]['science']}")
print(f"History: {students['Sara']["grades"]['history']}\n\n")




restaurant_menu = {
    "Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120},
    "Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100},
    "Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20},
    "Desserts": {"Ice Cream": 50, "Chocolate Cake": 60,
    "Cheese Cake": 70},
    "Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges":50}
}

print(f"Chicken burger price: {restaurant_menu['Burgers']["Chicken"]}")
print(f"Viggies pizza price: {restaurant_menu['Pizzas']["Veggie"]}")
print(f"Coke price: {restaurant_menu['Drinks']["Coke"]}")
print(f"Chocolate cake price: {restaurant_menu['Desserts']["Chocolate Cake"]}")
print(f"Onion Rings price: {restaurant_menu['Sides']["Onion Rings"]}\n\n")



students = {
    "Mohamed": 
    {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},

    "school": "Codezilla"
    },
    "Ahmed": 
    {"grades": {
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94},

    "school": "Codezilla"
    },
    "Ali": 
    {"grades": {
        "math": 85,
        "english": 83,
        "science": 87,
        "arabic": 100,
        "history": 90},

    "school": "Al-Azhar"
    },
    "Sara": 
    {"grades": {
        "math": 100,
        "english": 94,
        "science": 98,
        "arabic": 100,
        "history": 100},

    "school": "Al-Azhar"
    }
}

total_greades = sum(students['Ali']["grades"].values())
len_grades = len(students["Ali"]["grades"].keys())
print("Total grades: ", total_greades)
max_score = len_grades * 100
percentage = (total_greades / max_score) * 100

print(f"Total percentage of Ali's grades is: {percentage:.1f} %")