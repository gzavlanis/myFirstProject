import pandas as pd
import numpy as np

# define the date range
date_range = pd.date_range(start = '2020-01-01', end = '2020-12-31', freq = 'D')

# generate random data
data = np.random.rand(len(date_range))

# create dataframe
df = pd.DataFrame(data = data, index = date_range, columns = ['Sales'])
print(df.head(), '\n')

# Accessing year, month, and day
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['tasks_completed'] = np.random.randint(low = 1, high = 20, size = (len(date_range),))

# filtering data by rate
data_2020 = df[df['year'] == 2020]
print(data_2020, '\n')

# selecting data between two dates
data_jan_feb = df['2020-01-01':'2020-02-29']
print(data_jan_feb, '\n')

# resampling data to monthly frequency
monthly_data = df.resample('M').mean()
print(monthly_data,'\n')

# resampling data to weekly frequency and calculating the sum
weekly_data = df.resample('W').sum()

# calculate the 7-day rolling mean of tasks completed
df['tasks_rolling_mean'] = df['tasks_completed'].rolling(window = 7).mean()
print(df, '\n')

# Calculate the 30-day rolling sum of tasks completed
df['tasks_rolling_sum'] = df['tasks_completed'].rolling(window=30).sum()

# We have 100 employees
employee_ids = np.arange(1, 101)

# The departments are randomly assigned
departments = np.random.choice(['HR', 'Sales', 'Finance', 'Marketing'], 100)

# Generate random ages between 25 and 60 for our employees
ages = np.random.randint(25, 61, 100)

# Generate random salaries between 30000 and 120000 for our employees
salaries = np.random.randint(30000, 120001, 100)

# Create DataFrame
data = pd.DataFrame({'EmployeeID': employee_ids, 'Department': departments, 'Age': ages, 'Salary': salaries})

# convert the 'Department' column to a categorical data type
data['Department'] = data['Department'].astype('category')

# display the first 5 rows of the DataFrame
print(data.head(),'\n')
print(data.info(), '\n')

sorted_data = data.sort_values(by = 'Department')
print(sorted_data, '\n')

grouped_data = data.groupby('Department')
print(grouped_data, '\n')

filtered_data = data[data['Department'] == 'Finance']
print(filtered_data, '\n')

data = {
    "Employee": ["John Doe", "Jane Smith", "Bob Johnson"],
    "Hours Worked": [40, 37, 42],
    "Overtime": [5, 8, 2],
}
df = pd.DataFrame(data)

df['TotalHours'] = df.eval('`Hours Worked` + Overtime')
print(df, '\n')

filtered_df = df.query('TotalHours > 40')
print(filtered_df, '\n')

