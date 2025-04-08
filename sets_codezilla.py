nums = [3, 4, 5, 67, 2, 4, 6, 8, 3, 6, 8, 8, 3, 44, 7, 7, 7, 5, 5, 3, 3, 2, 2, 2, 1, 4, 5, 6, ]
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print(nums)
print(unique_nums)
print(set(nums))


print("#" * 66)

# """ Make a list that generates 1000 random number
#  between 1 and 1000 then calculate the number of
#  unique numbers and print them, then print the
#  average of the list and the average of the unique
#  numbers. """



# Make a list that generates random numbers between 1 and 1000
import random

random_nums = [random.randint(1, 1_000) for num in range(1_000)]

print(len(random_nums))
# calculate number of unique numbers
uniqu_nums = set(random_nums)
print(len(uniqu_nums))

# calculate the average of numbers in the list

print(sum(random_nums) / len(random_nums))

# calculate the average of numbers in the set

print(sum(uniqu_nums) / len(uniqu_nums))


lege_verzameling = set()

print("lege verzameling:", type(lege_verzameling))
print(*range(1, 6), sep="^")

getallen = set([1, 2, "Rood", 5])

print(type(getallen), getallen)