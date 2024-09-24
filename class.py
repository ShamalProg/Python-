# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Rahul",20)
# print(p1)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})" 
# p1=Person("Rahul",20) 
# print(p1)      

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfun(self):
#         print("my name is"+self.name )
# p1=Person("Rahul",30)
# p1.myfun()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# emp=Person("Rajesh",23)
# emp.display()

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#     def isemployee(self):
#         return False
# class Employee(Person):
#     def isemployee(self):
#         return True
# emp=Person("Rahul")
# print(emp.getname(),emp.isemployee)

class Student:
    _name=None
    _roll=None
    _branch=None
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def __disprollandbranch(self):
        print("Roll-No:",self._roll)
        print("Branch:",self._branch)
class College(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("Name:",self._name)
        self.__disprollandbranch()
stu=Student("Rahul",10,"Computer")
print(dir(stu))
print(stu._name)
stu.__disprollandbranch()
obj=College("Pooja",20,"Mechanical")
print("")
print(dir(obj))
obj.displayDetails()



