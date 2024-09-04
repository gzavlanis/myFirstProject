import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

fig = px.scatter(x, y, color_discrete_sequence = ['red'])
fig.update_traces(marker_size = 50)
fig.update_layout(title = 'Scatter plot of x vs y', xaxis_title = 'x values', yaxis_title = 'y values')
# fig.show()

months = ['January', 'February', 'March', 'April', 'May']
temperatures = [30, 35, 40, 50, 55]

fig = px.line(x = months, y = temperatures, color_discrete_sequence = ['blue'])
fig.update_traces(line = dict(width = 5))
fig.update_layout(title = 'Monthly Average Temperatures', xaxis_title = 'Temperature', yaxis_title = 'Month')
# fig.show()

# Create a dictionary with sales data for two products over four years
data = {
    'Year': [2017, 2018, 2019, 2020],
    'Product A': [2000, 2500, 2700, 3000],
    'Product B': [1500, 1800, 2100, 2400]
}
df = pd.DataFrame(data)

# create a new plotly figure object
fig = go.Figure()

# add a trace for Product A's sales
fig.add_trace(
    go.Scatter(
        x = df['Year'], y = df['Product A'], mode = 'lines+markers', name = 'Product A', line = dict(color = 'blue', width = 2), marker = dict(size = 8)
    )
)

# add a trace for product B's sales
fig.add_trace(
    go.Scatter(
        x = df['Year'], y = df['Product B'], mode = 'lines+markers', name = 'Product B', line = dict(color = 'red', width = 2), marker = dict(size = 8)
    )
)

# Update the layout of the figure
fig.update_layout(
    title = 'Sales per Year', xaxis_title = 'Year', yaxis_title = 'Sales', legend = dict(x = 0, y = 1, bgcolor = 'rgba(255, 255, 255, 0.5)'),
    plot_bgcolor = 'rgba(0, 0, 0, 0)', hovermode = 'x unified'
)
# fig.show()

# Create a dictionary with data of sales for four products
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": [2000, 2500, 1800, 2200],
}
df = pd.DataFrame(data)

# create a new plotly Figure object
fig = go.Figure()

# Add a bar trace to the figure
fig.add_trace(
    go.Bar(
        x = df['Product'], y = df['Sales'], text = df['Sales'], textposition = 'auto', marker_color = ['blue', 'red', 'green', 'purple'],
    )
)

# Update the layout of the figure
fig.update_layout(
    title = 'Sales in 2020', xaxis_title = 'Product', yaxis_title = 'Sales', plot_bgcolor = 'rgba(0, 0, 0,0)', hovermode = 'x unified'
)
# fig.show()

# Create a dictionary with data of market shares for four products
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Market Share': [30, 20, 25, 25]
}
df = pd.DataFrame(data)

# Create a Plotly Figure object
fig = go.Figure()

# Add a Pie trace to the figure
fig.add_trace(
    go.Pie(
        labels = df['Product'], values = df['Market Share'], textinfo = 'label+percent',
        marker = dict(
            colors = ['blue', 'red', 'green', 'purple'],
            line = dict(color = '#000000', width = 1)
        )
    )
)

# Update the layout of the figure
fig.update_layout(
    title = 'Market Share of Products', plot_bgcolor = 'rgba(0, 0, 0, 0)', hovermode = 'x unified'
)
# fig.show()

# Create a dictionary containing data for players, goals, and assists
data = {'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Kylian Mbappé'],
        'Goals': [31, 36, 19, 27],
        'Assists': [27, 7, 12, 7]}
df = pd.DataFrame(data)  # Convert the dictionary to a pandas DataFrame

fig = go.Figure()  # Create a new plotly Figure object

# Add a bar trace for goals, with blue bars and black borders
fig.add_trace(
    go.Bar(
        x = df['Player'], y = df['Goals'], name = 'Goals', marker = dict(color = 'blue', line = dict(color = '#000000', width = 1))
    )
)
# Add a bar trace for assists, with red bars and black borders
fig.add_trace(
    go.Bar(
        x = df['Player'], y = df['Assists'], name = 'Assists', marker = dict(color = 'red', line = dict(color = '#000000', width = 1))
    )
)

# Update the layout of the figure with a title, axis titles, and other settings
fig.update_layout(
    title = 'Goals and Assists in 2020 Season', xaxis_title = 'Player', yaxis_title = 'Goals and Assists', barmode = 'stack', plot_bgcolor = 'rgba(0, 0, 0, 0)', hovermode = 'x unified'
)
# fig.show()

