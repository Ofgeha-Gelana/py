try:
    file = open("app.py")
    age = int(input("Ag: "))
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
except FileNotFoundError:
    print("File not found.")
else:
    print("No exception was raised.")
finally:
    file.close()