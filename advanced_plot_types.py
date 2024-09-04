import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data_points = [32, 36, 22, 28, 30, 24, 26, 34, 29, 31]
bins = 5
range = (20, 40)
color = 'blue'
alpha = 0.7

plt.figure(figsize = (12, 6))
plt.hist(data_points, bins, range, color = color, alpha = alpha)
plt.xlabel('Data Points')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data Points')
# plt.show()

plt.figure(figsize = (12, 6))
plt.boxplot(
    data_points, vert = True, patch_artist = True, boxprops = dict(facecolor = 'blue', color = 'blue'),
    medianprops = dict(color = 'red'), whiskerprops = dict(color = 'green', linestyle = '--'),
    capprops = dict(color = 'purple'), flierprops = dict(marker = 'o', markerfacecolor = 'yellow', markersize = 8)
)
plt.ylabel('Data Points')
plt.title('Box Plot of Random Data Points')
# plt.show()

bins = 10
plt.figure(figsize = (12, 6))
plt.hist(data_points, bins, range, color = color, alpha = alpha)
plt.xlabel("Data Points")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data Points (10 Bins)")
# plt.show()

plt.figure(figsize = (12, 6))
plt.boxplot(
    data_points, vert = False, patch_artist = True, boxprops = dict(facecolor = "blue", color = "blue"),
    medianprops = dict(color = "red"), whiskerprops = dict(color = "green", linestyle = "--"), capprops = dict(color = "purple"),
    flierprops = dict(marker = "o", markerfacecolor = "yellow", markersize = 8))
plt.xlabel("Data Points")
plt.title("Horizontal Box Plot of Random Data Points")
# plt.show()

# Sample data (measurements at different points)
data = np.array(
    [
        [3, 2, 1, 0, 0],
        [2, 3, 2, 1, 0],
        [1, 2, 3, 2, 1],
        [0, 1, 2, 3, 2],
        [0, 0, 1, 2, 3],
    ]
)

plt.figure(figsize = (12, 6))
plt.imshow(data, cmap = 'coolwarm', interpolation = 'nearest')
plt.colorbar()

# Custom labels
x_labels = ['A', 'B', 'C', 'D', 'E']
y_labels = ['1', '2', '3', '4', '5']
plt.xticks(np.arange(len(x_labels)), x_labels)
plt.yticks(np.arange(len(y_labels)), y_labels)
# plt.show()

# Sample data (measurements)
x = np.linspace(0, 5, 6)
y = np.linspace(0, 5, 6)
X, Y = np.meshgrid(x, y)
Z = np.array([
    [3, 2, 1, 0, 0, 0],
    [2, 3, 2, 1, 0, 0],
    [1, 2, 3, 2, 1, 0],
    [0, 1, 2, 3, 2, 1],
    [0, 0, 1, 2, 3, 2],
    [0, 0, 0, 1, 2, 3]
])

plt.figure(figsize = (12, 6))
contour_plot = plt.contour(X, Y, Z, cmap = 'coolwarm', levels = 10)
plt.clabel(contour_plot, inline = True, fontsize = 8)
plt.colorbar()

# custom labels
x_labels = ['A', 'B', 'C', 'D', 'E', 'F']
y_labels = ['1', '2', '3', '4', '5', '6']
plt.xticks(np.arange(len(x_labels)), x_labels, rotation = 45)
plt.yticks(np.arange(len(y_labels)), y_labels)
# plt.show()

# Sample data (measurements)
x = np.linspace(0, 5, 6)
y = np.linspace(0, 5, 6)
X, Y = np.meshgrid(x, y)
Z = np.array([
    [3, 2, 1, 0, 0, 0],
    [2, 3, 2, 1, 0, 0],
    [1, 2, 3, 2, 1, 0],
    [0, 1, 2, 3, 2, 1],
    [0, 0, 1, 2, 3, 2],
    [0, 0, 0, 1, 2, 3]
])

plt.figure(figsize=(12, 6))
plt.contour(X, Y, Z)
plt.colorbar()
# plt.show()

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values_1 = [120, 150, 70, 220, 100]
values_2 = [80, 230, 100, 70, 180]
values_3 = [200, 100, 150, 100, 225]

fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot(111, projection = '3d')

colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))
markers = ['o', 's', '^', 'D', 'P']

for i, category in enumerate(categories):
    ax.scatter(values_1[i], values_2[i], values_3[i], color = colors[i], marker = markers[i], s = 100, edgecolors = 'k', linewidths = 1.5)
    ax.text(values_1[i], values_2[i], values_3[i], category, fontsize = 10, color = colors[i])

ax.set_xlabel('Value 1', fontsize = 14)
ax.set_ylabel('Value 2', fontsize = 14)
ax.set_zlabel('Value 3', fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 12)

plt.title("3D Scatter Plot Example", fontsize = 20)
# plt.show()

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values_1 = [68, 74, 86, 91, 86]
values_2 = [30, 29, 21, 76, 74]
values_3 = [78, 95, 51, 26, 39]

fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot(111, projection = '3d')

xpos = np.arange(len(categories))
ypos = np.zeros(len(categories))
zpos = np.zeros(len(categories))

dx = np.ones(len(categories))
dy = np.ones(len(categories))
dz = np.array(values_1)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color = 'purple')
ax.set_xticks(xpos)
ax.set_xticklabels(categories)
ax.set_ylabel('Value 2')
ax.set_zlabel('Value 1')
# plt.show()

# Sample data
x = np.linspace(0, 100, 100)
y = np.linspace(0, 50, 50)
x, y = np.meshgrid(x, y)
z = np.sin(0.1 * x) * np.cos(0.1 * y)

fig = plt.figure(figsize = (24, 12))
ax = fig.add_subplot(111, projection = "3d")

# cmap sets the colormap, while edge color sets the color of the edges between the surface polygons
ax.plot_surface(x, y, z, cmap = "viridis", edgecolor = "none")
ax.set_xlabel("Field Length (m)")
ax.set_ylabel("Field Width (m)")
ax.set_zlabel("Elevation (m)")
ax.view_init(elev = 25, azim = -60)
# plt.show()

# Sample data
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure(figsize = (12, 6))
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# plt.show()

# Sample data
x = np.linspace(0, 100, 100)
y = np.linspace(0, 50, 50)
x, y = np.meshgrid(x, y)
z = np.sin(0.1 * x) * np.cos(0.1 * y)

fig = plt.figure(figsize = (12, 6))
ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(x, y, z, cmap = "viridis", edgecolor = "none", alpha = 0.8)
ax.set_xlabel("Field Length (m)")
ax.set_ylabel("Field Width (m)")
ax.set_zlabel("Elevation (m)")
ax.view_init(elev = 25, azim = -60)
plt.tight_layout()
# plt.show()

# Practical example 3
goals = [45, 52, 48, 42, 50]

plt.figure(figsize = (10,6))
plt.hist(goals, bins = 5, color = 'green', edgecolor = 'black')
plt.title('Distribution of Goals Scored')
plt.xlabel('Goals Scored')
plt.ylabel('Frequency')
# plt.show()

assists = [20, 15, 18, 23, 22]

plt.figure(figsize = (10, 6))
plt.boxplot(assists, vert = False)
plt.title('Distribution of Assists')
plt.xlabel('Assists')
# plt.show()

minutes_played = [2800, 2900, 2750, 2700, 2850]
data = np.array([goals, assists, minutes_played])

corr_matrix = np.corrcoef(data)

plt.figure(figsize = (10, 6))
plt.imshow(corr_matrix, cmap = 'hot')
plt.title('Correlation Heatmap')
plt.colorbar(label = 'Correlation Coefficient')
plt.xticks(range(data.shape[0]), ['Goals', 'Assists', 'Minutes Played'])
plt.yticks(range(data.shape[0]), ['Goals', 'Assists', 'Minutes Played'])
# plt.show()

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(goals, assists, minutes_played, c = 'red', marker = 'o')
ax.set_title('3D Scatter Plot of Goals, Assists and Minutes Played')
ax.set_xlabel('Goals')
ax.set_ylabel('Assists')
ax.set_zlabel('Minutes Played')
# plt.show()

players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
player_indices = np.arange(len(players))  # the x locations for the players

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

