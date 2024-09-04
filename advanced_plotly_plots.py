import plotly.graph_objects as go
import numpy as np

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

