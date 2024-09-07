import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv('./Data/vgsales.csv')
df.dropna(inplace = True) # drop rows with missing values

"""Question 1: What are the top-selling video games of all time?"""
game_sales = df.groupby('Name')['Global_Sales'].sum() # group data by game and sum global sales
game_sales = game_sales.sort_values(ascending = False) # sort by global sales
print(game_sales.head(10)) # display top 10 games

"""Question 2: Which platform is the most popular?"""
platform_sales = df.groupby('Platform')['Global_Sales'].sum() # group data by platform and sum global sales
platform_sales = platform_sales.sort_values(ascending = False) # sort by global sales
print(platform_sales) # display platform sales

"""Question 3: Which genre is the most popular?"""
genre_sales = df.groupby('Genre')['Global_Sales'].sum() # group data by genre and sum global sales
genre_sales = genre_sales.sort_values(ascending = False) # sort by global sales
print(genre_sales) # display genre sales

"""Question 4: How do sales vary by region?"""
region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
region_sales.plot(kind = 'bar')
plt.title('Video Game Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales (millions)')
plt.show()

"""Question 5: Is there a relationship between the year of release and sales?"""
plt.scatter(df['Year'], df['Global_Sales'])
plt.title('Year of Release vs Global Sales')
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.show()

"""Question 6: Is there a relationship between publisher and sales?"""
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum() # group data by publisher and sum global sales
publisher_sales = publisher_sales.sort_values(ascending = False) # sort by global sales

# create a bar chart showing top publishers by global sales
publisher_sales.head(10).plot(kind = 'bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()

"""Question 7: Can we use a Poisson distribution to model video game sales data?"""
# calculate mean and variance of global sales data
mean_sales = df['Global_Sales'].mean()
var_sales = df['Global_Sales'].var()

# calculate expected mean and variance of Poisson distribution
exp_mean = var_sales
exp_var = var_sales

# compare mean and variance to expected values for Poisson distribution
print('Mean of global sales data:', mean_sales)
print('Variance of global sales data:', var_sales)
print('Expected mean of Poisson distribution:', exp_mean)
print('Expected variance of Poisson distribution:', exp_var)

def poisson_probability(k, lam):
    return (lam ** k) * math.exp(-lam) / math.gamma(k + 1)

mean_sales = np.mean(df['Global_Sales']) # compute the men of the global sales data
n, bins, patches = plt.hist(df['Global_Sales'], bins = 50, density = True, alpha = 0.5) # generate a histogram of the global sales data
poisson_dist = [poisson_probability(b, mean_sales) for b in bins] # calculate the Poisson distribution for the mean

# plot the Poisson distribution over the histogram
plt.plot(bins, poisson_dist, 'r-', linewidth = 2)
plt.title('Global Sales Data and Poisson Distribution')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Probability')
plt.show()
