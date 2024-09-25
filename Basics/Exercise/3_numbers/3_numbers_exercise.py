# Exercise
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it

length = 92
width = 48.8
area_of_field = length * width
print("Area of the football field", area_of_field)


# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
# and you gave shopkeeper 20 dollar. 
# Find out using python, how many dollars is the shopkeeper going to give you back?

total_packet = 9
packet_costs = 1.49
money_paid = 20
total_costs = total_packet * packet_costs
give_back = money_paid - total_costs
print("Cash Back: ", give_back)


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
# is its length. If tiles cost 500 rs per square feet, how much will be the total
# cost to replace all tiles. Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)

length = 5.5
area = length ** 2 ## Area of square is length power 2
cost = area * 500
print("total cost for tile replacement for Bathroom is: ", cost)


# 4. Print binary representation of number 17
decimal_number = 7
binary_representation = bin(decimal_number)[2:]
print("Binary representation for number is: ", binary_representation)
num = 17
print("Binary of number 17 is: ", format(num, 'b'))
