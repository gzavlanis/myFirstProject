import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dictionary containing soccer data
# Create a dictionary containing data
data = {
    "Category": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
    "Values": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
}
df = pd.DataFrame(data)

# Create a boxplot using seaborn to visualize the distribution of scores by category
plt.figure(figsize = (12, 6)) # set the figure size
sns.boxplot(x = 'Category', y = 'Values', data = df, palette = 'Set2') # create the boxplot
plt.title('Boxplot of values by category') # add a title to the plot
# plt.show()

# set seed for reproducibility
np.random.seed(0)

# Let's generate some synthetic data
categories = ['Category A', 'Category B', 'Category C']

# Generate random values for each category
values = np.concatenate([np.random.normal(loc = mu, scale = 3, size = 25).astype(int) for mu in [20, 30, 40]])

# create the dataframe
data = {
    'Category': np.repeat(categories, 25),
    'Values': values
}
df = pd.DataFrame(data)

# Create a figure with custom size
plt.figure(figsize = (10, 6))

# Create a violin plot using seaborn library
sns.violinplot(x = 'Category', y = 'Values', data = df, palette = 'muted')

# Set title and display plot
plt.title('Value distribution of different categories')
# plt.show()

# load the example tips dataset
tips = sns.load_dataset('tips')

# create a swarm lot of total bill amounts, grouped by day of the week
plt.figure(figsize = (10, 6))
sns.swarmplot(x = "day", y = "total_bill", data = tips)
# plt.show()

# Set seed for reproducibility
np.random.seed(0)

# Generate some synthetic data
categories = ['Category A', 'Category B', 'Category C']
values = np.concatenate([np.random.normal(loc = mu, scale = 5, size = 50).astype(int) for mu in [20, 30, 40]])

# Create a dataframe
data = {
    'Category': np.repeat(categories, 50),
    'Values': values
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize = (10, 6))

# Create a violin plot which shows the distribution of the values
sns.violinplot(x = 'Category', y = 'Values', data = df, inner = None, color = ".8")

# Add a swarm plot which shows each individual data point
sns.swarmplot(x = 'Category', y = 'Values', data = df, color = 'black')

# Set the title and display plot
plt.title('Violin and Swarmplot of Values by Category')
# plt.show()

# Set seed for reproducibility
np.random.seed(0)

# Generate some synthetic data
positions = ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']
values = np.concatenate([np.random.normal(loc = mu, scale = 5, size = 50).astype(int) for mu in [80, 60, 50, 30]])

# Create a dataframe
data = {
    'Position': np.repeat(positions, 50),
    'Market Value (in M€)': values
}
df = pd.DataFrame(data)

# Create the combined violin and swarm plot
plt.figure(figsize = (10, 6))
sns.violinplot(x = 'Position', y = 'Market Value (in M€)', data = df, palette = 'muted', inner = None, width = 0.6)
sns.swarmplot(x = 'Position', y = 'Market Value (in M€)', data = df, color = 'black', size = 5)
plt.title('Market value distribution of players in different positions')
# plt.show()

# Let's generate some synthetic data
positions = ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']
leagues = ['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1']
values = np.concatenate([np.random.normal(loc = mu, scale = 10, size = 100).astype(int) for mu in [80, 60, 50, 30]])

# Create a dataframe
data = {
    'Position': np.repeat(positions, 100),
    'League': np.tile(np.repeat(leagues, 20), 4),
    'Market Value (in M€)': values
}
df = pd.DataFrame(data)

plt.figure(figsize = (12, 8))
sns.boxplot(x = 'Position', y = 'Market Value (in M€)', hue = 'League', data = df, palette = 'muted')
plt.title('Market value distribution of players in different positions and leagues')
# plt.show()

# Define categories
categories = ['Category A', 'Category B', 'Category C', 'Category D']
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Generate some synthetic data
values = np.concatenate([np.random.normal(loc = mu, scale = 5, size = 100).astype(int) for mu in [80, 60, 50, 30]])

# Create a dataframe
data = {
    'Category': np.repeat(categories, 100),
    'Group': np.tile(np.repeat(groups, 25), 4),
    'Value': values
}
df = pd.DataFrame(data)

# Create a FacetGrid to visualize the data
g = sns.FacetGrid(df, col = 'Group', row = 'Category', hue = 'Category', palette = 'muted', margin_titles = True)

# Map histogram plot to the FacetGrid for the 'Value' column
g = g.map(plt.hist, 'Value')
# plt.show()

