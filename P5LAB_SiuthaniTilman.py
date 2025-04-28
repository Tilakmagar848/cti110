# Tilman Siuthani
# 04/02/2025
# P5LAB - Self-Checkout Change Dispenser
# This program simulates a self-checkout machine that calculates change 
# and disperses it using dollars, quarters, dimes, nickels, and pennies.

import random

def make_change(change):
    """Calculate and display change in dollars, quarters, dimes, nickels, and pennies."""
    money = int(change * 100)  # Convert float to integer cents

    # Calculate the number of each coin
    num_dollars = money // 100
    money -= num_dollars * 100

    num_quarters = money // 25
    money -= num_quarters * 25

    num_dimes = money // 10
    money -= num_dimes * 10

    num_nickels = money // 5
    money -= num_nickels * 5

    num_pennies = money // 1
    money -= num_pennies * 1

    print("\nChange breakdown:")
    if change <= 0:
        print("No Change")
    else:
        if num_dollars > 0:
            print(f"{num_dollars} Dollar" if num_dollars == 1 else f"{num_dollars} Dollars")
        if num_quarters > 0:
            print(f"{num_quarters} Quarter" if num_quarters == 1 else f"{num_quarters} Quarters")
        if num_dimes > 0:
            print(f"{num_dimes} Dime" if num_dimes == 1 else f"{num_dimes} Dimes")
        if num_nickels > 0:
            print(f"{num_nickels} Nickel" if num_nickels == 1 else f"{num_nickels} Nickels")
        if num_pennies > 0:
            print(f"{num_pennies} Penny" if num_pennies == 1 else f"{num_pennies} Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    cash_in = float (input("Enter cash into machine: "))
    change = cash_in - amount_owed
    print(f"Your change is ${change:.2f}")
    make_change(change)

    while True:
        try:
            cash_in = float(input("How much cash will you put in the self-checkout? "))
            if cash_in < amount_owed:
                print("Insufficient funds. Please enter an amount greater than or equal to what you owe.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    change_owed = round(cash_in - amount_owed, 2)
    print(f"Change is: ${change_owed:.2f}")

    make_change(change_owed)

if __name__ == "__main__":
    main()