for i, player in enumerate(player_indices):
    ax.bar3d(i, goals[i], 0, 0.4, 0.8, assists[i], color = 'b')

ax.set_title('3D Bar Plot of Player Performance')
ax.set_xticks(player_indices)
ax.set_xticklabels(players, rotation = 45, horizontalalignment = 'right')
ax.set_xlabel('Players')
ax.set_ylabel('Goals')
ax.set_zlabel('Assists')
# plt.show()

months = np.arange(1, 13)
product_1_sales = np.random.randint(50, 100, 12)
product_2_sales = np.random.randint(50, 100, 12)

plt.figure(figsize = (12, 6))
plt.plot(months, product_1_sales, label = 'Product 1', color = 'blue', linestyle = '-', linewidth = 2)
plt.plot(months, product_2_sales, label = 'Product 2', color = 'red', linestyle = '--', linewidth = 2)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Product Sales Over Time')
plt.legend()
plt.grid(True)
# plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_temp = np.random.randint(20, 35, 12)

x = np.arange(len(months))
width = 0.4

plt.figure(figsize = (12, 6))
plt.bar(x, avg_temp, width, color = 'green', edgecolor = 'black', linewidth = 1)
plt.xticks(x, months)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Monthly Temperatures')
# plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_temp = np.random.randint(20, 35, 12)

x = np.arange(len(months))
width = 0.4

plt.figure(figsize = (12, 6))
plt.bar(x, avg_temp, width, color = 'green', edgecolor = 'black', linewidth = 1)
plt.xticks(x, months)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Monthly Temperatures')
# plt.show()

x = np.random.randn(100)
y = np.random.randn(100)

plt.figure(figsize = (12, 6))
plt.scatter(x, y, s = 100, c = 'orange', edgecolor = 'black', linewidth = 1, alpha = 0.75)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Data Scatter Plot')
plt.grid(True)
# plt.show()

fig = plt.figure(figsize = (12, 6))
ax = fig.add_subplot(111, projection = '3d')

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

ax.scatter(x, y, z, s = 20, c = 'blue', edgecolor = 'black', linewidth = 0.5, alpha = 0.75)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')
# plt.show()

fig = plt.figure(figsize = (12, 6))
ax = fig.add_subplot(111, projection = '3d')

# Defining X, Y, Z for creating a surface
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x ** 2 + y ** 2))

# Creating a surface plot
surf = ax.plot_surface(x, y, z, cmap = 'viridis', linewidth = 0, antialiased = False, edgecolor = 'none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')
fig.colorbar(surf, shrink = 0.5, aspect = 5) # Add a color bar
# plt.show()

years = list(range(2010, 2020))
sales = [1200, 1500, 1700, 1600, 1750, 1800, 2000, 2100, 2200, 2300]

plt.figure(figsize= (12, 6))
plt.plot(years, sales, marker = 'o')
plt.xlabel('Year')
plt.ylabel('Sales (in thousands)')
plt.title('Company Sales over the Years')
plt.grid(True)
# plt.show()

regions = ['North', 'South', 'East', 'West', 'Central']
sales = [500, 650, 800, 450, 700]

plt.figure(figsize = (12, 6))
plt.bar(regions, sales, color = 'teal')
plt.xlabel('Region')
plt.ylabel('Sales (in thousands)')
plt.title('Product Sales by Region')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
# plt.show()

price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
quantity = [1500, 1200, 900, 850, 800, 750, 700, 650, 600, 550]

plt.figure(figsize = (12, 6))
plt.scatter(price, quantity, color = 'purple')
plt.xlabel('Price')
plt.ylabel('Quantity Sold')
plt.title('Price vs Quantity Sold')
plt.grid(True, linestyle = '-', color = '0.75')
# plt.show()

price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
quantity_sold = [1500, 1200, 900, 850, 800, 750, 700, 650, 600, 550]
profit = [500, 800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800]

fig = plt.figure(figsize = (12, 7))
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(price, quantity_sold, profit, color = 'red')
ax.set_xlabel('Price')
ax.set_ylabel('Quantity Sold')
ax.set_zlabel('Profit')
ax.set_title('3D Scatter Plot of Price, Quantity Sold and Profit')
# plt.show()

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure(figsize = (12, 7))
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y, z, cmap = 'viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')
# plt.show()

