coffee_price = 2.5
tea_price = 2.5

are_prices_equal = coffee_price == tea_price
print(are_prices_equal)

iphone_color = "Black"
samsung_color = "White"

are_colors_different = iphone_color != samsung_color
print(are_colors_different)

NY_population = 8.4   # in millions
LA_population = 4     # in millions

is_LA_more_populous = NY_population < LA_population
print(is_LA_more_populous)

amazon_stock = 3300    # In USD
google_stock = 2800    # In USD

is_amazon_stock_higher = amazon_stock > google_stock
print(is_amazon_stock_higher)

max_seating_restaurant = 100
people_in_restaurant = 85

is_capacity_exceeded = people_in_restaurant <= max_seating_restaurant
print(is_capacity_exceeded)

weekly_gym_visits_goal = 4
actual_gym_visits = 4

did_meet_gym_goal = actual_gym_visits >= weekly_gym_visits_goal
print(did_meet_gym_goal)

car1_mileage = 28  # miles per gallon
car1_fuel_capacity = 12  # gallons
car2_mileage = 24  # miles per gallon
car2_fuel_capacity = 10  # gallons

is_car1_better = (car1_mileage > car2_mileage) and (car1_fuel_capacity > car2_fuel_capacity)
print(is_car1_better)

permit_granted = True
good_weather = True

can_hold_event = permit_granted and good_weather
print(can_hold_event)

park_available = True
beach_available = False

can_plan_picnic = park_available or beach_available
print(can_plan_picnic)

book_available = False

is_book_unavailable = not book_available
print(is_book_unavailable)

script_ready = True
director_confirmed = False
lead_actor_confirmed = True

can_proceed_with_project = script_ready and (director_confirmed or lead_actor_confirmed)
print(can_proceed_with_project)

store_name = "Magic Emporium"
sales = 30000
customer_rating = 4.5

if sales >= 40000:
    print(store_name + " is a top-selling store.")
elif sales >= 20000:
    print(store_name + " is a good-selling store.")
else:
    print(store_name + " needs to boost sales.")

store_name = "Magic Emporium"
sales = 23000
customer_rating = 4.7

if sales >= 20000 and customer_rating >= 4.5:
    print(store_name + " is a star performer.")
elif sales >= 10000 or customer_rating >= 4:
    print(store_name + " is a valuable asset.")
else:
    print(store_name + " needs to improve.")

store_name = "Magic Emporium"
sales = 30000
customer_rating = 4.1

if sales >= 20000:
    if customer_rating >= 4.5:
        print(store_name + " is a star performer.")
    else:
        print(store_name + " has good sales but needs to improve customer satisfaction.")
else:
    if customer_rating >= 4.5:
        print(store_name + " needs to improve sales but has excellent customer satisfaction.")
    else:
        print(store_name + " needs overall improvement.")

# more improved examples in conditionals
apple_sales = 807
samsung_sales = 780

# Using comparison operators to see who made more sales
result = apple_sales > samsung_sales
print(result)

company_revenue = 60
market_share = 15

# Use logical operators to determine if the company is a market leader
result = company_revenue >= 50 and market_share >= 10
print(result)

revenue = 72

# Using conditional statements to determine the company's industry rank
if revenue >= 80:
    rank = "Top 3"
elif revenue >= 60:
    rank = "Top 10"
else:
    rank = "Below Top 10"

print(rank)

employee_sales = 25
employee_projects_completed = 10

# Using logical operators to determine if the employee is eligible for the Employee of the Year award
result = employee_sales >= 20 or employee_projects_completed >= 15
print(result)

team1_tasks_completed = 1200
team1_total_tasks = 1500
team2_tasks_completed = 1000
team2_total_tasks = 1300

# Calculate task completion rates and use comparison operators to determine which team is more efficient
team1_task_completion_rate = team1_tasks_completed / team1_total_tasks
team2_task_completion_rate = team2_tasks_completed / team2_total_tasks

result = team1_task_completion_rate > team2_task_completion_rate
print(result)

campaign_reach = 25
campaign_engagement = 30

