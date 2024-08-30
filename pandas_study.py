import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Field': ['Engineer', 'Engineer', 'Scientist', 'Engineer', 'Scientist'],
    'Projects': [10, 9, 15, 7, 16]
}

df = pd.DataFrame(data)
print(df)
print()
print(df.shape) # prints number of rows and columns
print(df.head()) # prints the first 5 rows of the dataframe
print(df.columns) # prints the names of all columns
print(df.info()) # prints the number of non-null values and the datatype for each column
print()

max_projects = df["Projects"].max()
min_projects = df["Projects"].min()
mean_projects = df["Projects"].mean()
print(max_projects)
print(min_projects)
print(mean_projects)
print()

sorted_values = df.sort_values("Projects", ascending = False)
print(sorted_values)
print()

grouped_values = df.groupby("Field")["Projects"].sum()
print(grouped_values)
print()

# Series
quantities = [45, 30, 80, 20]
fruits = pd.Series(quantities, index = ['Apples', 'Oranges', 'Bananas', 'Grapes'])
print(fruits)
print()

data = {'Apples': 45, 'Oranges': 30, 'Bananas': 80, 'Grapes': 20}
fruits = pd.Series(data)
print(fruits)
print()

quantities = np.array([45, 30, 80, 20])
fruits = pd.Series(quantities, index = ['Apples', 'Oranges', 'Bananas', 'Grapes'])
print(fruits)
print()

print(fruits[1])
print(fruits['Oranges'])
print(fruits[1:3])
print()

updated_fruits = fruits + 5
print(updated_fruits)

mean_quantity = fruits.mean()
print("Mean quantity:", mean_quantity)

abundant_fruits = fruits[fruits > 40]
print(abundant_fruits)

# Dataframes
data = {
    'Category': ['Books', 'Electronics', 'Clothing', 'Garden'],
    'Items': ['Harry Potter', 'iPhone', 'T-Shirt', 'Lawn Mower'],
    'Count': [5, 3, 10, 1]
}
df = pd.DataFrame(data)
print(df)
print()

data = [
    ['Books', 'Harry Potter', 5],
    ['Electronics', 'iPhone', 3],
    ['Clothing', 'T-Shirt', 10],
    ['Garden', 'Lawn Mower', 1]
]
columns = ['Category', 'Items', 'Count']
df = pd.DataFrame(data, columns = columns)
print(df)
print()

items = df['Items']
print(items)
print()

selected_columns = ['Category', 'Items']
selected_data = df[selected_columns]
print(selected_data)
print()

high_count = df[df["Count"] > 5]
print(high_count)
print()

# Add new column:
df['Price'] = [29.99, 999.99, 9.99, 125.0]
print(df)
print()

# Update existing column:
df['Count'] = df['Count'] + 1
print(df)
print()

# Delete a column:
df.drop('Price', axis = 1, inplace = True)
print(df)
print()

# Sorting by column:
sorted_data = df.sort_values(by = 'Count', ascending = False)
print(sorted_data)
print()

filtered_data = df[df['Count'] > 5]
print(filtered_data)
print()

total_count = df['Count'].sum()
print(total_count)
print()

# Import and Export data
data = pd.read_csv('./Data/data.csv')
print(data.head())
print()

data2 = pd.read_excel('./Data/Project-Management-Sample-Data.xlsx')
print(data2.head())
print()

data.to_csv('./Data/exported_data.csv', index = False)
data.to_excel('./Data/exported_data.xlsx', index = False)

# DataFrame Attributes
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 35, 19],
    'Score': [85, 91, 77, 98],
    'Passed': [True, True, False, True]
}
df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print()

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 27, 45, 35],
    'Company': ['Company A', 'Company B', 'Company A', 'Company C', 'Company B'],
    'Salary': [5000, 7000, 5500, 8000, 6500],
    'Experience': [2, 5, 3, 7, 4]
})

print(data.describe())
print(data.count())
print(data.min())
print(data.max())
# print(data.mean())

# indexing and Slicing
data = {
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Role': ['Engineer', 'Manager', 'Analyst'],
    'Salary': [70000, 80000, 60000],
    'Experience': [5, 7, 3]
}
df = pd.DataFrame(data)

row = df.loc[df['Employee'] == 'Alice']
print(row)
print()

row = df.iloc[1]
print(row)
print()

rows = df.loc[df['Role'] == 'Engineer', ['Employee', 'Salary']]
print(rows)
print()

rows = df.iloc[[0, 2], [0, 2]]
print(rows)
print()