# Data points
data = {
    "Point A": (30, 9),
    "Point B": (29, 3),
    "Point C": (41, 7),
}

# Create scatter plot
plt.figure(figsize = (12, 6))
for point, (x, y) in data.items():
    plt.scatter(x, y,label = point)
    plt.annotate(point, (x, y), textcoords = 'offset points', xytext = (0, 5), ha = 'center')
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Scatter Plot with Annotations')
plt.legend()
# plt.show()

# Data points
data = {'A': 86, 'B': 74, 'C': 69}

# create bar plot
labels = list(data.keys())
values = list(data.values())
x = np.arange(len(labels))

plt.figure(figsize = (12, 6))
plt.bar(x, values)
plt.xticks(x, labels)

# Add text annotation
for i, v in enumerate(values):
    plt.annotate(str(v), (i, v), textcoords = "offset points", xytext = (0, 5), ha = 'center')
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar plot with Annotations')
# plt.show()

# Data points
years = np.arange(2010, 2021)
values = [53, 73, 60, 41, 58, 41, 37, 45, 51, 31, 30]

plt.figure(figsize = (12, 6))
plt.plot(years, values, marker = 'o', label = 'Values')
plt.arrow(2014, 58, 0, -17, length_includes_head = True, head_width = 0.5, head_length = 2, color = 'red')
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Line Plot with Arrow')
plt.legend()
# plt.show()

# Data points
data = {'A': (30, 9, 35), 'B': (29, 3, 33), 'C': (41, 7, 29)}

fig = plt.figure(figsize = (12, 6))
ax = fig.add_subplot(111, projection = '3d')

# create 3D scatter plot
for point, (x, y, z) in data.items():
    ax.scatter(x, y, z, label = point)
    ax.text(x, y, z, point)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot with Annotations')
ax.legend()
# plt.show()

# Coordinates
x = np.linspace(0, 105, 100)
y = np.linspace(0, 68,100)
x, y = np.meshgrid(x, y)

# Function to plot
z = np.sin(np.sqrt(x ** 2 + y ** 2))

# Create 3D surface plot
fig = plt.figure(figsize = (12, 6))
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(x, y, z, cmap = 'viridis')

# Annotate specific point
ax.text(52, 34, 0, 'Point of Interest', color = 'red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot with Annotation')
fig.colorbar(surf, shrink = 0.5, aspect = 5)
# plt.show()

# Example data
categories = ["Category 1", "Category 2", "Category 3"]
values = [100, 200, 150]

# Create a 1x2 subplot grid
fig, ax = plt.subplots(1, 2, figsize = (12, 6))

# First subplot: bar plot
ax[0].bar(categories, values)
ax[0].set_title("Bar Plot")

# Second subplot: pie chart
ax[1].pie(values, labels = categories, autopct = '%1.1f%%')
ax[1].set_title("Pie Chart")
# plt.show()

# Example data
categories = ["Category 1", "Category 2", "Category 3"]
values1 = [100, 200, 150]
values2 = [80, 220, 130]

# Create a 1x2 subplot grid with shared Y-axis
fig, ax = plt.subplots(1, 2, sharey = True, figsize = (12, 6))

# First subplot: bar plot for values1
ax[0].bar(categories, values1)
ax[0].set_title("Values 1")

# Second subplot: bar plot for values2
ax[1].bar(categories, values2)
ax[1].set_title("Values 2")
# plt.show()

# Create a 1x2 subplot grid with shared Y-axis
fig, ax = plt.subplots(1, 2, sharey = True, figsize = (12, 6))

# First subplot: bar plot for values1
ax[0].bar(categories, values1)
ax[0].set_title("Values 1")

# Second subplot: bar plot for values2
ax[1].bar(categories, values2)
ax[1].set_title("Values 2")

# Adjust the spacing between subplots
plt.subplots_adjust(wspace = 0.4)
# plt.show()

# Example data
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

# Create a 1x2 subplot grid for 3D plots
fig = plt.figure(figsize = (12, 6))

# First subplot: 3D scatter plot
ax1 = fig.add_subplot(1, 2, 1, projection = '3d')
ax1.scatter(x, y, z)
ax1.set_title("3D Scatter Plot")

