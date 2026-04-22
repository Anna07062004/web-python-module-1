logs = [
    ("ivan", 8), ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

total_hours = {}

for employee, hours in logs:
    if employee in total_hours:
        total_hours[employee] += hours
    else:
        total_hours[employee] = hours

print("Суммарные часы по каждому сотруднику:")
for employee, total in total_hours.items():
    print(f"{employee}: {total} часов")

overtime_employees = {employee: hours for employee, hours in total_hours.items() if hours > 40}
print("\nСотрудники с переработкой (> 40 часов):")

if overtime_employees:
    for employee, hours in overtime_employees.items():
        print(f"{employee}: {hours} часов (переработка: {hours - 40} часов)")
else:
    print("Нет сотрудников с переработкой")

underwork_employees = {employee: hours for employee, hours in total_hours.items() if hours < 20}
print("\nСотрудники с недоработкой (< 20 часов):")
if underwork_employees:
    for employee, hours in underwork_employees.items():
        print(f"{employee}: {hours} часов (недоработка: {20 - hours} часов)")
else:
    print("Нет сотрудников с недоработкой")
