logs = [("ivan", "day", 8), ("ivan", "night", 4), ("olga", "day", 6), ("petr", "night", 1), ("anna", "day", 4), ("anna", "day", 3)]

employee_shirt = {}
shift_hours = {} 
employee_hours = {}

for name, shift, hours in logs:
    if name not in employee_shirt:
        employee_shirt[name] = set()
    employee_shirt[name].add(shift)

    if shift not in shift_hours:
        shift_hours[shift] = 0
    shift_hours[shift] += hours

    if name not in employee_hours:
        employee_hours[name] = 0
    employee_hours[name] += hours

multiple_shift = []

for employee in employee_hours:
    if len(employee_shirt[employee]) == 2:
        multiple_shift.append(employee)

shifts_less = []
for shift in shift_hours:
    if shift_hours[shift] < 8:
        shifts_less.append(shift)

employees = []

for employee in employee_hours:
    if employee_hours[employee] >= 12:
        employees.append(employee)