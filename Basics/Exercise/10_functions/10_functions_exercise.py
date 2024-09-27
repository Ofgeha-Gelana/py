# # Exercise: Functions in python
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```

def calculate_area(base, height):
    area = (1/2) * base * height
    return area
base = 5
height = 10
area = calculate_area(base, height)
print("Area of triangle is: ", area)


# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(base, height, shape = "rectangle"):
    if shape == "triangle":
        area = (1/2) * base * height
    elif shape == "rectangle":
        area = base * height
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area
base = 5
height = 10
area = calculate_area(base, height)
print("Area of rectangle is: ", area)



# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(num):
    for i in range(num):
        s = ''
        for j in range(i+1):
            s = s + "*"
        print(s)
print_pattern(5)