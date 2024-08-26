import time

soccer_players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé"]

for player in soccer_players:
    print(player)

for i in range(0, 10, 2):
    print(i)

soccer_positions = {
    "Lionel Messi": "Forward",
    "Cristiano Ronaldo": "Forward",
    "Neymar": "Forward",
    "Kylian Mbappé": "Forward"
}

for player, position in soccer_positions.items():
    print(player, "plays as a", position)

for i in range(1, 4):  # This will loop through numbers 1 to 3
    for j in range(1, 4):  # This will also loop through numbers 1 to 3
        print(i * j, end = "\t")  # Multiply and print the result. \t is for tab space.
    print()

footballers = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé"]

for player in footballers:
    if player == "Neymar":
        print(f"{player} is in the list! Stop the search!")
        break
    print(player)

for player in footballers:
    if player == "Neymar":
        continue  # Skip Neymar
    print(player)

for player in footballers:
    if player == "Neymar":
        pass  # Do nothing and play on!
    print(player)

completed_projects = [1, 1, 1, 1, 1]  # each 1 represents a completed project

total_projects = 0
for project in completed_projects:
    total_projects += project

print("Total completed projects:", total_projects)

"Employee Project Tracker"

employee_projects = {"Alice": 5, "Bob": 3, "Charlie": 8, "David": 2}

top_performer = ""
max_projects = 0
for employee, projects in employee_projects.items():
    if projects > max_projects:
        max_projects = projects
        top_performer = employee

print("Top performer:", top_performer, "with", max_projects, "projects")

completed_projects = [2, 3, 1, 0, 4]

task_distribution = {}
for project in completed_projects:
    if project in task_distribution:
        task_distribution[project] += 1
    else:
        task_distribution[project] = 1

print("Task distribution:", task_distribution)

team_projects = {"Team Alpha": [3, 2, 1, 4, 2], "Team Beta": [2, 1, 3, 2, 0]}

for team, projects in team_projects.items():
    total_projects = sum(projects)
    print(f"The total projects completed by {team} are {total_projects}.")

project_assignments = ["Alice", "Bob", "Alice", "Bob", "Alice", "Charlie", "Alice"]

assignment_count = {}
for employee in project_assignments:
    if employee in assignment_count:
        assignment_count[employee] += 1
    else:
        assignment_count[employee] = 1

print(assignment_count)

daily_tasks = [3, 2, 1, 4, 2, 0, 1, 3, 2, 2]

total_tasks = 0
for tasks in daily_tasks:
    total_tasks += tasks

average_tasks = total_tasks / len(daily_tasks)
print(f"The average tasks per day is {average_tasks}.")

employees = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Engineer"},
    {"name": "Charlie", "role": "Engineer"},
    {"name": "David", "role": "Manager"},
]

roles = {}
for employee in employees:
    role = employee["role"]
    if role in roles:
        roles[role].append(employee["name"])
    else:
        roles[role] = [employee["name"]]

print(roles)

employee_scores = [
    {"name": "Alice", "score": 8.5},
    {"name": "Bob", "score": 8.7},
    {"name": "Charlie", "score": 8.6},
    {"name": "David", "score": 8.7},
]

for i in range(len(employee_scores)):
    for j in range(len(employee_scores) -1):
        if employee_scores[j]["score"] < employee_scores[j + 1]["score"]:
            employee_scores[j], employee_scores[j + 1] = employee_scores[j + 1], employee_scores[j]

print(employee_scores)

count = 5

while count > 0:
  print("Count:", count)
  count = count - 1

user_input = ""

while user_input != "quit":
  user_input = input("Enter something (type 'quit' to exit): ")
  print("You entered:", user_input)

tasks_completed = 0

while tasks_completed < 5:
    print("Task completed!")
    tasks_completed += 1

tasks_completed = 0

while True:
    print("Task completed!")
    tasks_completed += 1

    if tasks_completed >= 5:
        break

days = 0

while days < 3:
    print("Day:", days + 1)
    tasks_completed = 0

    while tasks_completed < 5:
        print("Task completed!")
        tasks_completed += 1

    days += 1

tasks_completed = 0

while tasks_completed < 5:
    print("Task completed!")
    tasks_completed += 1
else:
    print("Excellent! You've completed", tasks_completed, "tasks today!")

# Task Tracker
tasks_remaining = 5