# Case study 1:
# Define data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Brown', 'Alice Johnson', 'Charlie Davis', 'Elizabeth Green', 'James White', 'Linda Miller', 'David Clark', 'Jennifer Rodriguez'],
    'Occupation': ['Engineer', 'Doctor', 'Lawyer', 'Artist', 'Scientist', 'Teacher', 'Nurse', 'Journalist', 'Actor', 'Architect'],
    'Age': [30, 28, 29, 32, 31, 30, 32, 33, 32, 30],
    'Experience': [5, 3, 4, 2, 5, 2, 3, 1, 2, 4],
    'Projects': [12, 7, 15, 11, 7, 16, 2, 10, 11, 6],
    'Sick_Days': [1, 3, 4, 2, 1, 2, 3, 1, 2, 2],
    'Vacation_Days': [10, 12, 15, 12, 10, 9, 11, 13, 10, 14]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print()

# Print the shape of the DataFrame
print('DataFrame Shape:', df.shape, '\n')

# Print the columns of the DataFrame
print('DataFrame Columns:', df.columns, '\n')

# Print the info of the DataFrame
print('DataFrame Info:')
print(df.info())

# Print the descriptive statistics for the DataFrame
print('DataFrame Statistics:')
print(df.describe(), '\n')

# Print the mean number of years of experience
print('Mean Experience:', df['Experience'].mean(), '\n')

# Print the individual with the most projects
print('Individual with Most Projects:', df['Name'][df['Projects'].idxmax()])

# Print the first 5 rows of the DataFrame
print('First 5 Rows:')
print(df.head(), '\n')

# Print the 'Name' and 'Experience' columns for all individuals who have more than 5 years of experience
print('Individuals with More Than 5 Years of Experience:')
print(df.loc[df['Experience'] > 5, ['Name', 'Experience']], '\n')

# Print the row for 'John Doe'
print('Row for John Doe:')
print(df.loc[df['Name'] == 'John Doe'])

# Data cleaning
data = {
    'Name': ['Alice', 'Bob', None, 'Eve'],
    'Age': [25, 32, 45, None],
    'Profession': ['Engineer', None, 'Doctor', 'Artist']
}
df = pd.DataFrame(data)

print(df.isnull())
print()
print(df.notnull())
print()

print(df.dropna())
print(df.fillna('Unknown'))

# Manage Dublicates
data = {'Name': ['Alice', 'Bob', 'Eve', 'Alice', 'Eve'],
        'Age': [25, 32, 29, 25, 29]}
df = pd.DataFrame(data)

duplicates = df.duplicated()
print(duplicates)
print()

df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)
print()

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 32, 29],
        'City': ['New York', 'London', 'Sydney']}
df = pd.DataFrame(data)
df.rename(columns = {'Name': 'Full Name', 'Age': 'Age in Years', 'City': 'Residence'}, inplace = True)
print(df)
print()

df.replace('New York', 'NYC', inplace = True)
print(df)
print()

# Case study 2: Data cleaning
data = {
    'Name': ['John Doe', 'Jane Smith', 'Bill Gates', 'Elon Musk', 'John Doe', None, 'Steve Jobs', 'Mark Zuckerberg', 'Jack Dorsey', 'Sundar Pichai'],
    'Previous_Team': ['Team Alpha', 'Team Bravo', 'Team Charlie', 'Team Delta', 'Team Alpha', 'Team Echo', 'Team Foxtrot', 'Team Golf', 'Team Hotel', None],
    'Current_Team': ['Team Bravo', 'Team Charlie', 'Team Delta', 'Team Echo', 'Team Bravo', 'Team Foxtrot', 'Team Golf', 'Team Hotel', 'Team India', 'Team Juliet'],
    'Contract_Fee_Millions': [0, 15, 222, 180, 0, 37, 35, 76, 85, 42],
    'Contract_Transition_Date': ['2021-08-10', '2021-08-31', '2017-08-03', '2018-07-01', '2021-08-10', None, '2014-07-01', '2015-08-30', '2018-07-01', '2017-07-01']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print()

# print the number of missing values in each column
print('Missing Values:')
print(df.isnull().sum(), '\n')

# fill missing names and previous team with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
df['Previous_Team'] = df['Previous_Team'].fillna('Unknown')

# drop rows with missing contract transition dates
df = df.dropna(subset = ['Contract_Transition_Date'])

# print the dataframe after handling missing values
print('\nDataFrame after handling missing values:')
print(df)
print()

# print the number of duplicates
print('\nNumber of Duplicates:', df.duplicated().sum(), '\n')

# drop duplicates
df.drop_duplicates(inplace = True)

# print the dataframe after removing duplicates
print('\DataFrame after removing duplicates:')
print(df)
print()

# Define new column names
new_column_names = {
    'Name': 'name',
    'Previous_Team': 'previous_team',
    'Current_Team': 'current_team',
    'Contract_Fee_Millions': 'contract_fee_millions',
    'Contract_Transition_Date': 'contract_transition_date'
}

# rename columns
df = df.rename(columns = new_column_names)

# print the dataframe after renaming columns
print('\nDataFrame after renaming columns:')
print(df)
print()

# Data manipulation
data = {'Name': ['Charlie', 'Alice', 'Bob', 'Dave', 'Eve'],
        'Attribute1': [20, 60, 50, 90, 70],
        'Attribute2': [18, 22, 16, 19, 20]}
df = pd.DataFrame(data)

# sort dataframe by index
sorted_df = df.sort_index(ascending = False)
print(sorted_df, '\n')

# sort dataframe by Attribute1 column in descending order
sorted_df = df.sort_values(by = 'Attribute1', ascending = False)
print(sorted_df, '\n')

# rank individuals by Attribute1
df['Attribute_Rank'] = df['Attribute1'].rank(ascending = False, method = 'min')
print(df, '\n')

data = {'Name': ['Charlie', 'Alice', 'Bob'],
        'Attribute1': [672, 450, 166],
        'Attribute2': [305, 131, 103]}
df = pd.DataFrame(data)

def sum_attributes(row):
    return row['Attribute1'] + row['Attribute2']

df['Total_Attributes'] = df.apply(sum_attributes, axis = 1)
print(df, '\n')

def format_data(element):
    if isinstance(element, int):
        return f"{element:,}"
    return element

df = df.map(format_data)
print(df,'\n')

data = {'Name': ['Charlie', 'Alice', 'Bob'],
        'Attribute1': [672345, 450123, 166789],
        'Attribute2': [305, 131, 103]}
df = pd.DataFrame(data)

def format_attributes(attr):
    return f"{attr:,}"

df['Attribute1'] = df['Attribute1'].map(format_attributes)
print(df, '\n')

# Grouping data:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Field': ['Engineer', 'Engineer', 'Scientist', 'Engineer', 'Scientist'],
    'Projects': [10, 9, 15, 7, 16]
}
df = pd.DataFrame(data)