# Generate synthetic data
items = ['Item' + str(i) for i in range(1, 101)]
values1 = np.random.randint(10, 50, size = 100)
values2 = np.random.poisson(lam = 10, size = 100)
values3 = np.random.poisson(lam = 5, size = 100)
values4 = np.random.normal(loc = 50, scale = 15, size = 100).astype(int)

# Create a dataframe
data = {
    'Item': items,
    'Value1': values1,
    'Value2': values2,
    'Value3': values3,
    'Value4': values4
}
df = pd.DataFrame(data)

# Create a
plt.figure(figsize = (12, 10))
g = sns.PairGrid(df.drop("Item", axis = 1))
g = g.map_diag(plt.hist, edgecolor = "w")
g = g.map_offdiag(plt.scatter, edgecolor = "w", s = 40)
# plt.show()

# Generate synthetic data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = np.concatenate([np.random.normal(loc = mu, scale = 5, size = 50).astype(int) for mu in [80, 60, 50, 30]])

# Create a dataframe
data = {
    'Category': np.repeat(categories, 50),
    'Value': values
}
df = pd.DataFrame(data)

# Create a Faceted Histogram
g = sns.FacetGrid(df, col = 'Category', col_wrap = 2, height = 4, aspect = 1.5)
g = g.map(plt.hist, 'Value', edgecolor = "w", bins = 15)
# plt.show()

# Generate some synthetic data
players = ['Player' + str(i) for i in range(1, 101)]  # Create a list of player names
ages = np.random.randint(18, 40, size = 100)  # Generate random ages between 18 and 40 for 100 players
goals = np.random.poisson(lam = 10, size = 100)  # Generate random goals scored using Poisson distribution for 100 players
assists = np.random.poisson(lam = 5, size = 100)  # Generate random assists using Poisson distribution for 100 players
values = np.random.normal(loc = 50, scale = 15, size = 100).astype(int)  # Generate random market values using normal distribution for 100 players

# Create a dataframe
data = {
    'Player': players,
    'Age': ages,
    'Goals Scored': goals,
    'Assists': assists,
    'Market Value (in M€)': values
}
df = pd.DataFrame(data)  # Create a pandas DataFrame from the generated data

# Create a scatterplot matrix
plt.figure(figsize = (12, 10))
sns.pairplot(df.drop('Player', axis = 1))  # Create a scatterplot matrix of the numerical columns in the DataFrame
# plt.show()  # Display the scatterplot matrix

# Generate a 50x6 matrix of random integers between 50 and 100
data = np.random.randint(50, 100, size = (50, 6))

# Define metrics for the data
metrics = ["Metric" + str(i) for i in range(1, 7)]

# Create a list of indices
indices = ["Index" + str(i) for i in range(1, 51)]

# Create a dataframe with the generated data
df = pd.DataFrame(data, columns = metrics, index = indices)

# Compute the correlation matrix between the metrics
corr = df.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize = (10, 8))  # Set the figure size
sns.heatmap(corr, annot = True, cmap = "coolwarm", center = 0)  # Plot the heatmap with annotations, color map, and center at 0
plt.title("Correlation heatmap of metrics")  # Set the title of the heatmap
# plt.show()  # Display the heatmap

# Create a DataFrame with synthetic data
data = {'Index': ['Index' + str(i) for i in range(1, 6)],
        'Metric1': np.random.randint(1, 100, size = 5),
        'Metric2': np.random.randint(1, 100, size = 5),
        'Metric3': np.random.randint(1, 100, size = 5),
        'Metric4': np.random.randint(1, 100, size = 5),
        'Metric5': np.random.randint(1, 100, size = 5)}

df = pd.DataFrame(data)

# Normalize the data
normalized_df = (df.iloc[:, 1:] - df.iloc[:, 1:].min()) / (df.iloc[:, 1:].max() - df.iloc[:, 1:].min())

# Add the indices back to the normalized DataFrame
normalized_df.insert(0, 'Index', df['Index'])

# Set the index to the indices
normalized_df.set_index('Index', inplace = True)

# Create a clustermap
sns.clustermap(normalized_df, cmap = 'coolwarm', annot = True, figsize = (10, 6))
# plt.show()

sns.set_theme()  # Setting the default seaborn theme for the plot

# Creating a dictionary containing the data for goals, assists, appearances, and minutes played
data = {
    "Goals": [15, 8, 12, 20, 5],
    "Assists": [10, 12, 8, 5, 15],
    "Appearances": [38, 35, 30, 32, 40],
    "Minutes_Played": [3420, 3150, 2700, 2880, 3600],
}

