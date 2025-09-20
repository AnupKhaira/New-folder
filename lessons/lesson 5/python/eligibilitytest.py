med_cause=input("do you have any medical conditions Y or N:")
atten=int(input("Enter the attendance of the student: "))
if medical_cause == 'Y':
    print("you are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")