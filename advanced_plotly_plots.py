import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import numpy as np
import pandas as pd

# Define the data for the 3D scatter plot
items = ["Item1", "Item2", "Item3"]
x_data = [10, 15, 20]
y_data = [20, 25, 30]
z_data = [5, 10, 15]
w_data = [25, 10, 30]

# Create a 3D scatter plot using the data
fig = go.Figure(
    go.Scatter3d(
        x = x_data,  # Set the x-axis data
        y = y_data,  # Set the y-axis data
        z = z_data,  # Set the z-axis data
        mode = "markers",  # Set the plot mode to display markers
        marker = dict(
            size = w_data,  # Set the size of the markers based on the w_data
            sizemode = "diameter",  # Set the size mode to diameter
            sizeref = 0.1,  # Set the size reference value
            color = w_data,  # Set the color of the markers based on the w_data
            colorscale = "Viridis",  # Set the colorscale for the markers
            showscale = True,  # Show the color scale
        ),
        text = items  # Set the text labels for the markers
    )
)
# fig.show()

# Define the data for the plot
items = ["Item1", "Item2", "Item3"]
x_data = [10, 15, 20]
y_data = [20, 25, 30]
z_data = [5, 10, 15]

# Create a 3D scatter plot using the data
fig = go.Figure(
    go.Scatter3d(
        x = x_data,  # Set the x-axis data
        y = y_data,  # Set the y-axis data
        z = z_data,  # Set the z-axis data
        mode = "markers",  # Set the plot mode to display markers
        marker = dict(size = 5, color = "purple"),  # Set the marker size and color
        text = items,  # Set the text labels for each marker
    )
)

# Update the layout of the plot
fig.update_layout(
    scene = dict(
        xaxis_title = "X Axis Label",  # Set the x-axis title
        yaxis_title = "Y Axis Label",  # Set the y-axis title
        zaxis_title = "Z Axis Label",  # Set the z-axis title
        bgcolor = "lightgrey",  # Set the background color of the 3D scene
    ),
    plot_bgcolor = "white",  # Set the background color of the plot
    title = "3D Scatter Plot",  # Set the title of the plot
)
# fig.show()

# Simulate the data
np.random.seed(42)  # for reproducibility
n_stars = 500
x = np.random.normal(size = n_stars)  # simulate star x-coordinates
y = np.random.normal(size = n_stars)  # simulate star y-coordinates
z = np.random.normal(size = n_stars)  # simulate star z-coordinates

# Simulate star temperature as color
temp = np.random.randint(low = 3000, high = 6000, size = n_stars)
color = ['rgb({}, {}, 255)'.format(int(t / 6000 * 255), int(t / 6000 * 255)) for t in temp]

# Create the figure
fig = go.Figure(data = [go.Scatter3d(x = x, y = y, z = z, mode = 'markers', marker = dict(size = 6, color = color, opacity = 0.8))])

# Update the layout of the figure
fig.update_layout(
    title = 'Simulated Galaxy', scene = dict(xaxis = dict(title = 'X'), yaxis = dict(title = 'Y'), zaxis = dict(title = 'Z')),
    width = 800, height = 800, margin = dict(l = 0, r = 0, b = 0, t = 0))
# fig.show()

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fig = go.Figure(data = go.Heatmap(z = data, colorscale = 'Viridis', hoverongaps = False))
# fig.show()

