medical_cause = input("Did you have any medical issue ma'am? :")


if medical_cause == 'y':
    print("Allowed")
else:
    attendance = int(input("Enter the percentage of attendance: "))
    if attendance < 75:
        print("Not allowed")
    else:
        print("Allowed")