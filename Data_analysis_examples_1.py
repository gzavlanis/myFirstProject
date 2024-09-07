import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""Example 1"""
data = pd.read_csv('./Data/sales_data1.csv') # load the dataset
print('Missing data:\n', data.isna().sum()) # check for missing data

data['Date'] = pd.to_datetime(data['Date']) # convert Date column to datetime format
data['Day_of_Week'] = data['Date'].dt.day_name() # Add a day of the week column
print('\nSummary Statistics:\n', data.describe()) # check the summary statistics

product_summary = data.groupby('Product').agg({'Revenue': 'sum', 'Quantity': 'sum'}) # group by Product and calculate total revenue and quantity sold
print('\nProduct Summary:\n', product_summary)

# Plot the total revenue per product
product_summary['Revenue'].plot(kind = 'bar')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.title('Total Revenue per Product')
# plt.show()

"""Example 2"""
# load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df = pd.read_csv(url, names = column_names, delim_whitespace = True)

# clean the dataset
df['horsepower'] = df['horsepower'].replace('?', np.nan)
df['horsepower'] = df['horsepower'].astype(float)
df.dropna(inplace = True)
print(df.describe())

# Exclude 'car_name' when calculating the correlation matrix
numeric_columns = df.select_dtypes(include = [np.number]).columns.tolist()
print(df[numeric_columns].corr())

# scatter plot of weight vs. mpg:
plt.scatter(df['weight'], df['mpg'])
plt.xlabel('Weight')
plt.ylabel('Miles Per Gallon')
plt.title('Weight vs. MPG')
# plt.show()

"""Example 3"""
# load the dataset into a Pandas dataframe:
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
  'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
  'Revenue': [100, 200, 150, 300, 120, 250, 170, 350, 110, 280]
}
df = pd.DataFrame(data)

# perform basic statistical analysis on the dataset:
total_revenue = np.sum(df['Revenue']) # calculate the total revenue
print('Total Revenue: ', total_revenue)

average_daily_revenue = np.mean(df['Revenue']) # Calculate the average revenue per day
print('Average revenue per day: ', average_daily_revenue)

product_revenue = df.groupby('Product')['Revenue'].sum() # calculate the total revenue for each product
print('Total revenue per product:\n', product_revenue)

# Visualize the data
# Bar chart of total revenue per product
fig, ax = plt.subplots()
ax.bar(product_revenue.index, product_revenue.values)
ax.set_xlabel('Product')
ax.set_ylabel('Revenue')
ax.set_title('Total Revenue per Product')
plt.show()

# Line chart of daily revenue
fix, ax = plt.subplots()
ax.plot(df['Date'], df['Revenue'])
ax.set_xlabel('Date')
ax.set_ylabel('Revenue')
ax.set_title('Daily Revenue')
plt.xticks(rotation = 45)
plt.show()

"""Example 4"""
df = pd.read_csv('./Data/movies.csv') # load the data into a DataFrame
df.dropna(inplace = True) # Remove any rows with missing values

# Convert the budget and revenue columns to numeric types
df['budget'] = pd.to_numeric(df['budget'])
df['revenue'] = pd.to_numeric(df['revenue'])

df['profit'] = df['revenue'] - df['budget'] # create a new column profit

# Calculate the summary statistics
budget_stats = df['budget'].describe()
revenue_stats = df['revenue'].describe()
profit_stats = df['profit'].describe()
print('Budget Stats:\n', budget_stats)
print('Revenue Stats:\n', revenue_stats)
print('Profit Stats:\n', profit_stats)

# Plot a histogram of the profit column
plt.hist(df['profit'], bins = 20)
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.title('Distribution of Profit')
plt.show()

# Create a scatter plot of budget versus revenue
plt.scatter(df['budget'], df['revenue'])
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.title('Budget vs Revenue')
plt.show()

"""Example 5"""
sales_data = pd.read_csv('./Data/sales_data2.csv') # read the CSV file

total_revenue = (sales_data['price'] * sales_data['quantity']).sum() # calculate the total revenue
print(f'Total Revenue: ${total_revenue}')

avg_order_value = sales_data.groupby('order_id')['price'].sum().mean() # calculate the average order value
print(f'Average Order Value: ${avg_order_value:.2f}')

# Identify the top-selling products.
product_sales = sales_data.groupby('product_id').agg({'quantity': 'sum'}).reset_index() # calculate product sales
product_sales = product_sales.sort_values(by = 'quantity', ascending = False) # sort the products by sales in descending order

# Get the top 5 selling products
top_selling_products = product_sales.head(5)
print('Top 5 selling products:\n', top_selling_products)

# Visualize the top-selling products using a bar chart
plt.bar(top_selling_products['product_id'], top_selling_products['quantity']) # set up the bar chart
plt.xlabel('Product ID')
plt.ylabel('Quantity Sold')
plt.title('Top 5 Selling Products')
plt.show()

"""Example 6"""
weather_data = pd.read_csv('./Data/weather_data.csv')
weather_data["date"] = pd.to_datetime(weather_data["date"]) # Convert the 'date' column to datetime format

# Extracting month and year from the date
weather_data["month"] = weather_data["date"].dt.month
weather_data["year"] = weather_data["date"].dt.year

weather_data['avg_temp'] = (weather_data['min_temp'] + weather_data['max_temp']) / 2 # calculating the average temperature for each day
monthly_avg_temp = (weather_data.groupby(['year', 'month'])['avg_temp'].mean().reset_index()) # calculating the monthly average temperature

# Finding the hottest and coldest days
hottest_day = weather_data.loc[weather_data['avg_temp'].idxmax()]
coldest_day = weather_data.loc[weather_data['avg_temp'].idxmin()]

# Display the results
print(monthly_avg_temp)
print(f"Hottest Day: {hottest_day['date'].strftime('%Y-%m-%d')} with an average temperature of {hottest_day['avg_temp']:.1f}°F", f"Coldest Day: {coldest_day['date'].strftime('%Y-%m-%d')} with an average temperature of {coldest_day['avg_temp']:.1f}°F")

# Plotting the histogram for temperature distribution
plt.figure(figsize = (10, 6))
sns.histplot(weather_data['avg_temp'], bins = 20, kde = True, color = 'skyblue', edgecolor = 'black')
plt.xlabel("Average Temperature (°F)", fontsize = 14)
plt.ylabel("Frequency", fontsize = 14)
plt.title("Temperature Distribution for January 2022", fontsize = 16)
plt.grid(True, which = "both", linestyle = "--", linewidth = 0.5)
plt.show()

"""Example 7"""
air_quality_data = pd.read_csv('./Data/air_quality_data.csv')
air_quality_data['date'] = pd.to_datetime(air_quality_data['date']) # Convert date column to datetime

# Extract month and year
air_quality_data['month'] = air_quality_data['date'].dt.month
air_quality_data['year'] = air_quality_data['date'].dt.year

# calculate the average PM2.5 concentration for each city
avg_pm25 = air_quality_data.groupby('city')['pm25'].mean().reset_index()
print('Average PM2.5 Concentration:\n', avg_pm25)

# Function to calculate AQI based on PM2.5 concentration
def calculate_aqi_pm25(pm25):
  if pm25 <= 12:
    aqi = (50 - 0) / (12 - 0) * (pm25 - 0) + 0
  elif pm25 <= 35.4:
    aqi = (100 - 51) / (35.4 - 12.1) * (pm25 - 12.1) + 51
  else:
    aqi = 101
  return aqi

air_quality_data['aqi_pm25'] = air_quality_data['pm25'].apply(calculate_aqi_pm25) # calculate AI for each record

# Calculate the monthly AQI for each city
monthly_aqi = air_quality_data.groupby(['city', 'year', 'month'])['aqi_pm25'].mean().reset_index()
print('Monthly Air Quality Index (AQI):\n', monthly_aqi)

pollutant_corr = air_quality_data[['pm25', 'no2', 'so2', 'co', 'o3']].corr() # calculate the correlation between pollutants

# Visualize the correlation using heatmap
plt.figure(figsize = (10, 8))
sns.heatmap(pollutant_corr, annot = True, cmap = 'coolwarm', linewidth = 0.5)
plt.title("Correlation Between Pollutants")
plt.show()

"""Example 8"""
betting_data = pd.read_csv("./Data/sports_betting_data.csv")

# Calculate the win rate
win_rate = betting_data[betting_data['bet_outcome'] == 'win'].groupby('bet_type')['bet_id'].count() / betting_data.groupby('bet_type')['bet_id'].count()
win_rate = win_rate.reset_index().rename(columns = {'bet_id': 'win_rate'})
print("Win Rate by Bet Type:")
print(win_rate)

# Calculate the betting returns
betting_data['returns'] = np.where(betting_data['bet_outcome'] == 'win', betting_data['bet_amount'] * (betting_data['odds'] - 1), -betting_data['bet_amount'])
betting_returns = betting_data.groupby('bet_type')['returns'].sum().reset_index()
print("Betting Returns by Bet Type:")
print(betting_returns)

winning_bets = betting_data[betting_data['bet_outcome'] == 'win'] # Filter the winning bets

# Set up the histogram
plt.hist(winning_bets['odds'], bins = 20, edgecolor = 'black')
plt.xlabel("Odds")
plt.ylabel("Frequency")
plt.title("Distribution of Winning Odds")
plt.show()

"""Example 9"""
admissions_data = pd.read_csv("./Data/hospital_admissions_data.csv")

# Convert admission_date and discharge_date to datetime
admissions_data['admission_date'] = pd.to_datetime(admissions_data['admission_date'])
admissions_data['discharge_date'] = pd.to_datetime(admissions_data['discharge_date'])

admissions_data['length_of_stay'] = (admissions_data['discharge_date'] - admissions_data['admission_date']).dt.days # Calculate length of stay

# Calculate the average length of stay by diagnosis
avg_length_of_stay = admissions_data.groupby('diagnosis')['length_of_stay'].mean().reset_index()
print("Average Length of Stay by Diagnosis:")
print(avg_length_of_stay)

diagnosis_counts = admissions_data.groupby('diagnosis')['admission_id'].count().reset_index().rename(columns = {'admission_id': 'count'}) # Count the number of admissions for each diagnosis

# Find the top 10 most common diagnoses
top_10_diagnoses = diagnosis_counts.nlargest(10, 'count')
print("Top 10 Most Common Diagnoses:")
print(top_10_diagnoses)

# Set up the histogram
plt.hist(admissions_data['age'], bins = 20, edgecolor = 'black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Patients")
plt.show()
