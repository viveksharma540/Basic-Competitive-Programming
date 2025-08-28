A =int(input("enter the 1st angle:\n"))
B =int(input("enter the 2nd angle:\n"))
C =int(input("enter the 3rd angle:\n"))

if A > 0 and B > 0 and C > 0 and (A + B + C == 180):
    print("valid triangle ")
else:
    print("invalif triangle ")
