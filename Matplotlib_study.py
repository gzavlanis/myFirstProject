import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
avg_temperatures = [0, 1, 5, 9, 14, 18, 21, 20, 16, 10, 5, 1]

plt.bar(months, avg_temperatures)
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Average Monthly Temperatures")
# plt.show()

avg_rainfall = [78, 60, 92, 55, 110, 95, 75, 65, 85, 70, 80, 90]
plt.bar(months, avg_rainfall)
plt.xlabel("Month")
plt.ylabel("Average Rainfall (mm)")
plt.title("Average Monthly Rainfall")
# plt.show()

investment_types = ['Stocks', 'Bonds', 'Mutual Funds', 'Real Estate', 'Cryptocurrency']
returns = [7.4, 2.8, 5.2, 9.3, 14.2]

fig, ax = plt.subplots(figsize = (10, 5))
ax.bar(investment_types, returns)
ax.set_title('Investment Returns in 2023')
ax.set_xlabel('Investment Type')
ax.set_ylabel('Returns (%)')
# plt.show()

# Line Plots
years = np.arange(2000, 2011)
data1 = np.random.randint(20, 50, 11)
data2 = np.random.randint(30, 60, 11)

plt.figure(figsize = (12, 6))
plt.plot(years, data1, label = 'Dataset 1', linestyle = '-', color = 'blue', marker = 'o')
plt.plot(years, data2, label = 'Dataset 2', linestyle = '--', color = 'red', marker = 's')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Value Trends for Dataset 1 and Dataset 2 (2000-2010)')
plt.legend()
# plt.show()

data3 = np.random.randint(40, 70, 11)

plt.figure(figsize = (12, 6))
plt.plot(years, data1, label = 'Dataset 1', linestyle = '-', color = 'blue', marker = 'o')
plt.plot(years, data2, label = 'Dataset 2', linestyle = '--', color = 'red', marker = 's')
plt.plot(years, data3, label = 'Dataset 3', linestyle = '-.', color = 'green', marker = '^')

plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Value Trends for Dataset 1, 2, and 3 (2000-2010)')
plt.legend()
# plt.show()

# Example 1: Time-Series Data Comparison
years = np.arange(2010, 2022)
dataset1 = np.random.randint(200, 500, 12)
dataset2 = np.random.randint(150, 450, 12)

plt.figure(figsize = (12, 6))
plt.plot(years, dataset1, label = 'Dataset 1', linestyle = '-', color = 'purple', marker = 'D')
plt.plot(years, dataset2, label = 'Dataset 2', linestyle = ':', color = 'orange', marker = 'o')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Time-Series Data Comparison (2010-2021)')
plt.legend()
# plt.show()

# Example 2: Displaying Annual Trends
years = np.arange(2010, 2021)
category1 = np.random.randint(50,100,11)
category2 = np.random.randint(100,150,11)
category3 = np.random.randint(150,200,11)

plt.figure(figsize=(12, 6))
plt.plot(years, category1, label = 'Category 1', linestyle = '-', color = 'blue', marker = 'o')
plt.plot(years, category2, label = 'Category 2', linestyle = '--', color = 'green', marker = '^')
plt.plot(years, category3, label = 'Category 3', linestyle = ':', color = 'red', marker = 's')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Annual Trends for Category 1, 2, and 3 (2010-2020)')
plt.legend()
# plt.show()

identifier = ['ID1', 'ID2', 'ID3', 'ID4', 'ID5']
var_1 = [30, 29, 41, 27, 23]
var_2 = [9, 3, 7, 6, 9]

plt.figure(figsize = (10, 5))
plt.scatter(var_1, var_2)

for i, id in enumerate(identifier):
    plt.annotate(id, (var_1[i], var_2[i]))

plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.title('Variable 1 vs Variable 2')
# plt.show()

# Example 1: Customizing Marker Styles
plt.figure(figsize = (10, 5))
plt.scatter(var_1, var_2, marker = '^', s = 80, edgecolors = 'black', linewidths = 1)

for i, id in enumerate(identifier):
    plt.annotate(id, (var_1[i], var_2[i]))

plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.title('Variable 1 vs Variable 2 with Custom Marker Styles')
# plt.show()

# Example 2: Customizing Colors
np.random.seed(0)
n = 50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = np.pi * (15 * np.random.rand(n)) ** 2

