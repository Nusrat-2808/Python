# #case 1
# #parent class 
# class Person(object):
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#     def display(self):
#         print(f'Your name: {self.name}')
#         print(f'Your ID number: {self.idnumber}')
# #child class
# class Employee(Person):
#     def __init__(self, name, idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         #Invoking the __init__ of the parent class
#         Person.__init__(self,name,idnumber)
# #creation of an objectvariable or an instance
# a=Employee('penguin',20210401,15000,'Intern')
# #calling a function of the class Person using its instance
# a.display()
# #case 2
# from abc import ABC,abstractmethod
# #create a base class
# class animal(ABC):
#     #abstract method
#     #should be implemented by all sub-classes
#     def move(self):
#         pass
# #sub classes
# class Human(animal):
#     def move(self):
#         print('Human can walk & run.')
# class Snake(animal):
#     def move(self):
#         print('Snake can crawl.')
# class Dog(animal):
#     def move(self):
#         print('Dog can bark.')
# class Lion(animal):
#     def move(self):
#         print('Lion can roar.')
# #driver code
# R=Human()
# R.move()
# K=Snake()
# K.move()
# D=Dog()
# D.move()
# L=Lion()
# L.move()
#case 3
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear=year
x=Student('Joey','King',2021)
x.printname()
print(x.graduationyear)