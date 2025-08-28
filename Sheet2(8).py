n = int(input("Enter:\n"))
count = 0
if n == 0:
    count = 1
else:
    while n != 0:
        n = n // 10  
        count += 1
print("nnumber of digits:", count)