plt.figure(figsize = (10, 5))
plt.scatter(x, y, s = area, c = colors, alpha = 0.5, cmap = 'viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot with Custom Colors and Colormaps')
plt.colorbar(label = 'Color scale')
# plt.show()

# Example 3: Customizing Axis Labels and Title
plt.figure(figsize=(10, 5))
plt.scatter(var_1, var_2)

for i, id in enumerate(identifier):
    plt.annotate(id, (var_1[i], var_2[i]))

plt.xlabel('Variable 1', fontsize = 15, color = 'blue')
plt.ylabel('Variable 2', fontsize = 15, color = 'red')
plt.title('Variable 1 vs Variable 2 with Custom Axis Labels and Title', fontsize = 20, color = 'green')
# plt.show()

# Example 4: Adding Gridlines
plt.figure(figsize = (10, 5))
plt.scatter(var_1, var_2)

for i, id in enumerate(identifier):
    plt.annotate(id, (var_1[i], var_2[i]))

plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.title('Variable 1 vs Variable 2 with Gridlines')
plt.grid(True)
# plt.show()

# Creating a Simple Bar Plot
individuals = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
achievements = [67, 70, 66, 73, 68]

plt.figure(figsize = (12, 6))
plt.bar(individuals, achievements, color = 'orange', width = 0.4)
plt.xlabel("Individuals")
plt.ylabel("Achievements")
plt.title("Number of Achievements by Individuals")
plt.grid(axis = 'y')
# plt.show()

# Example 1: Horizontal Bar Plot
plt.figure(figsize=(12, 6))
plt.barh(individuals, achievements)
plt.xlabel('Achievements')
plt.ylabel('Individuals')
plt.title('Number of Achievements by Individuals')
# plt.show()

# Example 2: Stacked Bar Plot
individuals = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
category1 = [30, 35, 25, 35, 27]
category2 = [25, 20, 22, 27, 23]
category3 = [12, 15, 19, 11, 18]

plt.figure(figsize = (12, 6))
plt.bar(individuals, category1, label = 'Category 1')
plt.bar(individuals, category2, bottom = category1, label = 'Category 2')
plt.bar(individuals, category3, bottom = np.array(category1) + np.array(category2), label = 'Category 3')
plt.xlabel('Individuals')
plt.ylabel('Achievements')
plt.title('Achievements by Individuals and Categories')
plt.legend()
# plt.show()

# Example 3: Grouped Bar Plot
x = np.arange(len(individuals))  # the label locations
width = 0.2  # the width of the bars

plt.figure(figsize = (12, 6))
plt.bar(x - width, category1, width, label = 'Category 1')
plt.bar(x, category2, width, label = 'Category 2')
plt.bar(x + width, category3, width, label = 'Category 3')

plt.xlabel('Individuals')
plt.ylabel('Achievements')
plt.title('Achievements by Individuals and Categories')
plt.xticks(ticks = x, labels = individuals) # set the x-ticks with the list of the individuals
plt.legend()
# plt.show()

# Example 4: Error Bars
individuals = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
achievements = [67, 70, 66, 73, 68]
errors = [5, 3, 4, 6, 2]

plt.figure(figsize = (12, 6))
plt.bar(individuals, achievements, yerr = errors, capsize = 7)
plt.xlabel("Individuals")
plt.ylabel("Achievements")
plt.title("Number of Achievements by Individuals")
# plt.show()

# Creating a Simple Pie Plot
# Data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
counts = [34, 25, 15, 10, 16]

# Pie plot
plt.figure(figsize = (8, 6))
plt.pie(counts, labels = fruits, autopct = '%1.1f%%')
plt.title('Fruit Distribution in a Basket')
# plt.show()

# Data
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Pie plot
plt.figure(figsize = (8, 6))
plt.pie(counts, labels = fruits, colors = colors, autopct = '%1.1f%%', startangle = 140)
plt.title('Fruit Distribution in a Basket')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
# plt.show()

# Example 1: Exploded Pie Plot
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice (Apples)

# Pie plot
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=fruits, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title('Fruit Distribution in a Basket (Exploded Pie Plot)')
plt.axis('equal')
# plt.show()

# Example 2: Pie Plot with Percentage Labels
# Pie plot
fig, ax = plt.subplots(figsize = (8, 6))
wedges, texts, autotexts = ax.pie(counts, labels = fruits, autopct = '%1.1f%%', startangle = 140, pctdistance = 0.85)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')
plt.tight_layout()
# plt.show()

