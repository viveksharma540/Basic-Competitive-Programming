percentage = float(input("Enter your percentage:\n"))

if percentage < 25:
    print("Your grade is: D")
elif percentage <= 45:
    print("Your grade is: C")
elif percentage <= 65:
    print("Your grade is: B")
elif percentage <= 85:
    print("Your grade is: A")
else:
    print("Your grade is: A+")
