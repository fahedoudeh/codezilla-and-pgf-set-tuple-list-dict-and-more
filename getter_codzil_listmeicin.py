pharmacy_prices = {
"panadol": 32,
"cold free": 25,
"omega 3": 45,
"fuciden": 37,
"augmentin": 50,
"zinc": 20,
"vitamin c": 15
}

while True:

# ask for input
    user_input = input("Enter the names of treatments separated by a comma\
(press Enter to Exit):\n").strip().lower()
    
    if user_input == "":
        break

    print("-" * 20)

# Make a list of the treatments
    treatment_list = [t.strip() for t in user_input.split(",")]
    print(treatment_list)

    # Loop over the list of treatments
    for treatment in treatment_list:
        if treatment in pharmacy_prices:
            price = pharmacy_prices[treatment]
            print(f"{treatment.title()}: ${price}")
        else:
            print(f"{treatment.title()} is not available.")

    print("-" * 20)



# if the treatment is not available inform the user


# get the user input

# make a list of the treatments

# empty dictionary to store the treatments and their prices

# loop over the list of treatments

# get the treatment information from the dictionary

# print the treatments and their prices