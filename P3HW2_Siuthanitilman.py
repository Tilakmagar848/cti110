# Tilman Siuthani
# 03/16/2025
# P3HW2
# Determine employee's regular pay, OT pay, and gross pay

# Get employee name from user
employee_name = input("Enter employee's name: ")

# Get hours worked from user
hours_worked = float(input("Enter number of hours worked: "))

# Get employee pay rate from user
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate values
if hours_worked > 40:
    ot_hours = hours_worked - 40
    ot_pay_rate = pay_rate * 1.5
    ot_pay = ot_hours * ot_pay_rate
    reg_hours = 40
    reg_pay = reg_hours * pay_rate
else:
    ot_hours = 0
    ot_pay_rate = 0
    ot_pay = 0
    reg_hours = hours_worked
    reg_pay = reg_hours * pay_rate

gross_pay = reg_pay + ot_pay

# Display output with formatted table
print("-" * 45)
print(f"Employee name:    {employee_name}")
print("-" * 45)
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-" * 90)
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{ot_hours:<15.1f}{ot_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:<15.2f}")