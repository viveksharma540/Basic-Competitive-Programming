#print hollow pramid pattern
# **********
# ****  ****
# ***    ***
# **      **
# *        *
n=int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*", end="")
    for k in range(2*i-2):
        print(" ", end="")
    for l in range(n-i+1):
        print("*", end="")
    print()