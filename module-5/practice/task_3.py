logs = [("ivan", "day", 8), ("ivan", "night", 4), ("olga", "day", 6), ("petr", "night", 1), ("anna", "day", 4), ("anna", "day", 3)]

employee_shirt = {}
shift_hours = {}
shift_hours_12 = {}


for log in logs:
    if log[1] not in shift_hours_12:
        shift_hours_12[log[1]] = 0
    shift_hours_12[log[1]] += log[2]

    if log[1] not in shift_hours:
        shift_hours[log[1]] = 0
    shift_hours[log[1]] += log[2]

    if log[0] not in employee_shirt:
        employee_shirt[log[0]] = set()
    employee_shirt [log[0]].add(log[1])
for employee in employee_shirt:
    value = employee_shirt[employee]
    if len(value) == 2:
        print(employee)
print(employee_shirt)
#пункт 2
for shift in shift_hours:
    if shift_hours[shift] < 8:
        print(f"На смене {shift} отработали меньше 8 часов")

for shift in shift_hours_12:
    if shift_hours_12[shift] > 12:
        print(f"На смене {shift} отработали больше 12 часов")






