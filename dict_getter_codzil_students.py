students = {
"Mohamed Hassan": {
"Password": "123456"
,
"grades": {
"math": 100
,
"english": 90
,
"science": 80
,
"arabic": 100,
"history": 97
}
},
"Ahmed Kamal": {
"Password": "1234",
"grades": {
"math": 100,
"english": 95,
"science": 93,
"arabic": 100,
"history": 94}
},
"Ali Adel": {
"Password": "12",
"grades": {
"math": 85,
"english": 83,
"science": 87,
"arabic": 100,
"history": 90}
},
"Hossam Yehia": {
"Password": "33",
"grades": {
"math": 100,
"english": 94,
"science": 98,
"arabic": 100,
"history": 100}
}
}

# get the user input
while True:
    user_input = input("Enter the student name (press Enter to Exit): ").title()
# if the user pressed enter
    if user_input == "":
        break
    if user_input not in students:
        print("this student name is not listed in the data!")
        user_input = input("Enter another student name (press Enter to Exit): ").title()
        if user_input == "":
            break
# get the password
    password = input("Enter the password: ")
    
    if user_input in students and  password == students[user_input]["Password"]:

# get student information from the dictionary
        student_info = students.get(user_input, "Not Available")
    # print the student information
        print("Grades:")
        print("-" * 20)
        grades = students[user_input]["grades"]
        for subject, marks in grades.items():
            print(f"{subject}: {marks}")
        print("-" * 20)
        percentage = sum(grades.values()) / len(grades)   
        print(f"Student Percentage: {percentage:.2f}%")
    else:
        print("Wrong Password or Student Name")     
