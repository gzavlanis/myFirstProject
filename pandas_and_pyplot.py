# Import the required libraries: pandas for data manipulation and matplotlib for plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary containing the data for years and goals scored
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Goals': [25, 30, 28, 35, 32]}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Set the figure size for the plot
plt.figure(figsize = (12, 6))

# Plot the goals scored over the years using a line plot
plt.plot(df['Year'], df['Goals'])

# Set the x-axis label as 'Year'
plt.xlabel('Year')

# Set the y-axis label as 'Goals'
plt.ylabel('Goals')

# Set the title of the plot as 'Goals Scored by a Soccer Player Over Time'
plt.title('Goals Scored by a Soccer Player Over Time')

# Display the plot
# plt.show()

# Create a dictionary containing the data for the players and their goals
data = {'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Kylian Mbappe'],
        'Goals': [36, 31, 23, 33]}

# Convert the dictionary to a pandas DataFrame and store it in the variable 'df'
df = pd.DataFrame(data)

# Create a new figure with a specified size (width, height) in inches
plt.figure(figsize = (12, 6))

# Create a bar chart using the 'Player' column as the x-axis and the 'Goals' column as the y-axis
plt.bar(df['Player'], df['Goals'])

# Set the label for the x-axis
plt.xlabel('Player')

# Set the label for the y-axis
plt.ylabel('Goals')

# Set the title for the chart
plt.title('Goals Scored by Soccer Players in a Season')
# plt.show()

# Create a dictionary with keys 'Age' and 'Goals' and their corresponding values as lists
data = {
    'Age': [22, 24, 26, 28, 30, 32, 34],
    'Goals': [15, 20, 25, 30, 28, 22, 18]
}
# Convert the dictionary 'data' into a pandas DataFrame and store it in the variable 'df'
df = pd.DataFrame(data)

# Create a new figure with a specified size (width, height) in inches
plt.figure(figsize = (12, 6))
# Create a scatter plot using the 'Age' and 'Goals' columns from the DataFrame 'df'
plt.scatter(df['Age'], df['Goals'])
# Set the x-axis label to 'Age'
plt.xlabel('Age')
# Set the y-axis label to 'Goals'
plt.ylabel('Goals')
# Set the title of the plot to 'Relationship Between Age and Goals Scored in a Season'
plt.title('Relationship Between Age and Goals Scored in a Season')
# plt.show()

# Create a dictionary containing the data for Age, Goals, and Assists
data = {'Age': [22, 24, 26, 28, 30, 32, 34],
        'Goals': [15, 20, 25, 30, 28, 22, 18],
        'Assists': [5, 8, 10, 12, 11, 9, 7]}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create a figure with a specified size (width, height) in inches
fig = plt.figure(figsize = (24, 12))

# Add a 3D subplot to the figure
ax = fig.add_subplot(111, projection = '3d')

# Create a 3D scatter plot using Age, Goals, and Assists columns from the DataFrame
# Color the points based on Age, use viridis colormap, set point size, edge color, line width, and transparency
ax.scatter(df['Age'], df['Goals'], df['Assists'], c = df['Age'], cmap = 'viridis', s = 100, edgecolors = 'k', linewidths = 1, alpha = 0.75)

# Set the x-axis label with specified font size and padding
ax.set_xlabel('Age', fontsize = 14, labelpad = 10)

# Set the y-axis label with specified font size and padding
ax.set_ylabel('Goals', fontsize = 14, labelpad = 10)

# Set the z-axis label with specified font size and padding
ax.set_zlabel('Assists', fontsize = 14, labelpad = 10)

# Set the title of the plot with specified font size and padding
plt.title('Relationship Between Age, Goals, and Assists in a Season', fontsize = 20, pad = 20)
# plt.show()

# Define a dictionary containing the data for the players, their goals, and their positions
data = {
    "Goals": [22, 18, 12, 6, 4, 2],
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Luka Modric",
        "N'Golo Kante",
        "Sergio Ramos",
        "Virgil van Dijk",
    ],
    "Position": [
        "Forward",
        "Forward",
        "Midfielder",
        "Midfielder",
        "Defender",
        "Defender",
    ],
}

# Create a pandas DataFrame from the data dictionary, which will allow for easy manipulation and analysis of the data
df = pd.DataFrame(data)

# Create a new matplotlib figure with a specified size (width, height) in inches
fig = plt.figure(figsize = (24, 12))

# Add a 3D subplot to the figure, which will be used to create a 3D bar chart
ax = fig.add_subplot(111, projection = "3d")

# Get the unique positions from the DataFrame's "Position" column
positions = df["Position"].unique()

# Define a list of colors to be used for the bars in the 3D bar chart
colors = ["darkorange", "lightgreen", "cyan"]

# Loop through the unique positions and their corresponding index
for i, position in enumerate(positions):
    # Filter the DataFrame to only include rows with the current position
    position_data = df[df["Position"] == position]

    # Create an array of integers from 0 to the length of the position_data DataFrame, which will be used as the x-coordinates for the bars
    x = np.arange(len(position_data))

    # Get the "Goals" column from the position_data DataFrame, which will be used as the y-coordinates for the bars
    y = position_data["Goals"]

    # Create an array of zeros with the same length as the position_data DataFrame, which will be used as the z-coordinates for the bars
    z = np.zeros(len(position_data))

    # Create an array of ones with the same length as the position_data DataFrame, which will be used as the width of the bars
    dx = np.ones(len(position_data))

    # Create an array of ones with the same length as the position_data DataFrame, which will be used as the depth of the bars
    dy = np.ones(len(position_data))

    # Get the "Goals" column from the position_data DataFrame, which will be used as the height of the bars
    dz = position_data["Goals"]

    # Create a 3D bar chart using the x, y, z, dx, dy, and dz arrays, and set the color and shading for the bars
    ax.bar3d(x, y, z, dx, dy, dz, color = colors[i], shade = True)

# Set the label for the x-axis
ax.set_xlabel("Player Index")

# Set the label for the y-axis
ax.set_ylabel("Goals")

# Set the label for the z-axis
ax.set_zlabel("Position")
# plt.show()

# Practical Example #5
data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappe', 'Robert Lewandowski'],
    'Games Played': [38, 40, 35, 39, 34],
    'Goals': [36, 34, 21, 33, 41],
    'Assists': [12, 7, 10, 7, 5],
    'Successful Dribbles': [174, 89, 142, 90, 41],
    'Yellow Cards': [3, 5, 6, 2, 1]
}
df = pd.DataFrame(data)

plt.figure(figsize = (10, 6))
plt.bar(df['Player'], df['Goals'], color = 'blue')
plt.xlabel('Player')
plt.ylabel('Goals')
plt.title('Number of Goals Scored by Each Player')
plt.grid(True)

plt.figure(figsize = (10, 6))
plt.hist(df['Yellow Cards'], bins = 5, color = 'red', edgecolor = 'black')
plt.xlabel('Yellow Cards')
plt.ylabel('Frequency')
plt.title('Distribution of Yellow Cards')
plt.grid(True)

plt.figure(figsize = (10, 6))
for player in df['Player']:
    plt.scatter(df[df['Player'] == player]['Games Played'], df[df['Player'] == player]['Successful Dribbles'], label = player)

plt.xlabel('Games Played')
plt.ylabel('Successful Dribbles')
plt.title('Relationship between Games Played and Successful Dribbles')
plt.legend()
plt.grid(True)
plt.show()