nums = []  
for i in range(1, 11):
    nums.append(i)
print(nums)

my_list = [num for num in range(1, 11) if num % 2 == 0]
print(my_list)

fruits = ['apples', 'banana', 'strawberry', 'orange']
print(fruits)
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]

nums = [-num for num in nums]

print(nums)

scores = [75, 87, 93, 98, 82, 67, 91, 88]

scores =  [str(score)+'%' for score in scores]
print(scores)

fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]

fruits_lower = [fruit.lower()for fruit in fruits]

print(fruits_lower)


prices = [10.99, 20.99, 30.99, 40.99, 50.99]

prices_in_dollars = [f"${price}" for price in prices]
print(prices_in_dollars)

nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
nums_sum = sum([num for num in nums if num % 2 == 0])
print(nums_sum)


print("#"*77)

# Write code to find the sum of numbers that are
# divisible by 3 and between 20 and 140 then print the
# numbers separated by a comma.


# find the numbers that are divisible by 3 and between 20 and 140
nums = [num for num in range(20, 140) if num % 3 == 0]
print(nums)
# find the sum of the numbers
nums_sum = sum([num for num in range(20, 140) if num % 3 == 0])
# print the sum
print(nums_sum)
# convert the numbers to strings
num_strings = str(nums)
# print the numbers separated by a comma
print(num_strings)
#########
# other way to print the numbers separated by a comma

import random
# make list with 20 random numbers between 100 and 1000 using
# list comprehension and random.randint()
random_nums = [random.randint(100, 1_000) for _ in range(20)]
print(random_nums)

print("%" * 100)

# Make list with 100 random numbers between 100
# and 10,000 that are divisible by 3 and 5.



random_nums = [random.randint(100, 10_001) for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
print(random_nums)


# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from',
'which', 'would', 'will', 'there',
'make', 'when', 'more', 'other', 'what', 'time',
'about', 'than', 'into', 'could',
'state', 'only', 'year', 'some', 'take', 'come',
'these', 'know', 'like', 'then',
'first', 'work', 'such', 'give', 'over', 'think',
'most', 'even', 'find', 'also',
'after', 'many', 'must', 'look', 'before', 'great',
'back', 'through', 'long',
'where', 'much', 'should', 'well', 'people', 'gouda',
'just', 'because', 'good',
'each', 'those', 'feel', 'seem', 'high', 'place',
'little', 'world', 'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become'
]
words_upper = [word.upper() for word in words ]
print(words_upper)

print("&" * 88)

words = [["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],

["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
print(words)
# A. convert each inner list to a string and join them with a
# space and add them to a list named sentences
sentances = [" ".join(word) for word in words]
print(sentances)
modified_sentences = [sentance.replace(" ", "-").upper() for sentance in sentances ]
print(modified_sentences)



nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99]

# get the absolute value of each number
positive_nums = [abs(num) for num in nums]
print(positive_nums)