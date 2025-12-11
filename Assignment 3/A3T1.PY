def factorial(num):
    if num == 1:
        return 1
    elif num > 1 :
        return num * factorial(num-1)
    else:
        return 0


n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")