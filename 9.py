Year = int(input("Enter :\n"))
if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
    print(" Leap year.")
else:
    print("not Leap year")
