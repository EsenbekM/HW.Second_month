
class Employes:     # created class "Employes"

    """This Class for conrol date of Employes salary"""
    
    emp_count = 0   # Created class attributes
    work_rate = 2
    
    def __init__(self, name, salary):    #created method .__init__() with atributes
        self.name = name 
        self.salary = salary
    
    def display_count():                #created Instance method statement
        pass
    
    def display_employee(self):         #created Instance method which will print name and salary
       print(f'name: {self.name}\nsalary:{self.salary}') 

    def change_name(self, new_name):        #created Instance method which will change name
        self.name = new_name

    def get_total_salary(self):         #created Instance method which will retern value of salary 
        return self.salary

E1 = Employes("Esen", 16000)        #created employee objects
E2 = Employes("Kolya", 12000)
E3 = Employes("Pavel", 24000)

E1.display_employee()           #printed name and salary of employes by using Instance method display_employee
E2.display_employee()
E3.display_employee()

E1.change_name('Nikita')        #change name of employ by using Instance method change_name

print("\nNew name: ")           
E1.display_employee()           #printed changed name