# Use conditional statements to determine the type of marketing campaign
if campaign_reach <= 18 and campaign_engagement <= 45:
    campaign_type = "Niche marketing campaign"
elif campaign_reach > 18 and campaign_engagement <= 45:
    campaign_type = "Mass marketing campaign"
else:
    campaign_type = "Viral marketing campaign"

print(campaign_type)

quarter1_revenue = 3
quarter2_revenue = 1

if quarter1_revenue > quarter2_revenue:
    difference = quarter1_revenue - quarter2_revenue
    print(f"Revenue in Quarter 1 was higher by {difference} units")
elif quarter2_revenue > quarter1_revenue:
    difference = quarter2_revenue - quarter1_revenue
    print(f"Revenue in Quarter 2 was higher by {difference} units")
else:
    print("Both quarters had equal revenue")

quarter1_revenue = 3
quarter2_revenue = 1

if quarter1_revenue > quarter2_revenue:
    difference = quarter1_revenue - quarter2_revenue
    print(f"Revenue in Quarter 1 was higher by {difference} units")
elif quarter2_revenue > quarter1_revenue:
    difference = quarter2_revenue - quarter1_revenue
    print(f"Revenue in Quarter 2 was higher by {difference} units")
else:
    print("Both quarters had equal revenue")

employee_a_sales = 10
employee_b_sales = 12
employee_c_sales = 8

if employee_a_sales > employee_b_sales and employee_a_sales > employee_c_sales:
    print("Employee A has the highest sales")
elif employee_b_sales > employee_a_sales and employee_b_sales > employee_c_sales:
    print("Employee B has the highest sales")
else:
    print("Employee C has the highest sales")

team_points = 10
qualification_points = 12

if team_points >= qualification_points:
    print("The team qualifies for the next round")
else:
    print("The team does not qualify for the next round")

annual_revenue = 8

if annual_revenue <= 8:
    print("The company is in Category A")
elif annual_revenue <= 16:
    print("The company is in Category B")
elif annual_revenue <= 24:
    print("The company is in Category C")
else:
    print("The company is in Category D")

# Here, we have a dictionary with employees and their respective sales.
# We iterate over each employee and use conditionals to evaluate their performance based on the number of units sold.
sales_data = {
    'Employee 1': 7,
    'Employee 2': 6,
    'Employee 3': 4,
}

for employee, units_sold in sales_data.items():
    if units_sold > 5:
        print(f"{employee} had an outstanding performance with {units_sold} units sold!")
    elif units_sold > 2:
        print(f"{employee} performed well with {units_sold} units sold.")
    else:
        print(f"{employee} could improve next quarter.")

for employee, units_sold in sales_data.items():
    print(f"{employee}: {units_sold}")

movie_ratings = {
    "The Lion King": "PG",
    "Scarface": "R",
    "Frozen": "PG",
    "The Godfather": "R",
    "Finding Nemo": "G",
}

your_age = 17

# Check if you can watch Scarface
if movie_ratings["Scarface"] == "R" and your_age < 17:
    print("Sorry, you can't watch Scarface.")
else:
    print("Enjoy watching Scarface!")

temperature = 25

# Check if it's a good day to go to the beach
if temperature > 30:
    print("It's a perfect day for the beach!")
elif temperature > 20 and temperature <= 30:
    print("It's a bit chilly for the beach.")
else:
    print("Maybe it's better to stay indoors.")

item_price = 150
coupon = "20OFF"

# Check how much you need to pay
if coupon == "20OFF":
    item_price -= item_price * 0.2
    print(f"Your discounted price is {int(item_price)}")
else:
    print(f"Sorry, your coupon is not valid.")

password = "pass1234"

# Check the strength of the password
if len(password) < 8 or password.isalnum() == False:
    print("Your password is weak.")
else:
    print("Your password is strong.")

x = 24
if x % 2 == 0:
    print(x, ' is even')
else:
   print(x, ' is odd' )

num = 34
if num >= 0:
     if num == 0:
         print("Zero")
     else: print("Positive number")
else:
   print("Negative number")

year = 2022
print('21th century') if year >= 2000 else print('not 21th century')