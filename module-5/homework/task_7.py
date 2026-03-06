class Employee:
    def __init__(self, full_name, phone, email, position, office_number, skype):
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.position = position
        self.office_number = office_number
        self.skype = skype

    def __repr__(self):
        return f"{self.full_name} - {self.position}"

class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, employee):
        self.employees[emp_id] = employee
        print(f"Сотрудник {employee.full_name} добавлен.")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            removed_employee = self.employees.pop(emp_id)
            print(f"Сотрудник {removed_employee.full_name} удален.")
        else:
            print("Сотрудник не найден.")

    def find_employee(self, emp_id):
        if emp_id in self.employees:
            print(f"Найден сотрудник: {self.employees[emp_id]}")
        else:
            print("Сотрудник не найден.")

    def update_employee(self, emp_id, **kwargs):
        if emp_id in self.employees:
            for key, value in kwargs.items():
                if hasattr(self.employees[emp_id], key):
                    setattr(self.employees[emp_id], key, value)
            print(f"Данные сотрудника {self.employees[emp_id].full_name} обновлены.")
        else:
            print("Сотрудник не найден.")

def main():
    company = Company()

    emp1 = Employee("Иванов Иван Иванович", "654-321", "exp@.com", "Менеджер", "101", "ivan.ivanov")
    emp2 = Employee("Петров Петр Петрович", "123-456", "pe@.com", "Разработчик", "102", "petr.petrov")
    
    company.add_employee(1, emp1)
    company.add_employee(2, emp2)
    company.find_employee(1)
    company.update_employee(1, phone="231-215", position="Старший менеджер")
    company.remove_employee(2)

if __name__ == "__main__":
    main()