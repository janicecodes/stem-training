try:
    value = int(input("enter first number:"))
    print(value)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("zro divisions must be")