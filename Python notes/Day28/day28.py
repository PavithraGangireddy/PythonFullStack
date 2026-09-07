from abc import ABC, abstractmethod
class person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @abstractmethod
    def get_role(self):
        pass
    def get_basic_info(self):
        return f"name:{self.name}, age:{self.age}"
    def get_details(self):
        return f"{self.get_basic_info()}, role:{self.get_role()}"

# student class
class student(person):
    def __init__(self,name,age,sid,course):
        super().__init__(name,age)
        self._sid = sid
        self._course = course
    def get_role(self):
        return"student"
    def get_student_info(self):
        return f"{self.get_basic_info()}, sid:{self.sid}, course:{self.course}"
#
# professor class
class professor(person):
    def __init__(self,name,age,pid,department):
        super().__init__(name,age)
        self._pid = pid
        self._department = department
    def get_role(self):
        return "professor"
    def get_professor_info(self):
        return f"{self.get_basic_info()}, pid:{self.pid}, department:{self.department}"

#Adminstaff class
class adminstaff(person):
    def __init__(self,name,age,aid,designation):
        super().__init__(name,age)
        self._aid = aid
        self._designation = designation
    def get_role(self):
        return "adminstaff"
    def get_adminstaff_info(self):
        return f"{self.get_basic_info()}, aid:{self.aid}, designation:{self.designation}"
    

# university class
class university:
    university_name = "Codegnan university"
    def __init__(self):
        self.__people = []
    def add_people(self, person:person):
        self.__people.append(person)
    def display_people(self):
        if not self.__people:
            print("no one is registered")
        else:
            for p in self.__people:
                print(p.get_details())

    @classmethod
    def get_university_name(cls):
        return cls.university_name

    @staticmethod
    def welcome():
        print("welcome to university")
print(university.welcome())
print(university.get_university_name())

u= university()

while True:
    print("Main menu")
    print("press 1 for student registration")
    print("press 2 for professor registration")
    print("press 3 for adminstaff registration")
    print("press 4 for  to see registered people")
    print("press 5 for exist)")

    choice = input("enter your choice:")
    if choice == '1':
        name = input("enter student name:")
        age = int(input("enter student age:"))
        sid = input("enter student id:")
        course = input("enter student course:")
        s = student(name, age, sid, course)
        u.add_people(s)
        print("student registration successfully done")

    elif choice == '2':
        name = input("enter professor name:")
        age = int(input("enter professor age:"))
        pid = input("enter professor id:")
        department = input("enter professor department:")
        p = professor(name, age, pid, department)
        u.add_people(p)
        print("professor registration successfully done")

    elif choice == '3':
        name = input("enter adminstaff name:")
        age = int(input("enter admin age:"))
        aid = input("enter adminstaff id:")
        designation = input("enter adminstaff designation:")
        a = adminstaff(name, age, aid, designation)
        u.add_people(a)
        print("adminstaff registration successfully done")

    elif choice == '4':
        u.display_people()

    elif choice == '5':
        print("Thank you for visiting the university")

    else:
        print("invalid option try again")


    

    