# Example 3: Nested Pie Plot
# Data
basket_labels = ['Basket 1', 'Basket 2']
basket_sizes = [80, 60]
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
fruit_sizes_basket1 = [34, 25, 15, 5, 1]
fruit_sizes_basket2 = [10, 15, 5, 20, 10]

# Pie plot
fig, ax = plt.subplots(figsize = (8, 6))

# Outer pie (baskets)
ax.pie(basket_sizes, labels = basket_labels, startangle = 90, frame = True, radius = 0.3)

# Inner pie (fruits in basket 1)
ax.pie(fruit_sizes_basket1, labels = fruits, radius = 0.3 - 0.3 * 0.6, startangle = 90, labeldistance = 0.7)

# Inner pie (fruits in basket 2)
ax.pie(fruit_sizes_basket2, labels = fruits, radius = 0.3 - 0.3 * 0.3, startangle = 90, labeldistance = 0.3)

# Equal aspect ratio ensures pie is drawn as a circle
ax.set_aspect('equal')
# plt.show()

# Example 4: Pie Plot with Custom Colors
# Data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
counts = [34, 25, 15, 10, 16]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Pie plot
plt.figure(figsize = (8, 6))
plt.pie(counts, labels = fruits, colors = colors, autopct = '%1.1f%%', startangle = 140)
plt.title('Fruit Distribution in a Basket (Custom Colors)')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
# plt.show()

# Practical example 1
# Problem 1: Line Plot
players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
goals = [23, 25, 21, 22, 19]

plt.figure(figsize = (10,6))
plt.plot(players, goals, marker = 'o')
plt.title('Goals Scored by EPL Players in a Season')
plt.xlabel('Players')
plt.ylabel('Goals Scored')
plt.grid(True)
# plt.show()

# Problem 2: Scatter Plot
goals = [23, 25, 21, 22, 19]
games = [34, 33, 34, 35, 33]

plt.figure(figsize = (10,6))
plt.scatter(games, goals)
plt.title('Goals Scored vs Games Played (Season)')
plt.xlabel('Games Played')
plt.ylabel('Goals Scored')
plt.grid(True)
# plt.show()

# Problem 3: Bar Plot
teams = ['Tottenham Hotspur', 'Liverpool', 'Manchester United', 'Leicester City', 'Tottenham Hotspur']
team_points = [65, 74, 70, 64, 65]

plt.figure(figsize = (10,6))
plt.bar(teams, team_points, color = ['blue', 'red', 'red', 'blue', 'blue'])
plt.title('EPL Team Points (Season)')
plt.xlabel('Teams')
plt.ylabel('Points')
plt.grid(True)
# plt.show()

# Problem 4: Pie Plot
players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
assists = [8, 7, 11, 6, 10]

plt.figure(figsize = (10,6))
plt.pie(assists, labels = players, autopct='%1.1f%%')
plt.title('Assists Distribution among EPL Players (Season)')
# plt.show()

# Data
years = [2018, 2019, 2020, 2021, 2022]
person_A_performance = [37, 34, 36, 25, 30]
person_B_performance = [25, 26, 21, 31, 29]

# Line Plot
plt.figure(figsize = (12, 6))
plt.plot(years, person_A_performance, marker = 'o', label = 'Person A')
plt.plot(years, person_B_performance, marker = 'o', label = 'Person B')

# Titles, Labels and Legends
plt.title("Performance Metrics of Person A and Person B (2018-2022)")
plt.xlabel("Year")
plt.ylabel("Performance Metric")
plt.legend()
# plt.show()

# Data
individuals = ["Person A", "Person B", "Person C", "Person D"]
variable_1 = [30, 29, 13, 18]
variable_2 = [9, 2, 20, 12]

# Scatter Plot
plt.figure(figsize = (12, 6))
plt.scatter(variable_1, variable_2)

for i, individual in enumerate(individuals):
    plt.annotate(individual, (variable_1[i], variable_2[i]))

# Titles and Labels
plt.title("Variable 1 vs Variable 2 Comparison")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
# plt.show()

# Data
organizations = ["Organization A", "Organization B", "Organization C"]
performance_metrics = [85, 102, 73]

# Bar Plot
plt.figure(figsize = (12, 6))
plt.bar(organizations, performance_metrics)

# Titles and Labels
plt.title("Performance Metrics by Organization")
plt.xlabel("Organization")
plt.ylabel("Performance Metric")
# plt.show()

# Data
years = list(range(2004, 2021))
sales = [1, 6, 14, 16, 38, 47, 53, 73, 60, 41, 58, 52, 37, 45, 51, 31, 38]

