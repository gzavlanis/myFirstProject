import random
import math
from collections import Counter

random_page = random.randint(1,200)
print(random_page)

artists = ["Beyonce", "Coldplay", "Bruno Mars", "Dua Lipa", "John Legend"]
random_artist = random.choice(artists)
print(random_artist)

genres = ["Comedy", "Drama", "Action", "Horror", "Sci-fi"]
random.shuffle(genres)
print(genres)

random_temperature = random.uniform(-10, 40)
print(random_temperature)

locations = ["Paris", "Tokyo", "New York", "Sydney", "Cairo", "London", "Rio de Janeiro", "Berlin", "Toronto", "Cape Town"]
random_destinations = random.sample(locations, 3)
print(random_destinations)

revenue = 500000
costs = 325000

gross_profit = revenue - costs
profit_margin = math.floor((gross_profit / revenue) * 100)
print(f"Gross Profit Margin: {profit_margin}%")

total_sales = 1500
total_days = 30

average_sales = math.ceil(total_sales / total_days)
print(f"Mean Daily Sales: {average_sales}")

successful_opens = 1250
total_emails_sent = 5000

open_rate = (successful_opens / total_emails_sent) * 100
print(f"Email Open Rate: {math.floor(open_rate)}%")

current_sales = 5000
growth_rate = 0.05

predicted_sales = current_sales * math.exp(growth_rate)
print(f"Predicted Sales Next Month: ${round(predicted_sales, 2)}")

years = 5
annual_profit = 100
discount_rate = 0.05

# Calculate present value of each year's profit and sum them
clv = sum([annual_profit * math.pow((1 - discount_rate), year) for year in range(years)])

print(f"Customer Lifetime Value: ${round(clv, 2)}")

ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Mint', 'Chocolate', 'Vanilla', 'Mint', 'Strawberry']

flavor_counter = Counter(ice_cream_flavors)
print(flavor_counter)

books = ['1984', 'To Kill a Mockingbird', '1984', 'The Great Gatsby', '1984', 'To Kill a Mockingbird', 'The Catcher in the Rye']

book_counter = Counter(books)
print(dict(book_counter))

integers = [1, 2, 3, 1, 2, 1, 4, 5]
integer_counter = Counter(integers)
print(integer_counter)

most_common_integer, frequency = integer_counter.most_common(1)[0]
print(f"The most common integer is {most_common_integer} and it appears {frequency} times.")

daily_tasks = ['email', 'meeting', 'code', 'email', 'lunch', 'code']
task_counter = Counter(daily_tasks)

print(task_counter)

weekly_tasks = {
    'email': 40,
    'meeting': 20,
    'code': 60,
    'documentation': 30,
    'review': 50
}

top_tasks = Counter(weekly_tasks)
top_three_tasks = top_tasks.most_common(3)

print(top_three_tasks)

company_earnings = [
    ('Apple', 150),
    ('Google', 120),
    ('Microsoft', 140),
    ('Amazon', 160),
    ('Facebook', 130)
]

earning_counter = Counter(dict(company_earnings))
top_earning_company = earning_counter.most_common(1)

print(top_earning_company)

tags = ['bug', 'feature', 'bug', 'bug', 'improvement', 'bug']
tag_counter = Counter(tags)

print(tag_counter)

interactions = ['Google', 'Apple', 'Microsoft', 'Google', 'Apple', 'Amazon']
interaction_counter = Counter(interactions)
most_frequent_interaction = interaction_counter.most_common(1)

print(most_frequent_interaction)

events = ['login', 'logout', 'login', 'data_change', 'login', 'logout']
event_counter = Counter(events)

print(event_counter)

preferences = ['dark_mode', 'light_mode', 'dark_mode', 'auto_mode', 'dark_mode', 'light_mode', 'auto_mode', 'dark_mode']
preference_counter = Counter(preferences)

print(preference_counter)

outcomes = ['success', 'failure', 'success', 'pending', 'success', 'failure', 'pending', 'success']
outcome_counter = Counter(outcomes)

print(outcome_counter)

points = [('team1', 2), ('team2', 3), ('team1', 1), ('team2', 2), ('team1', 2)]
points_counter = Counter()

for team, point in points:
    points_counter[team] += point

print(points_counter)

matchups = ['team1 vs. team2', 'team1 vs. team2', 'team1 vs. team3', 'team2 vs. team3', 'team1 vs. team2']
matchup_counter = Counter(matchups)

print(matchup_counter)

print(math.degrees(math.pi / 2))
print(math.factorial(20))