player_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 0, 0, 1, 2, 1, 0],
    [0, 2, 4, 2, 0, 0, 2, 4, 2, 0],
    [0, 1, 2, 1, 0, 0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 0, 0, 1, 2, 1, 0],
    [0, 2, 4, 2, 0, 0, 2, 4, 2, 0],
    [0, 1, 2, 1, 0, 0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

fig = go.Figure(data = go.Heatmap(z = player_data, colorscale = "Inferno", hoverongaps = False))
fig.update_layout(title = "Activity Grid Heatmap")
# fig.show()

fig = go.Figure(
    data = go.Heatmap(
         z = player_data,
        colorscale = "Viridis",
        colorbar = dict(title = "Intensity")
    )
)
# fig.show()

fig = go.Figure(data = go.Heatmap(z = player_data))
fig.update_layout(
    title = 'Activity Grid Heatmap',
    xaxis_title = 'X Axis Label',
    yaxis_title = 'Y Axis Label'
)
# fig.show()

fig = go.Figure(data = go.Heatmap(z = player_data))
fig.update_layout(
    autosize = False,
    width = 800,
    height = 600,
    plot_bgcolor = "rgba(245, 245, 245, 1)"
)
# fig.show()

# Data: List of dictionaries containing location data (name, latitude, and longitude)
location_data = [
    {"name": "Location 1", "lat": 51.50, "lon": -0.12},
    {"name": "Location 2", "lat": 48.85, "lon": 2.35},
    {"name": "Location 3", "lat": -33.87, "lon": 151.21},
]

# Create a Scattergeo plot using the location_data
fig = go.Figure(
    go.Scattergeo(
        lat = [location["lat"] for location in location_data],
        lon = [location["lon"] for location in location_data],
        text = [location["name"] for location in location_data],
        mode = "markers",
        marker = dict(
            size = 15,
            color = "rgba(0, 0, 255, 0.8)",
            line = dict(width = 2, color = "rgba(255, 255, 255, 0.8)"),
        ),
    )
)

# Customize the map's appearance
fig.update_geos(
    projection_type = "natural earth",
    showcountries = True,
    countrycolor = "rgb(204, 204, 204)",
    showcoastlines = True,
    coastlinecolor = "rgb(204, 204, 204)",
    showland = True,
    landcolor = "rgb(243, 243, 243)",
    showocean = True,
    oceancolor = "rgb(217, 217, 217)",
    showlakes = True,
    lakecolor = "rgb(255, 255, 255)",
    showrivers = True,
    rivercolor = "rgb(255, 255, 255)",
)

# Set the plot's layout
fig.update_layout(
    title = "Geographic Locations",
    font = dict(
        family = "Arial, sans-serif", size = 12, color = "rgb(37, 37, 37)"
    ),
    hovermode = "closest",
)
# fig.show()

# Mock dataset
data = {
    "country": ["China", "India", "USA", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"],
    "population": [1393000000, 1366000000, 331000000, 273000000, 225000000, 213000000, 211000000, 166000000, 146000000, 130000000]
}
df = pd.DataFrame(data)

fig = px.choropleth(
    df,
    locations = "country",
    locationmode = "country names",
    color = "population",
    title = "World Population Visualization",
    hover_name = "country",
    color_continuous_scale = px.colors.sequential.Plasma,
    projection = "natural earth"
)
# fig.show()

# Mock dataset
data = {
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "lat": [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 39.9526, 29.4241, 32.7157, 32.7767, 37.3382],
    "lon": [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -75.1652, -98.4936, -117.1611, -96.7970, -121.8863],
    "temperature": [25, 30, 28, 33, 38, 29, 36, 31, 32, 30]
}
df = pd.DataFrame(data)

fig = go.Figure(
    data = go.Scattergeo(
        lon = df['lon'],
        lat = df['lat'],
        text = df['city'],
        mode = 'markers',
        marker = dict(
            size = df['temperature'],
            color = df['temperature'],
            colorscale = 'Viridis',
            showscale = True,
            colorbar_title = "Temperature,<br>°C",
        )
    )
)

fig.update_layout(
    title_text = 'Real-Time Weather Data Visualization',
    geo_scope = 'usa',  # limit map scope to USA
)
# fig.show()

# Define a list of entities and their respective values
entities = ['Entity A', 'Entity B', 'Entity C']
values = [672, 674, 366]

# Create a bar chart with custom colors for each bar
trace = go.Bar(
    x = entities,  # Set the x-axis values to the list of entities
    y = values,  # Set the y-axis values to the list of values
    marker = dict(
        color = ['gold', 'crimson', 'limegreen'],  # Set the colors of the bars
        line = dict(color = 'black', width = 1.5)  # Set the border color and width of the bars
    )
)

# Define the layout of the chart, including title and background color
layout = go.Layout(
    title = dict(
        text = 'Example Chart',  # Set the chart title
        font = dict(size = 24, color = 'darkblue')  # Set the font size and color of the title
    ),
    plot_bgcolor = 'lightgray'  # Set the background color of the plot
)

# Create a Figure object with the trace and layout
fig = go.Figure(data = [trace], layout = layout)

# Display the chart
# pio.show(fig)

# Create a bar chart with custom text
trace = go.Bar(
    x = entities,
    y = values,
    text = values,  # Display the values as text inside the bars
    textposition = "inside",  # Position the text inside the bars
    textfont = dict(color = "white", size = 16),  # Set the text font color and size
    marker = dict(
        color = ["gold", "crimson", "limegreen"],  # Set the bar colors
        line = dict(color = "black", width = 1.5),  # Add a black border around the bars
    ),
)

# Define the layout of the chart
layout = go.Layout(
    title = dict(
        text = "Example Chart",  # Set the chart title
        font = dict(size = 24, color = "darkblue"),  # Set the title font size and color
    ),
    plot_bgcolor = "lightgray",  # Set the background color of the plot
)

# Create the figure with the trace and layout
fig = go.Figure(data = [trace], layout = layout)

# Show the chart
# pio.show(fig)

# Create a bar chart trace with custom text and marker properties
trace = go.Bar(
    x = entities,
    y = values,
    text = values,
    textposition = "inside",
    textfont = dict(color = "white", size = 16),
    marker = dict(
        color = ["gold", "crimson", "limegreen"],
        line = dict(color = "black", width = 1.5)
    ),
)

# Create a custom layout for the chart
layout = go.Layout(
    title = dict(
        text = "Example Chart",
        font = dict(size = 24, color = "darkblue")
    ),
    xaxis = dict(
        title = "Entities",
        titlefont = dict(size = 18, color = "darkred")
    ),
    yaxis = dict(
        title = "Values",
        titlefont = dict(size = 18, color = "darkred")
    ),
    plot_bgcolor = "lightgray",
)

# Create a Figure object with the trace and layout
fig = go.Figure(data = [trace], layout = layout)

# Display the chart
# pio.show(fig)

entities = ["Entity A", "Entity B", "Entity C"]
values = [305, 229, 216]

# Create a line chart with custom colors
trace = go.Scatter(
    x = entities,
    y = values,
    mode = "lines+markers",
    marker = dict(color = "blue", size = 10, line = dict(color = "black", width = 2)),
    line = dict(color = "blue", width = 3),
)
layout = go.Layout(
    title = dict(
        text = "Example Line Chart", font = dict(size = 24, color = "darkblue")
    ),
    plot_bgcolor = "lightgray",
)
fig = go.Figure(data = [trace], layout = layout)
# pio.show(fig)

labels = ["Label A", "Label B", "Label C"]
values = [305, 229, 216]

# Create a pie chart with custom text
trace = go.Pie(
    labels = labels,
    values = values,
    textinfo = 'label+percent',  # Display label and percent
    textfont = dict(size = 18),  # Set font size
    marker = dict(
        colors = ['blue', 'green', 'red'],  # Set color for each pie slice
        line = dict(color = 'black', width = 2),  # Add a black border around the pie slices
    ),
)
layout = go.Layout(
    title = dict(
        text = "Example Pie Chart", font = dict(size = 24, color = "darkblue")
    ),
)
fig = go.Figure(data = [trace], layout = layout)
# pio.show(fig)

# Define the data for the chart: soccer players and their goals
players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr"]
goals = [672, 674, 366]

# Create a bar chart with custom background color and text properties
trace = go.Bar(
    x=players,  # Set the x-axis values to the players' names
    y=goals,  # Set the y-axis values to the players' goals
    text=goals,  # Display the goals as text inside the bars
    textposition="inside",  # Position the text inside the bars
    textfont=dict(color="white", size=16),  # Set the text color and size
    marker=dict(
        color=["gold", "crimson", "limegreen"],  # Set the bar colors
        line=dict(color="black", width=1.5),  # Add a black border around the bars
    ),
)
layout = go.Layout(
    title=dict(
        text="Top 3 Soccer Players by Goals",  # Set the chart title
        font=dict(size=24, color="darkblue"),  # Set the title font size and color
    ),
    plot_bgcolor="lightgray",  # Set the background color of the plot
    margin=dict(l=50, r=50, t=50, b=50),  # Set the margins around the plot
)
fig = go.Figure(
    data=[trace], layout=layout
)  # Create a Figure object with the trace and layout

# Show the chart
# pio.show(fig)

# Define the data for the chart: soccer players and their goals
players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr"]
goals = [672, 674, 366]

# Create a bar chart with custom background color and text properties
trace = go.Bar(
    x = players,  # Set the x-axis values to the players' names
    y = goals,  # Set the y-axis values to the players' goals
    text = goals,  # Display the goals as text inside the bars
    textposition = "inside",  # Position the text inside the bars
    textfont = dict(color = "white", size = 16),  # Set the text color and size
    marker = dict(
        color = ["gold", "crimson", "limegreen"],  # Set the bar colors
        line = dict(color = "black", width = 1.5),  # Add a black border around the bars
    ),
)
layout = go.Layout(
    title = dict(
        text = "Top 3 Soccer Players by Goals",  # Set the chart title
        font = dict(size = 24, color = "darkblue"),  # Set the title font size and color
    ),
    plot_bgcolor = "lightgray",  # Set the background color of the plot
    margin = dict(l = 50, r = 50, t = 50, b = 50),  # Set the margins around the plot
)
fig = go.Figure(
    data = [trace], layout = layout
)  # Create a Figure object with the trace and layout

# Show the chart
# pio.show(fig)

data = {'Subject': ['Physics', 'Chemistry', 'Biology', 'Maths', 'Computer Science'],
        'Students': [47, 35, 42, 38, 50],
        'Pass Percentage': [86, 74, 80, 83, 92]}
df = pd.DataFrame(data)

fig = px.scatter(df, x = 'Students', y = 'Pass Percentage', hover_data = ['Subject'])
# fig.show()

data = {
    "Subject": ['Physics', 'Chemistry', 'Biology', 'Maths', 'Computer Science', 'History', 'Geography', 'Economics', 'Political Science', 'Psychology'],
    "Students": [47, 35, 42, 38, 50, 32, 37, 40, 36, 42],
    "Pass Percentage": [86, 74, 80, 83, 92, 75, 82, 78, 85, 87],
    "Department": ['Science', 'Science', 'Science', 'Science', 'Science', 'Arts', 'Arts', 'Arts', 'Arts', 'Arts']
}
df = pd.DataFrame(data)

fig = go.Figure()

for department in df["Department"].unique():
    fig.add_trace(
        go.Scatter(
            x = df[df["Department"] == department]["Students"],
            y = df[df["Department"] == department]["Pass Percentage"],
            mode = "markers",
            name = department,
            text = df[df["Department"] == department]["Subject"],
            visible = False,
        )
    )
fig.data[0].visible = True

buttons = [
    dict(
        label = department,
        method = "update",
        args = [
            {"visible": [department == dep for dep in df["Department"].unique()]},
            {"title": f"Department: {department}"},
        ],
    )
    for department in df["Department"].unique()
]
fig.update_layout(updatemenus = [dict(showactive = True, buttons = buttons)])
# fig.show()

# Create a sample DataFrame
data = {
    'Year': [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Lionel Messi', 'Cristiano Ronaldo', 'Neymar'],
    'Team': ['FC Barcelona', 'Juventus', 'Paris Saint-Germain', 'FC Barcelona', 'Juventus', 'Paris Saint-Germain', 'Paris Saint-Germain', 'Manchester United', 'Paris Saint-Germain'],
    'Goals': [25, 28, 20, 30, 33, 26, 32, 31, 29]
}
df = pd.DataFrame(data)

# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for year in df['Year'].unique():
    fig.add_trace(
        go.Scatter(
            visible = False,
            line = dict(color = "#00CED1", width = 6),
            name = "𝜈 = " + str(year),
            x = df.loc[df['Year'] == year, 'Player'],
            y = df.loc[df['Year'] == year, 'Goals']))

# Make 1st trace visible
fig.data[0].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method = "update",
        args = [{"visible": [False] * len(fig.data)}, {"title": "Slider switched to year: " + str(df['Year'].unique()[i])}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(active = 0, currentvalue = {"prefix": "Year: "}, pad = {"t": 50}, steps = steps)]

fig.update_layout(sliders = sliders)
# fig.show()

# Create hypothetical data
data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022,] * 5,
    "Club": ["FC Barcelona"] * 13 + ["Real Madrid"] * 13 + ["Manchester United"] * 13 + ["Paris Saint-Germain"] * 13 + ["Bayern Munich"] * 13,
    "Goals": [
        # FC Barcelona
        80, 82, 75, 85, 90, 82, 81, 86, 89, 78, 92, 85, 90,
        # Real Madrid
        85, 88, 79, 82, 92, 85, 88, 92, 95, 89, 95, 98, 99,
        # Manchester United
        70, 75, 72, 78, 80, 77, 78, 82, 85, 78, 85, 88, 90,
        # Paris Saint-Germain
        60, 65, 70, 72, 75, 78, 80, 82, 88, 90, 92, 95, 98,
        # Bayern Munich
        75, 78, 80, 82, 85, 88, 89, 90, 92, 95, 97, 100, 102,
    ],
}
# Create pandas DataFrame
df = pd.DataFrame(data)

# Create an animated bar chart using Plotly
fig = px.bar(
    df,
    x = "Club",  # Set x-axis to 'Club'
    y = "Goals",  # Set y-axis to 'Goals'
    animation_frame = "Year",  # Animate the chart based on 'Year'
    title = "Goals Scored by Top Football Clubs Over the Years",  # Set chart title
    labels = {"Goals": "Total Goals", "Club": "Football Club"},  # Customize axis labels
    color = "Club",
)  # Color bars based on 'Club'

# Set the y-axis range from 0 to 110
fig.update_yaxes(range = [0, 110])

# Set the animation frame duration to 1000 milliseconds (1 second)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
fig.show()
