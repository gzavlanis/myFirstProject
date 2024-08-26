import re

text = "My phone number is 123-456-7890"
pattern = r'\d'

results = re.findall(pattern, text)
print(results)

text2 = "I am learning Python programming"
pattern = r'\bPython\b'

result = re.search(pattern, text2)
print(result)
print(result.group())
print()

text = "Hidden within this message is Agent JF231. They're our top operative."
pattern = r"\bAgent [A-Z0-9]+\b"

match = re.search(pattern, text)

if match:
    print("Agent's code found:", match.group())
else:
    print("Agent remains undetected.")
print()

text = "Project Falcon, with a budget of 23000, is our largest undertaking."
pattern = r'\bbudget of (\d+)\b'

match = re.search(pattern, text)

if match:
    print("Budget located:", match.group(1))
else:
    print("No budget found.")
print()

text = "Dr. Rachel is a archaeologist working on artifact XJ12."
pattern = r'\bis a (\w+)\b'

match = re.search(pattern, text)

if match:
    print("Dr. Rachel's profession:", match.group(1))
else:
    print("No profession found.")
print()

pattern = r'^([A-Z][a-z]+)\s([A-Z][a-z]+)$'
string = "Alpha Bravo"

result = re.match(pattern, string)

if result:
    print("Code name confirmed:", result.group())
else:
    print("Invalid code name")
print()

pattern = r'^(CEO|CFO|CTO|CMO)$'
string = "CTO"

result = re.match(pattern, string)

if result:
    print("Title verified:", result.group())
else:
    print("Title not recognized")
print()

pattern = r'^([1-9][0-9]?)$'
string = "34"

result = re.match(pattern, string)

if result:
    print("Age entry validated:", result.group())
else:
    print("Invalid age entry")
print()

text = "Jane Doe and John Smith are prominent figures in their respective fields."
pattern = r'[A-Z][a-z]+ [A-Z][a-z]+'

names = re.findall(pattern, text)
print(names)
print()

text = "The planet Earth is approximately 4.5 billion years old and has 7.8 billion inhabitants."
pattern = r'\d+'

numbers = re.findall(pattern, text)
print(numbers)
print()

text = "The Apollo 11 moon landing took place on 20/07/1969, while the Hubble Space Telescope was launched on 24/04/1990."
pattern = r'\d{2}/\d{2}/\d{4}'

dates = re.findall(pattern, text)
print(dates)
print()

people_data = "Jane Doe (Engineer), John Smith (Doctor), Emma Watson (Actress), Elon Musk (Entrepreneur), Albert Einstein (Physicist)"
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

for match in re.finditer(pattern, people_data):
    print(match.group())
print()

people_data = "Jane Doe (Engineer), John Smith (Doctor), Emma Watson (Actress), Elon Musk (Entrepreneur), Albert Einstein (Physicist)"
pattern = r'\((\w+)\)'

for match in re.finditer(pattern, people_data):
    print(match.group(1))
print()

names = "Albert Einstein, Carl Einstein, Louisa Einstein"
pattern = "Einstein"
replacement = "Newton"

new_names = re.sub(pattern, replacement, names)
print(new_names)
print()

dates = "Event on 12-05-2021, Event on 15-05-2021, Event on 20-05-2021"
pattern = r"(\d{2})-(\d{2})-(\d{4})"
replacement = r"\3-\2-\1"

new_dates = re.sub(pattern, replacement, dates)
print(new_dates)
print()

authors = "George Orwell, J.K. Rowling, J.R.R. Tolkien, Stephen King"
pattern = ", "

result = re.split(pattern, authors)

print(result)
print()

conference_data = "2023-06-12|Neural Networks and Deep Learning|Washington DC"
pattern = r"\|| - "

result = re.split(pattern, conference_data)

print(result)
print()

# Examples
posts = [
    "@user1: Python is amazing!",
    "Have to agree with @user2 on this one!",
    "Check out the latest blog post from @user3",
]

username_pattern = re.compile(r"@(\w+)")

for post in posts:
    username = username_pattern.search(post)
    if username:
        print(f"Username: {username.group(1)}")
print()

posts = [
    "Learning #Python is fun! #coding",
    "Loving this #AI tutorial. #machinelearning",
    "Check out my latest #deeplearning project!",
]

