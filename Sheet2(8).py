N = int(input("Enter :\n"))
count = 0
if N == 0:
    count = 1
else:
    while N != 0:
        N = N // 10  
        count += 1
print("Number of digits:", count)
