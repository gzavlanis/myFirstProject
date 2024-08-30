import numpy as np

my_array = np.array([1, 2, 3])
print(my_array.shape)

my_array = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
])
print(my_array.shape)

ones = np.ones(4)
zeros = np.zeros((3, 3))
print(ones)
print(zeros)

my_array = np.array(["Bob", "Steve", "Sophia", "maria"])
print(my_array[1:2])
print(my_array[:2])
print(my_array[:3])

array1 = np.array([10, 9])
array2 = np.array([5, 6])

print(np.add(array1, array2))
print(np.subtract(array1, array2))
print(np.multiply(array1, array2))

numbers = np.array([34, 33, 29,28, 27])
print(numbers)

matrix = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print(matrix)

measurements = np.array([[185, 75], [170, 68], [192, 82], [178, 70], [175, 77]])
print(measurements)

tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor)

# 3D array where each layer represents a different group, rows represent individuals, and columns represent different measurements (height, weight)
group_measurements = np.array([[[185, 75], [170, 68], [192, 82], [178, 70], [175, 77]],
                               [[180, 72], [176, 78], [182, 80], [174, 72], [177, 69]],
                               [[188, 78], [180, 71], [182, 75], [179, 73], [176, 70]]])
print(group_measurements)

zeros = np.zeros((3, 3))
print("Zeros:\n", zeros)

ones = np.ones((3, 3))
print("\nOnes:\n", ones)

identity = np.eye(3)
print("\nIdentity matrix:\n", identity)

full = np.full((3, 3), 7)
print("\nFull:\n", full)

arange = np.arange(0, 10, 2)
print("\nArange:\n", arange)

linspace = np.linspace(0, 1, 5)
print("\nLinspace:\n", linspace)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print("Addition:\n", c)

d = a - b
print("\nSubtraction:\n", d)

e = a * b
print("\nMultiplication:\n", e)

f = a / b
print("\nDivision:\n", f)

a = np.array([1, 2, 3])
sum_a = np.sum(a)
print("Sum of array elements:", sum_a)

mean_a = np.mean(a)
print("\nMean of array elements:", mean_a)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transpose = np.transpose(matrix)
print("\nTranspose of matrix:\n", transpose)

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr, (2, 3))
print("\nReshaped array:\n", reshaped_arr)

flattened_arr = reshaped_arr.flatten()
print("\nFlattened array:\n", flattened_arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print("\nDot product:", dot_product)

cross_product = np.cross(a, b)
print("\nCross product:", cross_product)

shelf_layout = np.array([['Cereals', 'Pasta', 'Rice', 'Beans'],
                      ['Coffee', 'Tea', 'Milk', 'Juice'],
                      ['Apple', 'Banana', 'Mango', 'Peach']])

milk_position = shelf_layout[1, 2]
print(milk_position)

beverages = np.array(['Coffee', 'Tea', 'Milk', 'Juice', 'Water'])
top_3_beverages = beverages[:3]
print(top_3_beverages)

second_shelf = shelf_layout[1, :]
print(second_shelf)

prices = np.array([1.5, 1.0, 0.5, 2.0, 0.7])
cheap_beverages = beverages[prices < 1.0]
print(cheap_beverages)

fruit_positions = shelf_layout[np.isin(shelf_layout, ['Apple', 'Banana', 'Mango', 'Peach'])]
print(fruit_positions)

selected_beverages = beverages[[0, -1]]
print(selected_beverages)

selected_items = [shelf_layout[0][0], shelf_layout[2][3]]
print(selected_items)

# Broadcasting
heights = np.array([170, 187, 175])
weights = np.array([72,83, 68])

heights_meters = heights / 100
bmi = weights / (heights_meters ** 2)
print(bmi)

arr = np.array([1, 2, 3])
scalar = 5
result = arr + scalar
print(result)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 * arr2
print(result)

# Math operations
array1 = np.array([5, 10, 15])
array2 = np.array([3, 7, 9])

result = np.add(array1, array2)
print(result)

array1 = np.array([20, 15, 10])
array2 = np.array([5, 7, 3])

result = np.subtract(array1, array2)
print(result)

array1 = np.array([2, 3, 1])
array2 = np.array([3, 3, 3])

result = np.multiply(array1, array2)
print(result)

array1 = np.array([10000, 12000, 8000])
array2 = np.array([90, 120, 60])

result = np.divide(array1, array2)
print(result)

array = np.array([1, 2, 3])
result = np.exp(array)
print(result)

array = np.array([30, 45, 60])
result = np.sin(np.radians(array))
print(result)

array1 = np.array([85, 90, 88])
array2 = np.array([0.5, 0.3, 0.2])

result = np.dot(array1, array2)
print(result)

# Linear Algebra
A = np.array([[2, 3], [5,-1]])
B = np.array([39, -1])

solution = np.linalg.solve(A, B)
print(solution)

company_a = np.array([[1000], [1200], [1100]])
company_b = np.array([[900], [950], [920]])

total_sales = np.add(company_a, company_b)
print("Total sales in each month:\n", total_sales)

sales_difference = np.subtract(company_a, company_b)
print("Sales difference in each month:\n", sales_difference)

A = np.array([[4, 1], [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)