hashtag_pattern = re.compile(r"#(\w+)")

for post in posts:
    hashtags = hashtag_pattern.findall(post)
    print(f"Hashtags: {hashtags}")
print()

schedule = [
    "2023-07-01: Opening Keynote",
    "2023-07-02: Python Workshop",
    "2023-07-03: AI Panel Discussion",
]

date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")

for event in schedule:
    date = date_pattern.search(event)
    print(f"Date: {date.group()}")
print()

orders = [
    "Python Book to John Doe",
    "Machine Learning Course to Jane Doe",
    "AI Project Template to Michael Smith",
]

product_customer_pattern = re.compile(r"(.*?) to (.*?)$")

for order in orders:
    match = product_customer_pattern.search(order)
    print(f"Product: {match.group(1)}, Customer: {match.group(2)}")
print()

trades = [
    "Bought 100 shares of MSFT at $200 each",
    "Sold 50 shares of GOOG at $1500 each",
    "Bought 200 shares of AAPL at $125 each",
]

trade_pattern = re.compile(r"(\w+) (\d+) shares of (\w+) at \$(\d+) each")

for trade in trades:
    match = trade_pattern.search(trade)
    print(f"Action: {match.group(1)}, Quantity: {match.group(2)}, Symbol: {match.group(3)}, Price: {match.group(4)}")
print()

data = 'John Doe: $7,000, Jane Doe: $8,000, Michael Smith: $10,000'
pattern = r"(\w+\s\w+):\s\$(\d+,\d+)"

matches = re.findall(pattern, data)

for match in matches:
    salesperson, sales = match
    print(f'{salesperson} made sales worth ${sales}.')
print()

data = 'Python Book: SSSMS, Machine Learning Course: SSSSS, AI Project Template: MSSMS'
pattern = r'([^:]+): ([SMS]+)'

matches = re.findall(pattern, data)

for match in matches:
    product, sales = match
    product = product.strip(", ") # Remove any leading/trailing whitespace
    if 'M' not in sales:
        print(f'The {product} is successful.')
print()

data = 'Avengers Endgame: $357M, Avatar: $77M, Titanic: $28M'
pattern = r'([^:]+): \$(\d+M)'

matches = re.findall(pattern, data)

for match in matches:
    movie, gross = match
    if int(gross[:-1]) > 100:
        print(f'The movie {movie} had a high grossing opening weekend!')
print()

data = 'Startup1 was valued at $10M and is now worth $50M, Startup2 was valued at $1M and is now worth $10M, Startup3 was valued at $5M and is now worth $7M'
pattern = r'(\w+) was valued at \$(\d+M) and is now worth \$(\d+M)'

matches = re.findall(pattern, data)

for match in matches:
    startup, initial_value, current_value = match
    if int(current_value[:-1]) > 2 * int(initial_value[:-1]):
        print(f'{startup} has grown significantly since its inception!')
print()

data = 'The Startup of the Year award was won by Startup1 on 2023-05-28 after a stiff competition.'
pattern = r'The (.*?) award was won by (.*?) on (\d{4}-\d{2}-\d{2}) after (.*?)\.'

match = re.search(pattern, data)

if match:
    event, winner, date, details = match.groups()
    print(f'The {event} award was won by {winner} on {date}. Details: {details}.')

""" Notes """
"""
    \d: Matches any digit (0-9)
    \D: Matches any character that is not a digit (i.e., non-numeric characters)
    \w: Matches any word character (a-z, A-Z, 0-9, and _)
    \s: Matches any whitespace character (spaces, tabs, and line breaks)
    .: Matches any character except a newline
    ^: Matches the start of a string
    $: Matches the end of a string
    *: Matches zero or more occurrences of the preceding character
    +: Matches one or more occurrences of the preceding character
    ?: Matches zero or one occurrence of the preceding character
    {n}: Matches exactly n occurrences of the preceding character
    {n,}: Matches n or more occurrences of the preceding character
    {n,m}: Matches at least n and at most m occurrences of the preceding character
    [...]: Matches any one of the characters inside the brackets
    [^...]: Matches any character not inside the brackets
    |: Matches either the expression before or the expression after the | character
    \B: Matches at a position that is not a word boundary
"""
