# Handle Divide by Zero Exceptions

def func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("The second number that is provided is zero. Please ensure you provide the right ones")
        return 0

print(func(3, 0))

