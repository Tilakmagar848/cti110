# Tilman Siuthani
# 03/26/2025
# P4HW2
# Calculate Employee Payroll Calculator with Overtime


# Initialize accumulators
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(40, hours_worked)
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Update accumulators
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display individual employee payroll information
    print(f"\nEmployee name: {employee_name}")
    print(("-" * 80))
    print(f"Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-" * 80)
    print(f"{hours_worked:<14.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<14.2f}${regular_pay:<12.2f}${gross_pay:<10.2f}")
    print("\n")

# Display final payroll summary
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")