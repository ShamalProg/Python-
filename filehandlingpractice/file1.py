filename="exception.txt"
with open(filename,"w") as fp:
    fp.write(''' Python is one of the most popular and widely used Programming Languages. 
             Python is an Object Oriented Programming language which means it has features like Inheritance, 
             Encapsulation, Polymorphism, and Abstraction
         . In this article, we are going to learn about Multilevel Inheritance in Python.
Pre-Requisite
Python Inheritance
Python Multilevel Inheritance
Multilevel Inheritance in Python is a type of Inheritance in which a class inherits from a class, 
which itself inherits from another class. It allows a class to inherit properties and methods from multiple parent classes, 
forming a hierarchy similar to a family tree. It consists of two main aspects:
Base class: This represents a broad concept.
Derived classes: These inherit from the base class and add specific traits.
                              ''')
def check():    
    with open(filename,"r")as fp:
        data=fp.read()
        print(data)

#     with open(filename,"a") as fp:
#         fp.write('''Example 1: Simple Multilevel Inheritance
# In this method, we have three different classes that is Base, Intermediate and derived, 
# and we have inherited the feature of Base to Intermediate and then
#  the feature of Intermediate to derived class.''')
    
# with open(filename,"r")as fp:
#     data=fp.read()
#     print(data)
check()