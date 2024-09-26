# ## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#     1. Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input("please enter a city name and it should tell which country the city belongs to: ")
if city_name in india:
    print(f"{city_name} belongs to India")
elif city_name in pakistan:
    print(f"{city_name} belongs to Pakistan")
elif city_name in bangladesh:
    print(f"{city_name} belongs to bangladesh")
else:
    print("city not found in any country")