grouped_data = df.groupby('Field')['Projects'].sum()
print(grouped_data, '\n')

# Merging, Joining, and Reshaping Data with Pandas 📈🐼
# Sample DataFrames
employees = pd.DataFrame({'employee_id': [1, 2, 3],
                          'name': ['Alice', 'Bob', 'Charlie']})
departments = pd.DataFrame({'department_id': [1, 2, 3],
                            'department_name': ['HR', 'Sales', 'Engineering']})

# merging dataframes
merged_data = pd.merge(employees, departments, left_on = 'employee_id', right_on = 'department_id')
print(merged_data, '\n')

employees = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie']},
                         index=[1, 2, 3])
departments = pd.DataFrame({'department_name': ['HR', 'Sales', 'Engineering']},
                           index=[1, 2, 3])

# joining dataframes
joined_data = employees.join(departments, lsuffix = '_employee', rsuffix = '_department')
print(joined_data, '\n')

data = pd.DataFrame({'employee': ['Alice', 'Bob', 'Charlie'],
                     'department': ['HR', 'Sales', 'Engineering'],
                     'projects': [5, 7, 9]})

# reshaping data
pivoted_data = data.pivot(index = 'employee', columns = 'department', values = 'projects')
print(pivoted_data, '\n')

# reshaping again with melt()
melted_data = pd.melt(data, id_vars = ['employee'], value_vars = ['department', 'projects'], var_name = 'attribute', value_name = 'value')
print(melted_data, '\n')

# Case study 3: Data Cleaning
# Define player data
player_data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappé', 'Robert Lewandowski'],
    'Team': ['PSG', 'Manchester United', 'PSG', 'PSG', 'Bayern Munich'],
    'Position': ['Forward', 'Forward', 'Forward', 'Forward', 'Forward']
}

# Create player DataFrame
df_player = pd.DataFrame(player_data)

# Define performance data
performance_data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappé', 'Robert Lewandowski'],
    'Goals': [30, 31, 27, 33, 36],
    'Assists': [15, 12, 17, 15, 9]
}

# Create performance DataFrame
df_performance = pd.DataFrame(performance_data)

# Display the DataFrames
print('Player DataFrame:')
print(df_player)
print('\nPerformance DataFrame:')
print(df_performance,'\n')

# define function to calculate goal-assist ratio
def calculate_ratio(goals, assists):
    if assists == 0:
        return goals
    return goals / assists

# add new column
df_performance['Goal_Assist_Ratio'] = df_performance.apply(lambda row: calculate_ratio(row['Goals'], row['Assists']), axis = 1)

# print the updated dataframe
print('\nPerformance DataFrame with Goal-Assist Ratio:')
print(df_performance, '\n')

# sort by goals
df_sorted_goals = df_performance.sort_values('Goals', ascending = False)

# add rank based on goals
df_sorted_goals['Goal_Rank'] = df_sorted_goals['Goals'].rank(ascending = False)

# Print the updated DataFrame
print('\nDataFrame Sorted by Goals:')
print(df_sorted_goals, '\n')

# group by team
df_grouped = df_player.groupby('Team').size()

# Print the grouped DataFrame
print('\nNumber of Players per Team:')
print(df_grouped, '\n')

# merge the dataframes on 'Player'
df_merged = pd.merge(df_player, df_performance, on = 'Player')

# print the merged dataframe
print('\nMerged DataFrame:')
print(df_merged, '\n')