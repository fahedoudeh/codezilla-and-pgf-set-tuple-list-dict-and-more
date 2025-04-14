students = {
    "Mohamed Hassan": 
        {"grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97},
        "school": "Codezilla"
        },

    "Ahmed Kamal": 
        {"grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94},
        "school": "Codezilla"
        },

    "Ali Adel": 
        {"grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90},
        "school": "Al-Azhar"
    },

    "Sara Ahmed": 
        {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100},
        "school": "Al-Azhar"
    }
    }

# loop through the students
for student in students:
# print the name of the student
    print(f"Student name: {student}")
# print the school of the student
    print(f"School: {students[student]["school"]}")
# print the grades of the student
    print("Grades: ")
    subject_grades = students[student]["grades"]
# get the subjects and grades of the current student
    for subject, grades in subject_grades.items():
        print(f"{subject.title()}: {grades}")
    
# print the subject and the grade
# print a line to separate the students
    print("$"*15)


# calculate the percentage of every student

for student in students:
    grades = students[student]["grades"].values()
    
    total_score = sum(grades)
    len_subjects = len(grades)
    percentage =total_score / len_subjects
    print(f"{student}'s total percentage is {percentage:.2f}")
    print("-" * 20)


student_name = input("Please Enter the name of the student: ").title()

if student_name in students:
    print(f"{student_name} got the following grades:")
    
    
    student_grades = students[student_name]["grades"]
    for subject, grade in student_grades.items():
        print(f"{subject}: {grade}")

    total_score = sum(student_grades.values())
    len_subjects = len(student_grades.values())
    percentage = total_score / len_subjects
    print(f"{student_name}'s total percentage is {percentage:.2f}%")
else:
    print("Sorry! we don't have info about this student")    

