n = int(input("Enter:\n"))
print("odd no.from 1 to", n, "are:")
for i in range(1, n+1):
    if i % 2 != 0:   
        print(i, end=" ")
