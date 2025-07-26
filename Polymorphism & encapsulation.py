#case 1
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat.My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print('I can Meow')
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog.My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print('I can Bark')
cat1=Cat('Lily',2.5)
dog1=Dog('Tommy',5)
for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()
#case 2
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('Selling Price:{}'.format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()
#Change the price
c.__maxprice=1000
c.sell()
#using setter function
c.setMaxPrice(1000)
c.sell()