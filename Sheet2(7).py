n = int(input("Enter : "))
sumofodd = 0
for i in range(1, n+1):   
    if i % 2 != 0:       
        sumofodd += i
print("sum of all odd number 1 to", n, "is:", sumofodd)

