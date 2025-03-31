
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk
for stad in steden:
    print(stad)

# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple
nieuwe_tuple = tuple1 + tuple2
print(nieuwe_tuple)
# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
mijn_tuple = ("Amsterdam", 33, False, 1.9,  "Rotterdam", "Zeeland", True)

# Print enkele elementen van de mijn_tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element
print(mijn_tuple[0])
new_mijn_tuple = mijn_tuple[2:5]
print(new_mijn_tuple)
print(mijn_tuple[0])
print(mijn_tuple[-1])
# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd
gegevens = ("Ali",8)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
naam, leeftijd = gegevens


# Print de uitgepakte variabelen

print("naam:", naam)
print("leeftijd:", leeftijd)