studenten = [("Ali", 8), ("Joey", 9.5),("Aya", 7),("Benthe", 7.5),("Roos", 6.5)]
# print name of students with cijfers
for naam, cijfer in studenten:
    print(f"    {naam}: {cijfer}")

# make a separet list of only the scores
scores = [cijfer for naam, cijfer in studenten]

# calculate the total score
total_score = sum(scores)


# find gemiddelde score
gemiddelde_score = total_score / len(studenten)

print(f"gemiddelde score is: {gemiddelde_score}")

# find who has the highest score

highest_naam = studenten[0][0]
highest_cijfer = studenten[0][1]
for naam, cijfer in studenten:
    if cijfer > highest_cijfer:
        highest_naam = naam
        highest_cijfer = cijfer
print(f"{highest_naam} heeft de hoogste cijfer van {highest_cijfer}")        



