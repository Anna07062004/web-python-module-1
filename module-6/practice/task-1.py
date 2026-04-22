payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]

balances = {}
operation_count = {}

for user, amount in payments:
    if user in balances:
        balances[user] += amount
    else:
        balances[user] = amount

    if user in operation_count:
        operation_count[user] += 1
    else:
        operation_count[user] = 1

print("Баланс по каждому пользователю:")
for user, balance in balances.items():
    print(f"{user}: {balance}")

negative_balance_users = [user for user, balance in balances.items() if balance < 0]
print("\nПользователи с отрицательным балансом:")
if negative_balance_users:
    for user in negative_balance_users:
        print(f"{user} (баланс: {balances[user]})")
else:
    print("Нет пользователей с отрицательным балансом")

more_than_2_operations = [user for user, count in operation_count.items() if count > 2]
print("\nПользователи с более чем 2 операциями:")
if more_than_2_operations:
    for user in more_than_2_operations:
        print(f"{user} ({operation_count[user]} операций)")
else:
    print("Нет пользователей с более чем 2 операциями")