# Second subplot: 3D bar plot
ax2 = fig.add_subplot(1, 2, 2, projection = '3d')
_x = np.arange(3)
_y = np.arange(3)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax2.bar3d(x, y, bottom, width, depth, top, shade = True)
ax2.set_title("3D Bar Plot")

# Adjust the spacing between subplots
plt.subplots_adjust(wspace = 0.4)
# plt.show()

# Define the sample data for players, goals, assists, and appearances
players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr"]
goals = [672, 674, 366]
assists = [305, 229, 216]
appearances = [778, 895, 513]

# Create a figure with a specific size to hold the subplots
fig = plt.figure(figsize=(24, 12))

# Add a 3D scatter plot as the first subplot (1 row, 2 columns, 1st plot)
ax1 = fig.add_subplot(121, projection="3d")
# Plot the scatter points using goals, assists, and appearances data
ax1.scatter(goals, assists, appearances)
# Add player names as labels to the scatter points
for i, player in enumerate(players):
    ax1.text(goals[i], assists[i], appearances[i], player)
# Set the labels for the x, y, and z axes of the scatter plot
ax1.set_xlabel("Goals")
ax1.set_ylabel("Assists")
ax1.set_zlabel("Appearances")
# Set the title for the scatter plot
ax1.set_title("Goals, Assists, and Appearances (Scatter Plot)")

# Add a 3D bar plot as the second subplot (1 row, 2 columns, 2nd plot)
ax2 = fig.add_subplot(122, projection="3d")

# Prepare the data for the bar plot
x = np.arange(len(players))
y = np.array(goals)
z = np.array(assists)
dz = np.array(appearances)

# Create the 3D bar plot using the prepared data
ax2.bar3d(x, y, z, 0.5, 0.5, dz)
# Add player names as labels to the bars
for i, player in enumerate(players):
    ax2.text(x[i], y[i], z[i] + dz[i], player)
# Set the labels for the x, y, and z axes of the bar plot
ax2.set_xlabel("Players")
ax2.set_ylabel("Goals")
ax2.set_zlabel("Assists")
# Set the title for the bar plot
ax2.set_title("Goals, Assists, and Appearances (Bar Plot)")
# plt.show()

players = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappe', 'Robert Lewandowski']
goals = [36, 34, 21, 33, 41]
assists = [12, 7, 10, 7, 5]
dribbles = [174, 89, 142, 90, 41]

# Creating a subplot with 3 rows and 1 column
fig, ax = plt.subplots(3, 1, figsize = (10, 12), sharex = True)

# Adding a grid for better readability
for axis in ax:
    axis.grid(True)

# Creating a bar plot for goals
ax[0].bar(players, goals, color = 'blue')
ax[0].set_ylabel('Goals')
# Annotating the player with the maximum goals
max_goals_player = players[np.argmax(goals)]
ax[0].annotate('Max: ' + max_goals_player, xy = (players.index(max_goals_player), max(goals)),
    xytext = (players.index(max_goals_player), max(goals) + 1), arrowprops = dict(facecolor = 'red'))

# Creating a bar plot for assists
ax[1].bar(players, assists, color = 'green')
ax[1].set_ylabel('Assists')
# Annotating the player with the maximum assists
max_assists_player = players[np.argmax(assists)]
ax[1].annotate('Max: ' + max_assists_player, xy = (players.index(max_assists_player), max(assists)),
    xytext = (players.index(max_assists_player), max(assists) + 1), arrowprops = dict(facecolor = 'red'))

# Creating a bar plot for successful dribbles
ax[2].bar(players, dribbles, color = 'purple')
ax[2].set_xlabel('Players')
ax[2].set_ylabel('Successful Dribbles')
# Annotating the player with the maximum successful dribbles
max_dribbles_player = players[np.argmax(dribbles)]
ax[2].annotate('Max: ' + max_dribbles_player, xy = (players.index(max_dribbles_player), max(dribbles)),
    xytext = (players.index(max_dribbles_player), max(dribbles) + 1), arrowprops = dict(facecolor = 'red'))

plt.tight_layout()
plt.show()