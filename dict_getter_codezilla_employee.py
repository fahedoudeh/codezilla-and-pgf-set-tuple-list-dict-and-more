employees = {
    "Mohamed Hassan": {"age": 25, "salary": 5000, "department":
    "HR"},
    "Ahmed Kamal": {"age": 30, "salary": 6000, "department":
    "IT"},
    "Ali Adel": {"age": 35, "salary": 7000, "department":
    "IT"},
    "Hossam Yehia": {"age": 40, "salary": 8000, "department":
    "IT"}
    }


# get the user input
while True:
    user_input = input("Enter the employee name \
press Enter to exit: ").title()

    # if the user pressed enter
    if user_input == "":
        break
    # get employee information from the dictionary
    info = employees.get(user_input, "Not Available")
    # print the employee information
    if info != "Not Available":
        print(f"Employee: {user_input}")
        print(f"Age: {info["age"]}")
        print(f"Salary: {info["salary"]}")
        print(f"Department: {info["department"]}")
    else:
        print(info)    