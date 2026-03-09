#09.03.2026
#1
def devide(a, b):
    return a / b

# print(devide(10, 0))

#2
raw_values = ["10", "5", "abc", "3"]
numbers = []

for raw in raw_values:
    try:
        numbers.append(int(raw))
    except ValueError:
        print(f"не число {raw}")

# print(numbers)

#3
# def parse(a, b):
#     try:
#         x = int(a)
#         y = int(b)
#         return x / y
#     except ValueError:
#         return "Ошибка а или b не число"
#     except ZeroDivisionError:
#         return "Делить на ноль нельзя"
    
# print(parse("10", "2"))
# print(parse("10", "0"))
# print(parse("abc", "2"))

#4
# try:
#     date = {"name": "Alisa"}
#     print(date["email"])
# except KeyError as e:
#     print("Тип:", type(e).__name__)
#     print("Аргумент:", e.args)
#     print("Сообщение:", e)

#5
def set_discount(percent):
    if not 0 <= percent <= 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
    return f"Скидка установленна: {percent}"

# print(set_discount(20))
# print(set_discount(120))

#6
# def load_user(date, user_id):
#     try:
#         return date[user_id]
#     except KeyError:
#         print(f"Пользователь не найден: {user_id}")

# user = {1: "Alice"}
# try:
#     print(load_user(user, 2))
# except KeyError:
#     print("Ошибка")

#7
# class ConfigError(Exception):
#     pass
# def load_port(raw_port):
#     try:
#         return int(raw_port)
#     except ValueError as e:
#         raise ConfigError("После PORT должно быть целое число") from e

# try:
#     load_port("abc")
# except ConfigError as e:
#     print("Тип:", type(e).__name__)
#     print(type(e).__cause__)


#8
class EmployeeError(Exception):
    pass

class EmployeeNotFoundError(EmployeeError):
    messege2 = "Сотрудник не найден"
    pass

class SalaryValidationError(EmployeeError):
    pass

def find_employee(employees, emp_id):
    if emp_id not in employees:
        raise EmployeeNotFoundError(f"Сотрудник {emp_id} не найден")
    return employees[emp_id]

def validate_salary(value):
    if value < 0:
        raise SalaryValidationError ("ЗП не может быть отрицательным")
    
try:
    find_employee({}, 10)
except EmployeeNotFoundError as e:
    print(e.messege2)
except SalaryValidationError as e:
    print(e)

#9
def normalize_persent(x):
    assert isinstance(x, int), "должно быть числом"
    if not 0 <= x <= 100:
        raise ValueError("Процент должен быть от 0 до 100")

print(normalize_persent(25))
print(normalize_persent("abc"))