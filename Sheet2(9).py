N = int(input("Enter:\n"))
sumofdigits = 0
while N != 0:
    digit = N % 10        
    sumofdigits += digit   
    N = N // 10           

print("sum :", sumofdigits)
