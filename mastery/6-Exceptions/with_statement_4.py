
# We don't need finally, b/c when we use with it will close automatically

try:
    with open("app.py") as f:
        print("File Opened.")
    age = int(input("Ag: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError, FileNotFoundError):
    print("You didn't enter a valid age.")
else:
    print("No exception was raised.")


# When we do with multiple files.
try:
    with open("app.py") as f, open("another.py", "w") as target:
        print("File Opened.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError, FileNotFoundError):
    print("You didn't enter a valid age.")
else:
    print("No exception was raised.")