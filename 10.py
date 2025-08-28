days = ["sunday","monday","tuesday","wednesday","tyhursday","friday","saturday"]
num = int(input("Enter (1-7): "))
print(days[num-1] if 1 <= num <= 7 else "invalid input! Enter 1-7.")
 
