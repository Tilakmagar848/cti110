# Tilman Siuthani
# 02/26/2025
# P2HW1
# Travel Expenses


# Ask the user their budget
budget = float(input("Enter budget: $"))

# Ask user to enter travel destination
location = (input("Enter your travel destination: "))

# Ask user for amount they will spend on gas
travel = float(input("How much do you expect to pay for travel? $"))

# Ask user for amount they will spend on hotel/lodging
lodging = float(input("Approximately, how much will you need for lodging? $"))

# Ask user for amount they will spend on food
food = float(input("How much will you need for food? $"))

# Add expenses
expenses = travel + lodging + food

# Subtract expenses for budget
remaining_budget = budget - expenses

# Display travel expenses
remaining_budget = budget - expenses

print()
print("-----Travel Expensess-----")
print(f"{'Location: ':<20}  {location}")
print(f"{'Initial budget: ': <21} ${budget}")
print(f"{'Fuel: ': <21} ${travel}")
print(f"{'Accomodation: ': <21} ${lodging}")
print(f"{'Food: ': <21} ${food}") 

print("----------------------------------------")

print(f"{'Remaining Budget: ': <21} ${remaining_budget}")