# case study 4: Exploring Market Trends
# Define data
data = {
    'Item': ['Item1']*5 + ['Item2']*5 + ['Item3']*5,
    'Date': pd.date_range(start='2020-01-01', periods=5).tolist()*3,
    'Market_Value_Millions': [125, 100, 100, 90, 80, 105, 100, 90, 85, 75, 160, 160, 150, 140, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# convert 'Date' to datetime
df['Date'] = pd.to_datetime((df['Date']))

# Set date as index
df.set_index('Date', inplace = True)

# Display the DataFrame
print('\nDataFrame after setting Date as index:')
print(df, '\n')

# Resample the data
df_resampled = df.groupby('Item').resample('YE').mean(numeric_only = True)

# Print the resampled DataFrame
print('\nResampled Dataframe:')
print(df_resampled, '\n')

# Convert 'Item' to categorical data
df['Item'] = df['Item'].astype('category')

# Print the new DataFrame
print('\nDataFrame after converting Item to category:')
print(df, '\n')

# Exercises my solutions:
df = pd.read_csv("https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-o14h1x17-NapolivsAjax.csv")
print(df, '\n')

name = df.loc[df['ballRecovery'] == df['ballRecovery'].max()]["matchName"]
print(name.item(), '\n')

result = df.groupby('teamName')['successfulFinalThirdPasses'].mean()
print(result, '\n')

result = df.query("gameStarted == 0").groupby('teamName')['teamName'].count()
print(result, '\n')

result = df.groupby('teamName')['wonTackle'].sum()
print(result, '\n')

result = df.groupby(['teamName', 'position'])['ballRecovery'].mean()
print(result, '\n')

name2 = df[df['totalScoringAtt'] == df['totalScoringAtt'].max()]['matchName']
print(name2.tolist()[0], '\n') # return the first one

# Exercises recommended solutions:
# Sort the dataframe by the ballRecovery column in descending order and get the first player's name
top_player = df.sort_values(by = 'ballRecovery', ascending = False).iloc[0]
print(top_player['matchName'], '\n')

# Group by teamName and calculate the mean of successfulFinalThirdPasses for each group.
# The result will be a pandas Series with team names as the index and the average values as the data.
avg_final_third_passes = df.groupby('teamName')['successfulFinalThirdPasses'].mean()
print(avg_final_third_passes, '\n')

# Filter the dataframe for rows where gameStarted is 0 (substitutes)
substitutes_df = df[df['gameStarted'] == 0]

# Group by teamName and count the number of substitutes for each team
count_substitutes = substitutes_df.groupby('teamName').size()
print(count_substitutes, '\n')

# Group by 'teamName' and sum the 'wonTackle' for each group
total_tackles_by_team = df.groupby('teamName')['wonTackle'].sum()
print(total_tackles_by_team, '\n')

# Group by 'teamName' and 'position' and calculate the mean 'ballRecovery' for each group
avg_ball_recovery_by_team_position = df.groupby(['teamName', 'position'])['ballRecovery'].mean()
print(avg_ball_recovery_by_team_position, '\n')

# Find the player with the maximum 'totalScoringAtt'
top_scorer = df[df['totalScoringAtt'] == df['totalScoringAtt'].max()]['matchName'].iloc[0]
print(top_scorer, '\n')

# Exercises 2 My solutions:
df2 = pd.read_csv('https://s3.amazonaws.com/coderbyteprojectattachments/reatcodeltd-axldp-lkxhr3hf-CelticsvsRbLeipzig.csv')
print(df2, '\n')

def best_passer(df, team_name):
    names = df.query(f"teamName == '{team_name}'")
    results = names[names['accuratePass'] == names['accuratePass'].max()]
    return results['matchName'].item()

print(best_passer(df2, 'Celtic'), '\n')

def best_team_passes(df, team_name):
    return df.query(f"teamName == '{team_name}'").groupby('teamName')['accuratePass'].sum().item()

print(best_team_passes(df2, 'RB Leipzig'), '\n')

def total_goals(df, team_name):
    return df.query(f"teamName == '{team_name}'").groupby('teamName')['goals'].sum().item()

print(total_goals(df2, 'RB Leipzig'), '\n')

def best_performance(df):
    results = df[df['touches'] == df['touches'].max()]
    return results['matchName'].item()

print(best_performance(df2), '\n')

def most_active_team(df):
    results = df[df['totalPass'] == df['totalPass'].max()]
    return results['teamName'].item()

print(most_active_team(df2), '\n')

def top_defender(df):
    results = df[df['interceptionWon'] == df['interceptionWon'].max()]
    return results['matchName'].item()

print(top_defender(df2), '\n')

def goal_efficiency(df):
    def calculate_ratio(goals, totalScoringAtt):
        if totalScoringAtt == 0:
            return goals
        return goals / totalScoringAtt

    df['Total Scoring Attempts'] = df.apply(lambda row: calculate_ratio(row['goals'], row['totalScoringAtt']), axis = 1)
    results = df[df['Total Scoring Attempts'] == df['Total Scoring Attempts'].max()]
    return results['teamName'].item()

print(goal_efficiency(df2), '\n')

def most_efficient_sub(df):
    def calculate_ratio(successfulFinalThirdPasses, minsPlayed):
        if minsPlayed == 0:
            return 0
        return successfulFinalThirdPasses / minsPlayed

    df['Third Passes Ratio'] = df.apply(lambda row: calculate_ratio(row['successfulFinalThirdPasses'], row['minsPlayed']), axis = 1)
    names = df.query("gameStarted == 0")
    results = names[names['Third Passes Ratio'] == names['Third Passes Ratio'].max()]
    return results['matchName'].item()

print(most_efficient_sub(df2), '\n')
