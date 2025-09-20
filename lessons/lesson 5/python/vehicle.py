print("Select your ride: ")
print("1. Bike")
print("2. Car")

Choice=int(input("Enter your choice: "))
if(choice==1):
    print("What type of bike?")
    print("1.scooty\n")
    print("2.scooter\n")
choice2=int(input("Enter your choice2: "))
if choice2==1:
    print("You have selected scooty")
else:
    print("You have selected scooter")

elif(Choice==2):
    print("what type of car?")
    print("1. sedan")
    print("2. XUV")
    choice3=int(input("enter your choice: "))
if choice3==1:
    print("You have selected sedan")
else:
    print("you have selected XUV")

else:
    print("Wrong choice")