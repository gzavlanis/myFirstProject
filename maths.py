# Addition
a = 5
b = 3
result = a + b
print(result)

# subtraction
result2 = a - b
print(result2)

# Multiplication
result3 = a * b
print(result3)

# Division
result4 = a / b
print(result4)

# Modulus
result5 = a % b
print(result5)

# Exponentiation
result6 = a ** b
print(result6)

# Floor Division
result7 = a // b
print(result7)

# Accessing Characters in Strings
player_name = "Lionel Messi"
first_char = player_name[0]
second_char = player_name[1]
third_char = player_name[2]
last_char = player_name[-1]
pre_last_char = player_name[-2]

print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)
print("Last character:", last_char)
print("Pre-last character:", pre_last_char)

# Concatenation
first_name = "Lionel"
last_name = "Messi"
full_name = first_name + " " + last_name
print(full_name)

# Slicing
player_name = "Cristiano Ronaldo"
first_name = player_name[:9]
last_name = player_name[10:]
print(first_name)
print(last_name)

# Replacing
team_name = "Real Madrid"
new_team_name = team_name.replace("Real", "Atletico")
print(new_team_name)

# Formatting
player_name = "Neymar"
goals = 19
assists = 12
stats = "{} scored {} goals and provided {} assists last season."
formatted_stats = stats.format(player_name, goals, assists)
print(formatted_stats)

# Upper and Lower Case
team_name = "Barcelona"
uppercase_team_name = team_name.upper()
lowercase_team_name = team_name.lower()
print(uppercase_team_name)
print(lowercase_team_name)

# Splitting
player_data = "Lionel Messi, 34, Forward"
data_list = player_data.split(", ")
print(data_list)

# Joining
data_list = ['Lionel Messi', '34', 'Forward']
player_data = ", ".join(data_list)
print(player_data)

# Stripping
team_name = "  Barcelona  "
stripped_team_name = team_name.strip()
print(stripped_team_name)

pi = 3.14159
print(f"Value of pi up to two decimal places: {pi:.2f}")

def greet(name):
    return f"Hello, {name}!"

print(greet("John"))

# Padding and Aligning
x = 5
print(f"{x:0>3}")

# Specifying Precision
pi = 3.14159
print(f"{pi:.3f}")

# Using f-strings with Dictionary
person = {'name': 'John', 'age': 30}
print(f"{person['name']} is {person['age']} years old.")

# Using f-strings with List
fruits = ['apple', 'banana', 'cherry']
print(f"My favorite fruit is {fruits[0]}.")

print(f"2 + 2 equals {2 + 2}.")

# Multiline f-strings
name = "John"
age = 30
print(f"""
    Name: {name}
    Age: {age}
""")

# escape quotes
print(f"He said, \"Hello, {name}!\"")

# Using Escape Characters for Quotes
quote = "\"You have to fight to reach your dream. You have to sacrifice and work hard for it.\" - Lionel Messi"
print(quote)

top_scorers = "Rank\tPlayer\t\tGoals\n1\tMohamed Salah\t22\n2\tHarry Kane\t21\n3\tSergio Agüero\t21"
print(top_scorers)

# Python Casting
pages = 250
pages_float = float(pages)
print(pages_float)

average_hours = 12.75
average_hours_int = int(average_hours)
print(average_hours_int)

items = 15
items_str = str(items)
print(items_str)
print(type(items_str))

steps_str = "10000"
steps = int(steps_str)
print(steps)

# Concatenation
person1 = "Alice Johnson"
occupation1 = "Software Engineer"

person2 = "Bob Smith"
occupation2 = "Graphic Designer"

person3 = "Charlie Brown"
occupation3 = "Data Analyst"

result1 = person1 + " - " + occupation1
result2 = person2 + " - " + occupation2
result3 = person3 + " - " + occupation3

print(result1)
print(result2)
print(result3)

# Slicing
person_info = "Emma Watson, Actress"
first_name = person_info[:4]
last_name = person_info[5:11]
occupation = person_info[13:]

print(first_name)
print(last_name)
print(occupation)

# Replacing
company_info = "John Doe works for Microsoft."
new_company_info = company_info.replace("Microsoft", "Google")
print(new_company_info)

# Formatting
person_name = "Jane Smith"
activity1 = "hiking"
activity2 = "painting"

formatted_string = "{} enjoys {} and {}.".format(person_name, activity1, activity2)
print(formatted_string)

# Upper and Lower Case
city_name = "New York City"

uppercase_city_name = city_name.upper()
lowercase_city_name = city_name.lower()

print(uppercase_city_name)
print(lowercase_city_name)

# Splitting, Joining, and Stripping
person_data = "  Emily Davis, 35, Architect  "
split_data = person_data.strip().split(', ')
joined_data = '|'.join(split_data)

print(joined_data)
print('Python ' + 'rules!')
print('Scored ' + str(5))