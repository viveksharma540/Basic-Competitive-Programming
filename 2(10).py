
n=int(input("enter:"))
original=n
rev=""
while n>0:
    rem=n%10
    rev+=str(rem)
    n=n//10
print(" palindrome" if original==int(rev) else "No plaindrome!")
