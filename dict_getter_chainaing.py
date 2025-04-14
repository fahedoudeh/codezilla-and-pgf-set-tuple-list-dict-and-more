patients = {
    "Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1},
    "Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2},
    "Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3},
    "Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4}
    }

while True:
    # get user input
    user_input = input("Enter the patient name (press Enter to Exit): ").strip().title()
    # enter to exit
    if user_input == "":
        break
    patient = patients.get(user_input, {})
    age = patient.get("age", "Not available")
    disease = patient.get("disease", "Not available")
    room = patient.get("room", "Not available")
    message = f"""Patient: {user_input}
Age: {age}
Disease: {disease}
Room: {room}"""
    print(message)

print("Welcome to Codezilla hospital. wishing all patients speedy recovery")