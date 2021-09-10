import datetime as dt # imported datatime and use for curent time

curent_year = dt.datetime.now()
curent_year = curent_year.year

class Person:   
    ''' Parent class person. '''
    __total_person = 0

    def __init__(self, __name, __birth_year, **kwargs):        
        self.name = __name
        self.birth_year = __birth_year
        Person.__total_person += 1
        self.language = kwargs.get("language")

        if __birth_year > curent_year:
            raise TypeError ("Write correct!")
    
    def is_abult(self):  # created metoth for check and get abult
        if curent_year - self.birth_year >= 18:
            return True
        return False

    def get_age(self): # created metoth get age
        return curent_year - self.birth_year

    @classmethod
    def get_total_person(cls): # created metoth for get total person
        return cls.__total_person

    def talk(self): # created metoth for print 'Hello world'
        print(f"{self.name} says Hello world!")
    
    def print_language(self): # created metoth for print person's language
        print(f"{self.name}'s language: {self.language}")


class Teacher(Person):
    ''' child class Teacher '''
    def talk(self): # created Polimorphism metoth
        print(f"Greetings, {self.name} your teacher")
    
    def teach(self): # created metod print for teachers
        print("Lesson started by Teacher")

# created Person's class objects 
p1 = Person('Esen', 2003, language = 'KG')
p2 = Person('Alex', 2000, language = "RU")
p3 = Person('Beka', 2004)

# created Teacher's class objects 
t1 = Teacher('Abai', 1990, language = 'ENG')
t2 = Teacher('Nurlan', 2000, language = 'TUR')
t3 = Teacher('Li', 1989, language = 'CHIN')

# get methods for objects

print(p1.get_age())
p1.talk()
p1.print_language()

print(p2.get_age())
p2.talk()
p2.print_language()

print(p3.get_age())
p3.talk()
p3.print_language()

print(t1.get_age())
t1.talk()
t1.print_language()

print(t2.get_age())
t2.talk()
t2.print_language()

print(t3.get_age())
t3.talk()
t3.print_language()

print(t3.get_total_person()) # print total person
