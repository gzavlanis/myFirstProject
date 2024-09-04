import numpy as np
import pandas as pd # Importing pandas library for data manipulation
import seaborn as sns # Importing seaborn library for data visualization
import matplotlib.pyplot as plt # Importing matplotlib library for creating plots

np.random.seed(42)
data = np.random.randint(low = 1, high = 10, size = (5, 5))
print(data)

hm = sns.heatmap(data = data, cmap = 'coolwarm', annot = True)
# plt.show()

# my turn:
data = np.random.randint(low = 10, high = 100, size = (7, 7))
print(data)

hm1 = sns.heatmap(data = data, cmap = 'viridis', annot = True)
# plt.show()

# sample soccer player data
data = {
    'Name': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Kylian Mbappé', 'Mohamed Salah'],
    'Age': [34, 36, 29, 22, 29],
    'Market Value (M€)': [80, 45, 100, 160, 110]
}
df = pd.DataFrame(data) # create a pandas dataframe from the data dictionary

# Plotting the age distribution:
sns.histplot(data = df, x = 'Age', bins = 5) # Creating a histogram plot of the 'Age' column with 5 bins
plt.title('Soccer Players Age Distribution') # Adding the title to the plot
# plt.show()

sns.scatterplot(data = df, x = 'Age', y = 'Market value (M€)', hue = 'Name', s = 100) # Creating a scatterplot with seaborn
plt.title('Soccer players Market value vs. Age') # Adding a title to the plot
# plt.show()

# Define a dictionary containing age data
age_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "Age": [28, 29, 30, 27, 29, 27, 23, 30, 30, 29],
}
df = pd.DataFrame(age_data)

# Create a histogram of the Age column using seaborn's displot function
sns.displot(df['Age'])

# Add a title x-axis label and y-axis label to the plot
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
# plt.show()

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Create a jointplot
sns.jointplot(x = 'Books_Read', y = 'Hours_TV_Watched', data = data)
# plt.show()

# Define a dictionary containing data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [34, 36, 29, 30, 29],
    'Books_Read': [30, 32, 25, 10, 28],
    'Hours_TV_Watched': [12, 5, 18, 20, 8],
    'Hours_Slept': [33, 31, 27, 35, 32]
})

# create a pairplot
sns.pairplot(data[['Age', 'Books_Read', 'Hours_TV_Watched', 'Hours_Slept']])
# plt.show()

# Create a dictionary containing soccer data
data = {
    "team": ["Barcelona", "Real Madrid", "Atletico Madrid", "Sevilla", "Villarreal"],
    "goals": [86, 67, 58, 54, 60],
}
soccer_data = pd.DataFrame(data)

# set the plot style to darkgrid
sns.set_style('darkgrid')
# set the color palette for the plot
sns.set_palette('husl')

# Create a scatter plot using seaborn with custom square markers and size 100
sns.scatterplot(x = 'team', y = 'goals', data = soccer_data, marker = 's', s = 100)

# add a title and labels to the plot
plt.title('Goals Scored by teams')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.show()