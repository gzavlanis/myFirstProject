import random

from conditionals import is_car1_better

achievers_data = [
    {"name": "Performer A", "score": 5},
    {"name": "Performer B", "score": 6},
    {"name": "Performer C", "score": 8},
    {"name": "Performer D", "score": 7},
    {"name": "Performer E", "score": 6}
]

for i in range(len(achievers_data)):
    max_index = i
    j = i + 1
    while j < len(achievers_data):
        if achievers_data[j]["score"] > achievers_data[max_index]["score"]:
            max_index = j
        j += 1
    achievers_data[i], achievers_data[max_index] = achievers_data[max_index], achievers_data[i]

for performer in achievers_data:
    print(f"{performer['name']} scored {performer['score']} in the competition.")

print('________________________________________________________________________________________')

group_data = {
    "A": {"events": 12, "score": 21},
    "B": {"events": 12, "score": 22},
    "C": {"events": 12, "score": 27},
    "D": {"events": 12, "score": 20},
    "E": {"events": 12, "score": 23},
    "F": {"events": 12, "score": 24},
    "G": {"events": 12, "score": 19},
    "H": {"events": 12, "score": 18}
}

threshold = 1.75

for group, data in group_data.items():
    total_score = data["score"]
    total_events = data["events"]
    average_score = total_score / total_events

    # While loop to ensure average score is at least the threshold
    while average_score < threshold:
        # Simulate adding an event with a random score between 2 and 3
        new_score = random.uniform(2, 3)
        total_score += new_score
        total_events += 1
        average_score = total_score / total_events
        print(f"Group {group}'s average score is lower than the threshold. We add an event with score {new_score:.2f}. The new average is {average_score:.2f}")

    print(f"Group {group}: Final average {average_score:.2f}.")

print('__________________________________________________________________________________________')

nationalities = [
    {"country": "Spain", "players": 70},
    {"country": "Germany", "players": 65},
    {"country": "France", "players": 60},
    {"country": "England", "players": 55},
    {"country": "Italy", "players": 50}
]

for i in range(len(nationalities)):
    max_index = i
    j = i + 1
    while j < len(nationalities):
        if nationalities[j]["players"] > nationalities[max_index]["players"]:
            max_index = j
        j += 1
    nationalities[i], nationalities[max_index] = nationalities[max_index], nationalities[i]

for country in nationalities:
    print(f"{country['country']} has {country['players']} players in the Champions League.")

print('__________________________________________________________________________________________')

patients_data = [
    {"name": "Patient A", "visits": [5, 6, 4, 6, 7, 5]},
    {"name": "Patient B", "visits": [6, 5, 5, 6, 5, 4]},
    {"name": "Patient C", "visits": [7, 6, 7, 5, 6, 6]},
    {"name": "Patient D", "visits": [6, 5, 6, 5, 5, 4]},
    {"name": "Patient E", "visits": [5, 4, 5, 6, 5, 6]}
]

for patient in patients_data:
    total_visits = 0
    i = 0
    while i < len(patient["visits"]):
        total_visits += patient["visits"][i]
        i += 1
    average_visits = total_visits / len(patient["visits"])
    print(f"{patient['name']} has an average of {average_visits:.2f} visits per month.")

print('__________________________________________________________________________________________')

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num > 1:  # primes are greater than 1
        i = 2
        while i < num:
            if (num % i) == 0:  # check for factor
                print(num, "is not a prime number.")
                break
            i += 1
        else:  # else part of the while loop (not the for loop)
            print(num, "is a prime number.")

print('__________________________________________________________________________________________')

for num in range(2, 10):  # tables for 2, 3, and 4
    multiplier = 1
    while multiplier <= 10:
        print(num, 'x', multiplier, '=', num * multiplier)
        multiplier += 1
    print()  # for empty line after each table

print('__________________________________________________________________________________________')

strings = ["apple", "banana", "cherry", "zavlanis"]

for s in strings:
    i = 0
    vowel_count = 0
    while i < len(s):
        if s[i] in 'aeiou':
            vowel_count += 1
        i += 1
    print("There are", vowel_count, "vowels in", s)

print('___________________________________________________________________________________________')

print([i for i in range(4)])
print('___________________________________________________________________________________________')

x = 0
y = 10
while y < 90:
    y = y + 20
    x = x + y
    print(x, y)
print('___________________________________________________________________________________________')

x = 15
while x <= 30:
    x = x + 5
    print(x)
print(x)
print('___________________________________________________________________________________________')

for i in range(1, 6):
    print(str(i) * i)
print('___________________________________________________________________________________________')

sum = 0
for i in range(0, 5):
    sum = sum + i
print(sum)
print('___________________________________________________________________________________________')

while True:
    print("Hello")
    break

print('___________________________________________________________________________________________')

arr = [2,3,4]
num_of_evens = 0

for i in arr:
    j = 0
    while j <= i:
        if j % 2 == 0:
            num_of_evens += 1
        j += 1

print(num_of_evens)

