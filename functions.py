from functools import reduce
# create a function
def print_goal_message():
    print("Cristiano Ronaldo scored a goal!")

# create a function with arguments
def greet_person(name, time_of_day):
    greeting = "Good " + time_of_day + ", " + name + "!"
    print(greeting)

def make_coffee(coffee_type, cup_size):
    print("Making a " + cup_size + " cup of " + coffee_type + " coffee!")

def describe_book(title, author, genre):
    print("📖 Title:", title)
    print("✍️ Author:", author)
    print("📚 Genre:", genre)

# Return values
def total_goals(home_goals, away_goals):
    total = home_goals + away_goals
    return total

# Function with Multiple Return Statements
def is_positive(number):
    if number > 0:
        return "It's a positive number!"
    return "It's not a positive number!"

# lambda functions
total_energy_consumption = lambda fridge, ac, heater: fridge + ac + heater
net_savings = lambda total_income, total_expenses: total_income - total_expenses
car_efficiency = lambda total_miles, total_gallons: total_miles / total_gallons

# map function and lambda function
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = list(map(lambda temp: (temp * 9/5) + 32, celsius))

# filter function and lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))

# reduce function and lambda function
numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), numbers)

# call function
print_goal_message()

# call the function with arguments
greet_person("George", "evening")

make_coffee("Espresso", "small")

describe_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")

# call the function with the return value
team_a_home_goals = 3
team_b_away_goals = 2
total = total_goals(team_a_home_goals, team_b_away_goals)

print("Total goals scored in the match:", total)

# call the function with multiple return statements
message = is_positive(5)
print(message)

# run the lambda function
household_energy_consumption = total_energy_consumption(50, 120, 80)
print(household_energy_consumption)

monthly_savings = net_savings(5000, 3500)
print(monthly_savings)

mpg = car_efficiency(500, 25)
print(mpg)

# run the lambda - map function
print(fahrenheit)

# run the lambda - filter function
print(even_numbers)

# run lambda - reduce function
print(product)

# built-in python functions
classics_wordcount = {
    "War and Peace": 587287,
    "Moby Dick": 206052,
    "Pride and Prejudice": 122749
}

print("Classics Wordcount:", classics_wordcount)
print("Longest Classic:", max(classics_wordcount, key = classics_wordcount.get))

authors_novels = {
    "Agatha Christie": 75,
    "Stephen King": 63,
    "Isaac Asimov": 506
}

total_novels = sum(authors_novels.values())
number_of_authors = len(authors_novels)

print("Number of authors:", number_of_authors)
print("Total novels written:", total_novels)

players = ["Messi", "Ronaldo", "Neymar"]
teams = ["Barcelona", "Juventus", "Paris Saint-Germain"]
player_team_pairs = list(zip(players, teams))
print(player_team_pairs)

player_name = "Cristiano Ronaldo"
goals = 25
formatted_string = "{} scored {} goals this season.".format(player_name, goals)
print(formatted_string)

def add_team_prefix(name):
    return "Team " + name

team_names = ["Barcelona", "Real Madrid", "Juventus"]
prefixed_team_names = list(map(add_team_prefix, team_names))
print(prefixed_team_names)

teams = ["Barcelona", "Real Madrid", "Juventus"]
for index, team in enumerate(teams):
    print("{}. {}".format(index + 1, team))

def cook_recipe():
    dish_name = "Spaghetti Bolognese"
    main_ingredient = "Ground Beef"
    cooking_method = "Simmer"
    print(f"To cook {dish_name}, you need to {cooking_method} the {main_ingredient}.")

cook_recipe()

def cook_recipe(dish_name, main_ingredient, cooking_method):
    print(f"To cook {dish_name}, you need to {cooking_method} the {main_ingredient}.")

cook_recipe("Spaghetti Bolognese", "Ground Beef", "Simmer")

def cooking_time(number_of_dishes):
    return number_of_dishes * 30

time_needed = cooking_time(5)
print(f"We need {time_needed} minutes to cook these dishes.")

kitchen = "Italian Kitchen"

def cook_recipe(dish_name, cooking_method):
    kitchen_used = kitchen
    print(f"In the {kitchen_used}, we're {cooking_method}ing the {dish_name}.")

cook_recipe("Spaghetti Bolognese", "Simmer")

dishes = [
    {"name": "Spaghetti Bolognese", "cooking_time": 30},
    {"name": "Pizza Margherita", "cooking_time": 15},
    {"name": "Lasagna", "cooking_time": 60}
]

sorted_dishes = sorted(dishes, key = lambda dish: dish["cooking_time"], reverse = True)

for dish in sorted_dishes:
    print(f"{dish['name']} requires {dish['cooking_time']} minutes to cook.")

cooking_times = [30, 15, 60]

average_time = sum(cooking_times) / len(cooking_times)
print(f"The average cooking time for these dishes is {average_time:.1f} minutes.")

def code_validations(programmer_name, successful_validations, total_validations):
    accuracy = (successful_validations / total_validations) * 100
    print(f"{programmer_name}'s validation success rate is {accuracy:.2f}%.")

programmer_name = "Grace Hopper"
successful_validations = 120
total_validations = 130

code_validations(programmer_name, successful_validations, total_validations)

def bug_solution_ratio(bugs_solved, total_bugs):
    return bugs_solved / total_bugs

programmer_name = "Linus Torvalds"
bugs_solved = 36
total_bugs = 44

ratio = bug_solution_ratio(bugs_solved, total_bugs)
print(f"{programmer_name}'s bug solution ratio is {ratio:.2f}.")

def code_review_ratio(programmer_name, code_reviewed, total_code):
    percentage = (code_reviewed / total_code) * 100
    print(f"{programmer_name}'s code review percentage is {percentage:.2f}%.")

programmer_name = "Margaret Hamilton"
code_reviewed = 150
total_code = 250

code_review_ratio(programmer_name, code_reviewed, total_code)

quick_fix_ratio = lambda quick_fixes, total_issues: quick_fixes / total_issues

programmer_name = "Guido van Rossum"
quick_fixes = 20
total_issues = 38

ratio = quick_fix_ratio(quick_fixes, total_issues)
print(f"{programmer_name}'s quick fix ratio is {ratio:.2f}.")

def coding_hours_average(programmer_name, total_hours, days):
    avg_hours = total_hours / days
    print(f"{programmer_name} codes for an average of {avg_hours:.2f} hours per day.")

programmer_name = "Alan Turing"
total_hours = 2700
days = 100

coding_hours_average(programmer_name, total_hours, days)

def greeting(name):
    print(f"Hi! My name is {name}")

greeting("George")

print(range(5))

greek_names = ["George","John"]
greek_names.append("Kostas")
print(greek_names)