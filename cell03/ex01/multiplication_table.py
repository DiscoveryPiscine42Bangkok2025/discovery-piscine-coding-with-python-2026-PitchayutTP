number = int(input("Enter a number: "))

for i in range(1, number+1):
    result = number * i
    print(number, "x", i, "=", result)