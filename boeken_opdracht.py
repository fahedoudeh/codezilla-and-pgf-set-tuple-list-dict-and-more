# Boeken geleend door Groep 1
groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]
# Boeken geleend door Groep 2
groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]


# Opdracht 1 Maak twee sets van de Groep 1 en Groep 2.

set1 = set(groep1)
set2 = set(groep2)

# Print de unieke boeken voor beide groepen

print(f"Unique boeken in groep 1\n{set1}\nUnique boeken in groep 2\n{set2}")

# Boeken door beide groepen geleend

print(f"Boeken die door beide groepen geleend:\n{set1 & set2}")

# boeken alleen door groep1 geleend

print(f"Boeken alleen door groep 1 geleend:\n{set1.difference(set2)}")
print(set1 - set2)

# boeken alleen door groep 2 geleend
print(f"boeken alleen door greop 2 geleend\n{set2 - set1}")
print(set2.difference(set1))
print("\n\n" )
# dict voor elke geroep. aantal geleend keren per boek

dict_groep1 = {"Harry Potter": 2,
               "De Hobbit": 3,
               "De Da Vinci Code": 2,
               "Twilight": 1,
               "De vijvde Golf": 1}

dict_groep2 = {"De Davinci Code": 1,
               "De Alchemist": 1,
               "Harry Potter": 1,
               "De Hobbit": 2,
               "Twilight": 2,
               "The Hunger Games": 1,
               "Gone Girl": 1,
               }

meest_geleend_naam1 = ""
meest_geleend_keer1 = 0

for boek, keers in dict_groep1.items():
    if keers > meest_geleend_keer1:
        meest_geleend_naam1 = boek
        meest_geleend_keer1 = keers
print(f"De meeste geleend boek in groep 1 is: {meest_geleend_naam1} geleend {meest_geleend_keer1} keers")    

print("\n" )


meest_geleend_naam2 = ""
meest_geleend_keer2 = 0

for boek, keers in dict_groep2.items():
    if keers > meest_geleend_keer2:
        meest_geleend_naam2 = boek
        meest_geleend_keer2 = keers
print(f"De meeste geleend boek in groep 2 is: {meest_geleend_naam2} geleend {meest_geleend_keer2} keers")




