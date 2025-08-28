n = int(input("Enter:\n"))
sumofdigits = 0
while n != 0:
    digit = n % 10        
    sumofdigits += digit   
    n = n // 10           

print("sum of all digits:", sumofdigits)
