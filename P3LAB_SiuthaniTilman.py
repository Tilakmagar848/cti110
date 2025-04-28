# Tilman siuthani
# 03/03/2025
# P2LAB
# Use if/else statements to determine coin combintion

# Get a float from user and convert to integer
input_money = float(input("Enter the amount of money as a float: $"))
money = int(input_money * 100)
#print(money)

# Calculate number of whole dollars
num_dollars = money // 100 
#print(f"Num dollars: {num_dollars}")
# Remove the dollars from the amount of money
money = money - (num_dollars * 100)
#print(f"The remaining money is: {money}")


# calculate number of whole quarters
num_quarters = money // 25
#print(f"Num quarters: {num_quarters}")
# Remove the dollars from the amount of money
money = money - (num_quarters * 25)
#print(f"The remaining money is: {money}")


# calculate number of dimes
num_dimes = money // 10
#print(f"Num_dimes: {num_dimes}")
# Remove the dollars from the amount of money
money = money - (num_dimes * 10)
#print(f"The remaining money is: {money}")


# calculate number of nickles
num_nickles = money // 5
#print(f"Num_nickles: {num_nickles}")
# Remove the dollars from the amount of money
money = money - (num_nickles * 5)
#print(f"The remaining money is: {money}")


# calculate number of pennies
num_pennies = money // 1
#print(f"Num_pennies: {num_pennies}")
# Remove the dollars from the amount of money
money = money - (num_pennies * 1)
#print(f"The remaining money is: {money}")


# Display coins/dollars needed only if they are used
# Ensure all grammar is correct
print()
print()
print()

print(f"{input_money:.2f}")


#If no change is due, display "No Change"
if input_money  <=0.00:
    print("No Change")


# Display dollars
if num_dollars > 0:
    if num_dollars  == 1:
        print(f"{num_dollars} Dollar")
    else: 
        print(f"{num_dollars} Dollars")

# Display quarters
if num_quarters > 0:
    if num_quarters  == 1:
        print(f"{num_quarters} Quarter")
    else: 
        print(f"{num_quarters} Quarters")

# Display dimes
if num_dimes > 0:
    if num_dimes  == 1:
        print(f"{num_dimes} Dime")
    else: 
        print(f"{num_dimes} Dimes")

# Display nicles
if num_nickles > 0:
    if num_nickles  == 1:
        print(f"{num_nickles} Nickl")
    else: 
        print(f"{num_nickles} Nickles")

# Display penny
if num_pennies > 0:
    if num_pennies  == 1:
        print(f"{num_pennies} Penny")
    else: 
        print(f"{num_pennies} Pennies")








