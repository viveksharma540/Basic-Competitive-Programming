A = int(input("Enter 1st:\n "))
B = int(input("Enter 2nd:\n "))
C = int(input("Enter 3rd :\n "))

if A <=B and A < C:
    print("A is minimum")
elif B < A and B < C:
    print("B is minimum")
else:
    print("C is minimum")
