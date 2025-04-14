


pharmacy_prices = {
"panadol": 32,
"cold free": 25,
"omega 3": 45,
"fuciden": 37,
"augmentin": 50,
"zinc": 20,
"vitamin c": 15
}

user_input = input("Enter the names of treatments separated by a comma (Press Enter to Exit) :\n").strip().lower()
print('-'*20)

treatments = user_input.split(", ")

treatments_prices = {}

for treatment in treatments:
    treatments_prices[treatment] = pharmacy_prices.setdefault(treatment, 'Not Available')

for treatment, price in treatments_prices.items():
    print(f"{treatment.title()} : {price}")













# ask for input

# if the treatment is not available inform the user


# get the user input

# make a list of the treatments

# empty dictionary to store the treatments and their prices

# loop over the list of treatments

# get the treatment information from the dictionary

# print the treatments and their prices