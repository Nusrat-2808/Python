# #Project 1
# class fruit:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     #instance method
#     def intro(self):
#         print("Hello! I am ",self.name,". My color is ",self.color)
# #Object creation
# apple=fruit('Apple','Red')
# orange=fruit('Orange','Orange')
# guava=fruit('Guava','Green')
# #Calling object
# apple.intro()
# guava.intro()
# orange.intro()
# #Project 2
# class student:
#     grade=10
#     name='Sayeema'
#     def introduction(self):
#         print('Hi I am a student.')
#     def details(self):
#         print('My name is ',self.name)
#         print('I study in Grade',self.grade)
# ob=student()
# ob.introduction()
# ob.details()
class Parrot:
    #class attribute
    species='bird'
    #instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return '{} sings {}'.format(self.name,song)
    def dance(self):
        return '{} is now dancing.'.format(self.name)
#instantiate the Parrot class
rio=Parrot('Rio',2)
angel=Parrot('Angel',5)
#access the class attributes
print('Rio is a {}'.format(rio.species))
print('Angel is also a {}'.format(angel.species))
#access the instance attributes
print('{} is {} years old.'.format(rio.name,rio.age))
print('{} is {} years old.'.format(angel.name,angel.age))
print(rio.sing('Happy'))
print(angel.dance())