# encapsulation
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
b = Bank(10000)
print(b.get_balance())

#public 
class Student:
    def __init__(self):
        self.name = "Pavithra"
s = Student()
print(s.name)

# protected
class Student:
    def __init__(self):
        self._marks = 90

s = Student()
print(s._marks)

#private
class Student:
    def __init__(self):
        self.__marks = 90
    def show(self):
        print(self.__marks)
s = Student()
s.show()

#getter&setter
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks
s = Student(80)
print(s.get_marks())
s.set_marks(90)
print(s.get_marks())