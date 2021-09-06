# ЗАДАНИЕ:

# 1. Создать класс Employee. При инициализации класса (т.е. создании объекта) должны передаваться параметры:
#   name - Имя сотрудника
#   salary - Зарплата сотрудника.
#   Для этого нужен метод init

# 2. класс Employee будет иметь общие аттрибуты (для всех создаваемых объектов):
#   emp_count = 0
#   work_rate = 2

# 3. Внутри класса Employee создать метод display_count и установить в нем pass.

# 4. Внутри класса Employee создать метод display_employee, который будет печатать
#   'Моё Имя <здесь_должно_печататься Имя сотрудника>. Зарплата: <здесь_должно_печататься Зарплата сотрудника>'

# 5. Внутри класса Employee создать метод change_name, который будет менять имя у конкретного объекта.

# 6. Внутри класса Employee создать метод get_total_salary, которая будет возвращать значение из аттрибута salary

class Employes:

    emp_count = 0
    work_rate = 2

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def display_count():
        pass
    
    def display_employee(self):
       print(f'name: {self.name}\nsalary:{self.salary}') 

    def change_name(self, new_name):
        self.name = new_name

    def get_total_salary(self):
        return self.salary

E1 = Employes("Esen", 16000)
E2 = Employes("Kolya", 12000)
E3 = Employes("Pavel", 24000)

E1.display_employee()
E2.display_employee()
E3.display_employee()

E1.change_name('Nikita')

print("\nNew name: ")
E1.display_employee()