# ## Exercise: Python Dict and Tuples

# 1. We have following information on countries and their population (population is in crores),

#     |Country|Population|
#     |-------|----------|
#     |China|143|
#     |India|136|
#     |USA|32|
#     |Pakistan|21|
#     1. Using above create a dictionary of countries and its population

country_pop = {
    'China':143, 
    'India':136, 
    'USA':32, 
    'Pakistan':21}


    # 2. Write a program that asks user for three type of inputs,
    #     1. print: if user enter print then it should print all countries with their population in this format,
    #         ```
    #         china==>143
    #         india==>136
    #         usa==>32
    #         pakistan==>21
    #         ```
    #     1. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
    #     2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
    #     3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


def print_all():
    for country, population in country_pop.items():
        print(f'{country}==>{population}')

def add():
    country = input("enter a country name")
    if country in country_pop:
        print(f'{country} exist and do nothing')
    else:
        population = int(input("enter a population"))
        country_pop[country] = population
        print(f'{country} added with population {population} crores')
        
def remove():
    country  = input("enter a country name")
    if country in country_pop:
        del country_pop[country]
        print_all()
    else:
        print(f'{country} doesn\'t exist')
        
def query():
    country = input("enter a country name to see population")
    if country in country_pop:
        print(f'{country} population is {country_pop[country]} crores')
    else:
        print(f'{country} doesn\'t exist')
        

def operation():
    op = input("enter operation(query,remove, add, print)")
    if op == 'query':
        query()
    elif op == 'remove':
        remove()
    elif op == 'add':
        add()
    else:
        print_all()
        
operation()