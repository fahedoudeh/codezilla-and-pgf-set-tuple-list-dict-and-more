# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,
getal = int(input("voer een getal in:\n"))


# print(getal, "x 1 =", getal * 1)
# print(getal, "x 2 =", getal * 2)
# print(getal, "x 3 =", getal * 3)
# print(getal, "x 4 =", getal * 4)
# print(getal, "x 5 =", getal * 5)
# print(getal, "x 6 =", getal * 6)
# print(getal, "x 7 =", getal * 7)
# print(getal, "x 8 =", getal * 8)
# print(getal, "x 9 =", getal * 9)
# print(getal, "x 10 =", getal * 10)



# Probeer het nu met een loop.
for getal1 in range(1, 11):
    print(f"{getal} x {getal1} = {getal*getal1}")

# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)

limiet = int(input("Voer een limiet in: "))

som = 0

for getal in range(1, limiet + 1):
    som += getal

print(f"De som van alle getallen tot {limiet} is {som}")


# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

for getal in range(1, 101):
    if getal % 3 == 0 and getal % 5 == 0:
        print("FIZZBUZZ")
    elif getal % 3 == 0:
        print("FIZZ")
    elif getal % 5 == 0:
        print("BUZZ")
    else:
        print(getal)

# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

# i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
# a = 0
# b = 1

# Eerst drukken we de eerste twee getallen af


# Vervolgens berekenen we de volgende getallen en drukken ze af
# i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))
#
# a = 0
# b = 1
#
# print(a)
# print(b)
#
# for _ in range(i - 2):
#     c = a + b
#     print(c)
#     a = b
#     b = c

aantal_getallen = 10

eerste = 0
tweede = 1

print("Fibonacci-reeks:")
print(eerste)
print(tweede)

for _ in range(aantal_getallen - 2):
    volgende = eerste + tweede
    print(volgende)
    eerste = tweede
    tweede = volgende
