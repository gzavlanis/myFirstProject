# Numeric Data Types
num_programmers = 10
lines_of_code = 3000
average_lines_per_programmer = 300
average_bug_rate = 0.05

print("Number of programmers in the team:", num_programmers)
print("Total lines of code written:", lines_of_code)
print("Average lines of code per programmer:", average_lines_per_programmer)
print("Average bug rate per line of code:", average_bug_rate)

# Sequence Data Types
string_example = "Python Developer"
list_example = [1, 2, 3]
tuple_example = ("Frontend", "Backend", "DevOps")

print(string_example)
print(list_example)
print(tuple_example)

# Mapping Data Type
programming_data = {
    "name": "Guido van Rossum",
    "age": 65,
    "language_rankings": {"Python": 1, "Java": 2, "JavaScript": 3},
}

print(programming_data)

# Set Data Types
unique_programming_languages = {"Python", "Java", "C++"}
unique_frameworks = {"Django", "Flask", "Spring"}

frozen_unique_programming_languages = frozenset(["Python", "Java", "C++"])
frozen_unique_frameworks = frozenset(("Django", "Flask", "Spring"))

print(unique_programming_languages)
print(unique_frameworks)
print(frozen_unique_programming_languages)
print(frozen_unique_frameworks)

team_completed_project = True
if team_completed_project:
    print("Team has completed the programming project")
else:
    print("Team has not completed the programming project")

# None type
programmer_stat = None
print(programmer_stat)

# Using f-strings
developer_name = "Guido van Rossum"
language_created = "Python"

print(f"{developer_name} created the {language_created} programming language.")

# Using str.format()
developer_name = "Brendan Eich"
language_created = "JavaScript"

print("{} created the {} programming language.".format(developer_name, language_created))

# Displaying Dictionaries
language_creators = {
    "Python": "Guido van Rossum",
    "JavaScript": "Brendan Eich",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}

print(language_creators)

language_name = "Python"
version = 3.11
print(f"{language_name} has version {version}.")

programmer_name = "Ada Lovelace"
lines_of_code = 1000
print("{} has written {} lines of code.".format(programmer_name, lines_of_code))

top_programming_languages = ["Python", "JavaScript", "Java", "C#"]
print(top_programming_languages)

programmer_stats = {
    "name": "Kevin De Coder",
    "team": "Code City",
    "projects": 10,
    "contributions": 18,
}
print(
    f"{programmer_stats['name']} from {programmer_stats['team']} has completed {programmer_stats['projects']} projects and provided {programmer_stats['contributions']} contributions."
)

# Basic Syntax Example for Integer Conversion:
# Prompting the user for input and converting the input to an integer
age = int(input("Enter your age: "))

# using the converted input:
print("Your age is: ", age)

# float convertion:
# Prompting the user for input and converting the input to a float
height = float(input("Enter your height in meters: "))
print("Your height is: ", height)

# Syntax Example for Handling Decimal Inputs:
# First, convert the string to a float, then convert the float to an integer
age2 = int(float(input("Enter your age: ")))
print("Your age is: ", age2)

# Programming Project
project_name = input("Enter the name of the programming project: ")
project_deadline = input("Enter the deadline of the project (MM/DD/YYYY): ")
project_language = input("Enter the programming language used for the project: ")

print("Programming Project Details:")
print("Project Name:", project_name)
print("Project Deadline:", project_deadline)
print("Programming Language:", project_language)

# Pass Accuracy
player_name = input("Enter the player's name: ")
total_passes = int(input("Enter the total number of passes made by the player: "))
successful_passes = int(input("Enter the number of successful passes made by the player: "))

pass_accuracy = (successful_passes / total_passes) * 100

print("Player:", player_name)
print("Pass Accuracy: {:.2f}%".format(pass_accuracy))