# Line Plot
plt.figure(figsize = (12, 6))
plt.plot(years, sales, color = 'blue', marker = 'o', linestyle = '--')

# Titles and Labels
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Product Sales per Year')
# plt.show()

data_set_A = [1, 6, 14, 16, 38, 47, 53, 73, 60, 41, 58, 52, 37, 45, 51, 31, 38]
data_set_B = [7, 12, 23, 42, 26, 33, 53, 60, 55, 51, 61, 51, 42, 44, 28, 37, 36]

# Scatter Plot
plt.figure(figsize = (12, 6))
plt.scatter(years, data_set_A, color = 'blue', marker = 'o', label = 'Data Set A')
plt.scatter(years, data_set_B, color = 'red', marker = 's', label = 'Data Set B')

# Titles, Labels and Legends
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Yearly Values: Data Set A vs Data Set B')
plt.legend()
# plt.show()

# Data
products = ['Product A', 'Product B', 'Product C']
sales = [23, 22, 18]

# Bar Plot
plt.figure(figsize = (12, 6))
plt.bar(products, sales, color = ['blue', 'red', 'green'])

# Titles and Labels
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Top Selling Products in 2021')
# plt.show()

# Data
years = list(range(2004, 2021))
growth = [1, 6, 14, 16, 38, 47, 53, 73, 60, 41, 58, 52, 54, 45, 51, 31, 38]

# Plot
plt.figure(figsize = (12, 6))
plt.plot(years, growth)

# Titles and Labels
plt.xlabel('Year')
plt.ylabel('Growth %')
plt.title('Company Annual Growth')

# Customize ticks and limits
plt.xticks(years, rotation = 45)
plt.yticks(range(0, 81, 10))
plt.xlim(2004, 2021)
plt.ylim(0, 80)
# plt.show()

# Data
years = ['2004', '2005', '2006', '2007', '2008']
sales = [5, 15, -5, 20, 15]
ad_costs = [1, 5, -1, 10, 9]

# Plot
plt.figure(figsize = (12, 6))
plt.scatter(sales, ad_costs)

# Titles and Labels
plt.xlabel('Sales')
plt.ylabel('Advertising Costs')
plt.title('Sales vs Advertising Costs')

# Customize ticks, labels, and limits
for i, year in enumerate(years):
    plt.annotate(year, (sales[i], ad_costs[i]), fontsize = 10, ha = 'right')

plt.xticks(range(-10, 26, 5))
plt.yticks(range(-5, 16, 2))
plt.xlim(-10, 25)
plt.ylim(-5, 15)
# plt.show()

# Data
products = ['Product A', 'Product B', 'Product C']
sales = [41, 30, 29]

# Plot
plt.figure(figsize = (12, 6))
plt.bar(products, sales)

# Titles and Labels
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Annual Sales for Products')

# Customize ticks and limits
plt.xticks(range(len(products)), products, rotation = 45)
plt.yticks(range(0, 51, 5))
plt.ylim(0, 50)
# plt.show()

# Practical Example 2
# Problem 1: Titles, Labels & Legends
players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
goals = [12, 15, 16, 13, 14]

plt.figure(figsize = (10, 6))
plt.plot(players, goals, marker = 'o', label = 'Goals')
plt.title('Goals Scored by Players in the Champions League')
plt.xlabel('Players')
plt.ylabel('Goals Scored')
plt.legend()
# plt.show()

# Problem 2: Colors, Markers & Line Styles
games = [10, 10, 10, 10, 10]
colors = ['darkblue', 'darkgreen', 'darkred', 'purple', 'darkorange']
markers = ['o', 'v', '^', '<', '>']

plt.figure(figsize = (10, 6))
for i in range(len(players)):
    plt.scatter(games[i], goals[i], color = colors[i], marker = markers[i])
plt.title('Goals Scored vs Games Played')
plt.xlabel('Games Played')
plt.ylabel('Goals Scored')
# plt.show()

assists = [5, 6, 4, 7, 5]
plt.figure(figsize = (10, 6))
plt.bar(players, assists, color = 'skyblue')
plt.title('Assists by Players in Champions League')
plt.xlabel('Players')
plt.ylabel('Assists')
plt.yticks(range(0, 10, 1))  # setting the ticks from 0 to 10 with a step of 1
plt.ylim(0, 10)  # setting the limits from 0 to 10
# plt.show()