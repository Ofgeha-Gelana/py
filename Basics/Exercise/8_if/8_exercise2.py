# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = int(input("Sugar Level: "))
if sugar_level >=80 and sugar_level <= 100:
    print("Sugar is Normal")
else:
    if sugar_level > 100:
        print("Sugar is High")
    else:
        print("Sugar is lower")
    