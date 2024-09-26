# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i == "heads":
        count += 1
    else:
        continue

print("Number of heads: ", count)


# 2. Print square of all numbers between 1 to 10 except even numbers

for i in range(1, 11):
    if i%2 == 0:
        continue
    else:
        print(i**2)

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
exp_amount = int(input("Expenses: "))
for i in range(len(expense_list)):
    if expense_list[i] == exp_amount:
        print(f"Expense {exp_amount} occurred in month: ", i+1)
        break
    else:
        print("Expense not found")


# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
length = 0
while length <= 5:
    la = input("are you tired? ")
    if la == "yes":
        print("you didn't finish the race")
        break
    elif la == "no":
        length += 1
    else:
        if length == 5:
            print("Congratulations! You finished the race")
    


# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
x = 1
while x <= 5:
    print('*' * x)
    x = x+1