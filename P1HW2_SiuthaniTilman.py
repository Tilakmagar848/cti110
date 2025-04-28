# Tilman Siuthani
# 02/12/2025
# P1HW2

print("This program calculate and displays travel expenses")

budget = float(input("Enter Budget: $"))

destination = input("Enter your travel destination: ")

fuel_cost = float (input("How much do you think you will spend on gas? $"))

accommodation_cost = float(input("Approximately, how much will you need for accomodation/hotel? $"))

food_cost = float(input("Last, how much do you need for food? $"))


# Calculate remaining balances 
remaining_balance = budget - (fuel_cost + accommodation_cost + food_cost)

# Display travel expenses summary

print ("\n------------Travel Expenses----------")
print (f"Location: {destination}")
print (f"Initial Budget: {budget}\n")

print (f"Fuel: {fuel_cost}")
print (f"Accommodation: {accommodation_cost}")
print (f"Food: {food_cost}\n")

print (f"Remaining Balance: {remaining_balance}")