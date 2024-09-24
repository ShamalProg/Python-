# class Attribute/instance and static mothod

# class Student:
#     Collegenm="RDTC"             #class attribute
#     def __init__(self,sname,sid) :
#         self.sname=sname
#         self.sid=sid
# s1=Student('Shamal',58)
# s2=Student('Vaishnavi',57)

# print(s1.Collegenm)             #shared memory for college name from class

# s2.Cnm="SCSCOE"                 #call for only s2 object indivisual memory given for college name
# print(s2.Cnm)

#------------------------------------------------------------------

#class method and static method

# class Student:
#     Collegenm="RDTC"             #class attribute
#     def __init__(self,sname,sid) :
#         self.sname=sname
#         self.sid=sid
#     @classmethod
#     def changecname(vcname,newcname):         #
#         vcname=newcname

#     @staticmethod                             # this is the static method wher we can not define any variable
#     def show():
#         print("This is the Static method.")
# Student.changecname="OrangeIt"
# v=Student('vaishnavi',57)
# print(Student.changecname)
# v.show()


class stud:
    Address="Pune"
    def __init__(self, id, name) :
        self.id=id
        self.name=name

    @classmethod
    def changeadd(self,newadd):
        self=newadd
    @staticmethod
    def showadd():
        print("Student address is Mumbai")

s1=stud(1,"Vaishnavi")
s1.showadd()


# s1=stud(1,"Vaishnavi")
# s2=stud(2,"Shamal")
# s2.Addr="Bhor"
# print(f"Address from shared memory :{s1.Address}")   # access by attribute name
# print(f"Address from indivisual memory :{s2.Addr}")   # access by variable name
