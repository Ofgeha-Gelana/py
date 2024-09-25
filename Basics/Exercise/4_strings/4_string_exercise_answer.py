# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "11 Bole Ruwanda"
city = "Addis Ababa"
country = "Ethiopia"
address = street + "\n" + city + "\n" + country
print("Address using + operator", address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string", address)



# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

earth_rev = "Earth revolves around the sun"
print(earth_rev[6:14])
print(earth_rev[26:])


# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

num_fruit = 5
num_vegetables = 10
print(f"I eat {num_vegetables} veggies and {num_fruit} fruits daily")

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s='maine 200 banana khaye'
print(s.replace('200', '10').replace('banana', 'samosa'))