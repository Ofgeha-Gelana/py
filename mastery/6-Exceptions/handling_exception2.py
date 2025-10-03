
try:
    age = int(input("Ag: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exception was raised.")