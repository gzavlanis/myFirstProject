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