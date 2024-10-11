# HYBRID INHERITANCE EXAMPLE
# is the combination of more than one type of inheritance

# class Animal:
#     def speak(self):
#         print("Animal speaks")


# class Mammal(Animal):
#     def give_birth(self):
#         print("Mammal gives birth")


# class Bird(Animal):
#     def lay_eggs(self):
#         print("Bird lays eggs")


# class Platypus(Mammal, Bird):
#     pass


# platypus = Platypus()
# platypus.speak()        # Method from Animal class
# platypus.give_birth()   # Method from Mammal class
# platypus.lay_eggs() 

# HIERARCHICAL INHERITANCE

# more than one derived class can be inheritedb from the one base class

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return F"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# # Usage
# dog = Dog("Budd")
# cat = Cat("Whiskers")
# print(dog.speak())  
# print(cat.speak()) 

# MULTILEVEL INHERITANCE

# in this inheritance base class is inherited from the other derived class1 
# and the other derived class2 is inherited from the derived class1 

# class Base:
#     # Constructor to set Data
#     def __init__(self, name, roll, role):
#         self.name = name
#         self.roll = roll
#         self.role = role

# # Intermediate Class: Inherits the Base Class
# class Intermediate(Base):
#     # Constructor to set age
#     def __init__(self, age, name, roll, role):
#         super().__init__(name, roll, role)
#         self.age = age

# # Derived Class: Inherits the Intermediate Class
# class Derived(Intermediate):
#     # Method to Print Data
#     def __init__(self, age, name, roll, role):
#         super().__init__(age, name, roll, role)

#     def Print_Data(self):
#         print(F"The Name is : {self.name}")
#         print(F"The Age is : {self.age}")
#         print(F"The role is : {self.role}")
#         print(F"The Roll is : {self.roll}")

# # Creating Object of Base Class
# obj = Derived(21,"Lokesh Singh", 25,"Software Trainer")
# obj.Print_Data()

# MULTIPLE INHERITANCE

# in this example more than one base classes are inherited from the single derived class

class Addition:
    def add(self, x, y):
        return x + y

class Subtration:
    def sub(self, x, y):
        return x - y

class Multiplication:
    def multiply(self, x, y):
        return x * y

class Calculation(Addition, Subtration, Multiplication):
    def div(self, x, y):
        return x / y

# Create an instance of class Calculation.
cal = Calculation()

# Calling methods of parent classes as well as child class.
result1 = cal.add(20, 10)
result2 = cal.sub(40, 20)
result3 = cal.multiply(10, 30)
result4 = cal.div(20, 5)

print(result1)
print(result2)
print(result3)
print(result4)