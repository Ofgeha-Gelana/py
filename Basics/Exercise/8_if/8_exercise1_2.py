# 2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
    
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_one = input("please enter city one: ")
city_two = input("please enter city two: ")

if city_one in india and city_two in india:
    print("Both cities are in India")
elif city_one in pakistan and city_two in pakistan:
    print("Both cities are in Pakistan")
elif city_one in bangladesh and city_two in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")