while tasks_remaining > 0:
    print(f"Task {tasks_remaining} in progress...")
    tasks_remaining -= 1

print("All tasks completed! Great job! 👏")

# Element Ranking
elements = ["Element 1", "Element 2", "Element 3", "Element 4", "Element 5"]
index = 0

while index < len(elements):
    print(f"Rank {index + 1}: {elements[index]}")
    index += 1

# Accuracy Tracker
successful_attempts = 0
total_attempts = 10

while successful_attempts < total_attempts:
    print(f"Successful attempt {successful_attempts + 1}")
    successful_attempts += 1

accuracy = (successful_attempts / total_attempts) * 100
print(f"Accuracy: {accuracy}% 🎯")

# Score Difference Calculator
team_a_score = 0
team_b_score = 0
rounds = 3
round_count = 0

while round_count < rounds:
    team_a_score += 2
    team_b_score += 1
    round_count += 1

score_difference = team_a_score - team_b_score
print(f"Score difference: {score_difference}")

results = ["Success", "Success", "Failure", "Success", "Success", "Success", "Failure", "Success"]
i = 0
max_streak_count = 0
current_streak_count = 0

# Outer while loop to go through the entire list.
while i < len(results):

    # Inner while loop to count consecutive successes.
    while i < len(results) and results[i] == "Success":
        current_streak_count += 1
        i += 1

    # Update max_streak_count using max() function to avoid 'if'.
    max_streak_count = max(max_streak_count, current_streak_count)

    # Reset current_streak_count to 0 for the next streak count.
    current_streak_count *= 0  # Same as setting to 0.

    # Increment i to move past the "Failure".
    i += (i < len(results))  # This will add 1 if i is less than len(results), otherwise adds 0.

# Final Output
print(f"The longest success streak is {max_streak_count} iterations. 🔥")

# High-Performance Locator
performances = [1, 2, 1, 3, 4, 2, 5, 2]

i = 0
while i < len(performances) and performances[i] < 5:
    i += 1

if i < len(performances):
    print(f"The first high-performing instance was at index {i + 1} with a score of {performances[i]}. 🚀")
else:
    print("There were no high-performing instances.")

# Performance Tracker
performances = [5, 4.5, 4.7, 4.9, 5.2, 4.8]
i = 0
start_time = time.time()

while i < len(performances) and time.time() - start_time < 1:
    print(f"Instance {i + 1} performance: {performances[i]}")
    time.sleep(0.5)  # Adding a delay of 0.5 seconds
    i += 1

while i < len(performances): # Notice we removed the constraint `and time.time() - start_time < 1` from this line
    print(f"Instance {i + 1} performance: {performances[i]}")
    time.sleep(0.5)  # Adding a delay of 0.5 seconds
    i += 1

# Substitution Manager
squad = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5']
subs = ['Sub 1', 'Sub 2', 'Sub 3']
i = 0

while i < len(subs):
    print(f"Substitute: {squad[i]} out, {subs[i]} in")
    squad[i] = subs[i]
    i += 1

print(f"Final squad: {squad}")

# Countdown Timer
countdown = 10

while countdown >= 0:
    print(f"Starting in {countdown} seconds! ⏰")
    time.sleep(1)
    countdown -= 1

print("Let's go!")

# what to choose
projects = [("Project A", "June 25"), ("Project B", "July 2"), ("Project C", "July 9"), ("Project D", "July 16")]

for project, deadline in projects:
    print(f"{project} is due on {deadline}.")

current_skill_level = 5
target_skill_level = 10
practice_sessions = 0

while current_skill_level < target_skill_level:
    practice_sessions += 1
    current_skill_level += 1

print(f"You need {practice_sessions} more sessions to reach the target skill level.")

# Mixing For and While Loops: A Dance of Iteration
dance_moves = ["Twist", "Moonwalk", "Floss", "Robot", "Macarena"]
max_moves = 3  # Maximum moves to perform
move_performed = 0  # To keep track of moves performed

print("Let's Dance! 🌟💃🕺")

while move_performed < max_moves:
    for move in dance_moves:
        user_input = input(f"Performing {move}! Type 'Next' to perform the next move: ")
        if user_input.lower() == 'next':
            print(f"{move} performed! 🎉")
            move_performed += 1
            if move_performed >= max_moves:
                print("You've reached the limit of moves! 🛑")
                break
        else:
            print("Keep going, you're doing great! 💃🕺")