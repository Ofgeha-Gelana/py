
try:
    age = int(input("Ag: "))
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exception was raised.")

try:
    age = int(input("Ag: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exception was raised.")