# Creating a list of player names
players = ["Player1", "Player2", "Player3", "Player4", "Player5"]

# Creating a pandas DataFrame using the data dictionary and setting the index to player names
df = pd.DataFrame(data, index = players)

# Normalizing the DataFrame by subtracting the minimum value and dividing by the range (max - min)
normalized_df = (df - df.min()) / (df.max() - df.min())

# Creating a matplotlib figure and axis with a specified size
fig, ax = plt.subplots(figsize = (10, 5))

# Creating a heatmap using seaborn with the normalized DataFrame, adding annotations, and setting the colormap
sns.heatmap(normalized_df, annot = True, cmap = "coolwarm", ax = ax)

# plt.show()

# Set the theme for seaborn plots
sns.set_theme(style = "white")

# Create a custom dataframe with player data
data = {
    "Player": [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar",
        "Kylian Mbappe",
        "Mohamed Salah",
    ],
    "Goals": [672, 674, 366, 131, 156],
    "Assists": [305, 229, 216, 77, 64],
    "Appearances": [778, 895, 520, 216, 295],
    "Minutes_Played": [66960, 75810, 44370, 18450, 25200],
}

df = pd.DataFrame(data)

# Normalize the data (min-max scaling) for better comparison
normalized_df = (df.iloc[:, 1:] - df.iloc[:, 1:].min()) / (df.iloc[:, 1:].max() - df.iloc[:, 1:].min())
normalized_df["Player"] = df["Player"]

# Create a clustermap with single linkage method
g = sns.clustermap(normalized_df.set_index("Player"), method = "single", cmap = "coolwarm", figsize = (10, 6))
plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0)
plt.show()

# Create a clustermap with complete linkage method
g = sns.clustermap(normalized_df.set_index("Player"), method = "complete", cmap = "coolwarm", figsize = (10, 6))
plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0)
plt.show()

# Create a clustermap with average linkage method
g = sns.clustermap(normalized_df.set_index("Player"), method = "average", cmap = "coolwarm", figsize = (10, 6))
plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0)
plt.show()

# Create a clustermap with ward linkage method
g = sns.clustermap(normalized_df.set_index("Player"), method = "ward", cmap = "coolwarm", figsize = (10, 6))
plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0)
plt.show()

# Define a dictionary containing data
data = {
    "Height": [170, 168, 177, 181, 176],
    "Weight": [72, 67, 78, 79, 73],
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

sns.set(style = "darkgrid")
plt.figure(figsize = (12, 6))

# Create a scatter plot with a regression line using seaborn
sns.regplot(x = "Height", y = "Weight", data = df, marker = "o", scatter_kws = {"s": 200, "alpha": 0.5})
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
# plt.show()

data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Sales": [50, 58, 66, 74, 85, 96],
    "Expenses": [30, 35, 40, 45, 50, 55],
}
df = pd.DataFrame(data)

sns.set(style = "darkgrid", palette = "Set2")
plt.figure(figsize = (10, 6))

sns.lineplot(data = df["Sales"], marker = "o", markersize = 10, linewidth = 2)
sns.lineplot(data = df["Expenses"], marker = "o", markersize = 10, linewidth = 2)

plt.title("Company Performance Over Time", fontsize = 16)
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Count (in 1000s)", fontsize = 12)
plt.legend(labels = ["Sales", "Expenses"])
# plt.show()

data = {
    'Name': ['John', 'Maria', 'Steve', 'Sophia', 'Mike', 'Emma', 'Jake', 'Clara'],
    'Score': [30, 28, 35, 31, 27, 33, 29, 30],
    'Age': [15, 16, 15, 16, 17, 16, 15, 17],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}
df = pd.DataFrame(data)

sns.lmplot(x = 'Score', y = 'Age', data = df, hue = 'Gender', scatter = True, legend = False)
plt.legend(title = 'Gender', loc = 'upper left', bbox_to_anchor = (1, 1))
plt.title('Score vs Age')
plt.xlabel('Score')
plt.ylabel('Age')
# plt.show()

data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product A Sales': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Product B Sales': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
    'Product C Sales': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
}
df = pd.DataFrame(data)

sns.set(style = "darkgrid")
plt.figure(figsize = (10, 6))
sns.lineplot(data = df.drop('Month', axis = 1), markers = True, linewidth = 2.5)
plt.title("Sales Trends Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(title = 'Product', loc = 'upper left')
plt.show()