# Create a dictionary with sales and profit data for four products
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": [2000, 2500, 1800, 2200],
    "Profit": [500, 700, 400, 600],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a plotly Figure object
fig = go.Figure()

# Add a bar trace for sales
fig.add_trace(
    go.Bar(
        x = df["Product"], y = df["Sales"], name = "Sales", marker = dict(color = "blue", line = dict(color = "#000000", width = 1)),
    )
)

# Add a bar trace for profit
fig.add_trace(
    go.Bar(
        x = df["Product"], y = df["Profit"], name = "Profit", marker = dict(color = "red", line = dict(color = "#000000", width = 1)),
    )
)

# Update the layout of the figure
fig.update_layout(
    title = "Sales and Profit in 2020", xaxis_title = "Product", yaxis_title = "Values", plot_bgcolor = "rgba(0, 0, 0, 0)", hovermode = "x unified", barmode = "group",
)
# fig.show()

# Create a dictionary with sales data for three products over four years
data = {
    'Year': [2017, 2018, 2019, 2020],
    'Product A': [2000, 2500, 2700, 3000],
    'Product B': [1500, 1800, 2100, 2400],
    'Product C': [1800, 2100, 2300, 2500]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a new plotly Figure object
fig = go.Figure()

# Add a trace for each product's sales
for product in ['Product A', 'Product B', 'Product C']:
    fig.add_trace(go.Scatter(x = df['Year'], y = df[product], mode = 'lines+markers', name = product))

# Update the layout of the figure
fig.update_layout(title = 'Sales per Year', xaxis_title = 'Year', yaxis_title = 'Sales', plot_bgcolor = 'rgba(0, 0, 0, 0)', hovermode = 'x unified')
# fig.show()

# Create a dictionary with market shares for four products
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Market Share': [30, 20, 25, 25]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a Plotly Figure object
fig = go.Figure()

# Add a Pie (Donut) trace to the figure
fig.add_trace(go.Pie(
    labels = df['Product'], values = df['Market Share'], hole = 0.4,  # This creates the 'donut' shape
    textinfo = 'label+percent', marker = dict(colors = ['blue', 'red', 'green', 'purple'])
))

# Update the layout of the figure
fig.update_layout(title = 'Market Share of Products', plot_bgcolor = 'rgba(0, 0, 0, 0)', hovermode = 'x unified')
# fig.show()

# Create a dictionary containing age data
data = {
    "ID": [
        "ID1",
        "ID2",
        "ID3",
        "ID4",
        "ID5",
        "ID6",
        "ID7",
        "ID8",
        "ID9",
        "ID10",
    ],
    "Age": [22, 24, 35, 45, 67, 72, 51, 48, 56, 33],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a histogram trace using the age data, with 5 bins and custom marker color
trace = go.Histogram(x = df["Age"], nbinsx = 5, name = "Age Distribution", marker = dict(color = "#1f77b4"))

# Define the layout for the plot, including the title
layout = go.Layout(title = "Population Age Distribution")

# Create a Figure object with the trace and layout
fig = go.Figure(data = [trace], layout = layout)
# fig.show()

# Create a dictionary containing employee names and their salaries
data = {
    "Employee": [
        "John",
        "Maria",
        "Steve",
        "Helen",
        "Tom",
        "Rose",
        "Mark",
        "Jenny",
        "Greg",
        "Sophia",
    ],
    "Salary": [34000, 36000, 29000, 22000, 28000, 30000, 40000, 35000, 37000, 32000],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a box plot trace using the employee salaries
trace = go.Box(
    y = df["Salary"],  # Set the y-axis values to the 'Salary' column of the DataFrame
    name = "Employee Salary",  # Set the trace name to 'Employee Salary'
    marker = dict(color = "#2ca02c"),  # Set the marker color to green
)

# Create a layout for the plot with a title
layout = go.Layout(title = "Employee Salary Distribution")

# Create a Figure object with the trace and layout
fig = go.Figure(data = [trace], layout = layout)
# fig.show()

# Create a dictionary containing product names and their sales
data = {
    "Product": [
        "Product A",
        "Product B",
        "Product C",
        "Product D",
        "Product E",
    ],
    "Sales": [1200, 1500, 900, 1800, 1600],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a histogram trace using the product sales
trace = go.Histogram(
    x = df["Sales"],  # Sales data
    nbinsx = 5,  # Number of bins
    name = "Product Sales",  # Name of the trace
    marker = dict(color = "#ff7f0e"),  # Color of the bars
)

# Create a layout for the plot with a title
layout = go.Layout(title = "Product Sales Distribution")

# Combine the trace and layout into a single Figure object
fig = go.Figure(data = [trace], layout = layout)
# fig.show()

# Create a dictionary containing customer IDs and their spending
data = {
    "Customer ID": [
        "Cust1",
        "Cust2",
        "Cust3",
        "Cust4",
        "Cust5",
    ],
    "Spending": [200, 150, 350, 400, 250],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a box plot trace using the customer spending
trace = go.Box(y = df["Spending"], name = "Customer Spending", marker = dict(color = "#d62728"))

# Define the layout for the plot, including the title
layout = go.Layout(title = "Customer Spending Distribution")

# Create a Figure object with the trace and layout
fig = go.Figure(data = [trace], layout = layout)
# fig.show()

# Define the data for the scatter plot
x_values = [1, 2, 3, 4, 5]  # List of x values
y_values = [2, 3, 1, 5, 4]  # List of y values

# Create a scatter plot using the data
fig = go.Figure(
    go.Scatter(
        x = x_values, y = y_values, mode = "markers",
        marker = dict(
            size = 15, color = ["red", "green", "blue", "orange", "purple"], showscale = True
        )
    )
)

# Update the layout of the scatter plot
fig.update_layout(title = "A Simple Scatter Plot", xaxis_title = "X Values", yaxis_title = "Y Values")
# fig.show()

# Define the data for the plot
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 1, 5, 4]
z_values = [1, 3, 2, 4, 1]  # Extra dimension for bubble size

# Create a scatter plot using the data
fig = go.Figure(
    go.Scatter(
        x = x_values,  # Set the x-axis values
        y = y_values,  # Set the y-axis values
        mode = "markers",  # Set the plot mode to display markers
        marker = dict(
            size = [a * 10 for a in z_values],  # Set the marker size based on z_values
            color = ["red", "green", "blue", "orange", "purple"],  # Set the marker colors
            showscale = True,  # Display a color scale
        )
    )
)

# Update the layout of the plot
fig.update_layout(
    title = "A Simple Bubble Chart",  # Set the plot title
    xaxis_title = "X Values",  # Set the x-axis title
    yaxis_title = "Y Values",  # Set the y-axis title
)
# fig.show()

# Create a dictionary containing data about X and Y coordinates
data = {
    "X": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Y": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot using the data
fig = go.Figure(
    go.Scatter(
        x = df['X'],  # Set the x-axis values
        y = df['Y'],  # Set the y-axis values
        mode = "markers",  # Set the plot mode to display markers
        marker = dict(
            size = 10,  # Set the marker size
            color = df['Y'],  # Set the marker colors based on 'Y' values
            showscale = True,  # Display a color scale
        ),
    )
)

# Update the layout of the scatter plot
fig.update_layout(
    title = "Scatter Plot of X and Y Values",  # Set the plot title
    xaxis_title = "X Values",  # Set the x-axis title
    yaxis_title = "Y Values",  # Set the y-axis title
)
# fig.show()

# Create a DataFrame
data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'UK'],
    'GDP': [65000, 10000, 7000, 45000, 40000],
    'Population': [331002651, 1439323776, 1380004385, 83783942, 67886011]
}
df = pd.DataFrame(data)

# Create a bubble chart
fig = go.Figure(
    go.Scatter(
        x = df['GDP'], y = df['Country'], mode = 'markers',
        marker = dict(
            size = df['Population'] / 1e8,  # Adjust the size parameter to properly scale the bubble sizes
            color = df['GDP'], showscale = True
        ),
        text = df['Country']  # This will add tooltips to each marker
    )
)

# Update the layout of the bubble chart
fig.update_layout(title = "Countries by Population and GDP", xaxis_title = "GDP per capita", yaxis_title = "Country")
# fig.show()

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 1, 5, 4]

fig = go.Figure(
    go.Scatter(
        x = x_values, y = y_values, mode = 'lines+markers',  # Add lines connecting the markers
        marker = dict(
            size = 10, color = y_values, showscale = True
        )
    )
)

fig.update_layout(title = "Scatter Plot with Line", xaxis_title = "X Values", yaxis_title = "Y Values")
# fig.show()

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 1, 5, 4]
sizes = [30, 80, 50, 100, 70]

fig = go.Figure()

for category, x, y, size in zip(categories, x_values, y_values, sizes):
    fig.add_trace(
        go.Scatter(
            x = [x], y = [y], mode = 'markers', name = category,
            marker = dict(
                size = [size], sizemode = 'diameter'
            ),
        )
    )

fig.update_layout(title = "Bubble Chart with Different Categories", xaxis_title = "X Values", yaxis_title = "Y Values")
fig.show()