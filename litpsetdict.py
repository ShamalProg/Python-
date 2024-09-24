 #LIST QUESTIONS

# 1 write a program to create a list of integers and find the sum of its elements

# li=[1,20,43,20,10]
# print(li)
# print(sum(li))

# 2 create a program to remove all duplicates fro a list

# li1=[10,20,30,10,49,20]
# print("list with dulicate elements",li1)
# set1=set(li1)
# li3=list(set1)
# print("list after removing duplicate elemnts",li3)

# 3 write a program to reverse a list in python

# list=[10,30,23,45,3,5]
# print(list)
# print(list.reverse())
# print(list)

# 4 implement a function that finds the minimum and maximum elements in list

# minimum=[]
# maximum=[]
# list1=[10,20,30,3,4,5,60,89,90,6]
# print(min(list1))
# minimum.append(list1)
# print(max(list1))

# 5 create a program that checks if a list is sorted in ascending order

# list=[10,20,78,5,7]
# if(list==sorted(list)):
#     print("list is sorted in ascending order")
# # elif(list==sorted(list,reverse=True)):
# #     print("list is sorted in ascendig order")
# else:
#     print("list is in decending order")

# 6 write a python function to calculate the average of list of  numbers

# list=[20,10,4,50,30,6,2]
# print(sum(list)/len(list))
# def calc_average(list):
#     return sum(list)/len(list)
#     #list=[20,10,4,50,30,6,2]
# average=calc_average(list)
# print("the average of the list is",(average))

# 7 implement a program that mergs two sorted lists into a single list

# li1=[10,20,30,40]
# li2=[50,60,70,80]
# li3=li1+li2
# print(li3)

# 8 create a python program that finds the frequency of the given element in a list





# 9 write a function that returns the second largest element from the list

# list=[10,2,45,6,7]
# list.sort()
# print("Tge second largest element from the list is:",list[-2])

# 10 implement the program to shuffle the elements of list randomly

# import random
# list=[1,2,3,4,5]
# shuffle_list=sorted(list,key=lambda x:random.random())
# print("original list is :",list)
# print("Shuffled list is :",shuffle_list)

# TUPLE QUESTUIONS

# 1 write a python program to create a tuple of strings and sort them in aphabeticle order

# tuple1=("Computer","E and TC","Mechanical","Civil","Artificial intelligence","Data Science")
# t1 = list(tuple1)
# print(t1)

# 2 create a program that concatenates two tuples

# names=("Pooja","Radhik","Sanika","Sonam")
# sirname=("Mane","Gade","Bathe","Doke")
# print(names+sirname)

# 3 write a function that checks if an element exists in a tuple

# names=("Pooja","Sonam","Radha","Rani")
# def check_element_in(names):
#     names1=input("Enter a string you want to find")
#     if(names1 in names):
#          print("the string %s exists in a tuple names"%(names1))
#     else:
#          print("the string %s does not exists in a tuple names"%(names1))
# checked_string=check_element_in(names)/

# 4 implment a program to find the index of the first occurance of the element in a tuple

# char=("a","b","c","d","a","m","c","f","d")
# index=char.index("m")
# print("index of m is:",index)

# 5 create tuple with mixed datatypes and calculate the sum of its numeric elements

# tuple(10,"Rani","Pooja",20,30,"Raha")



# 6 write a program to find the length of the tuple

# tuple=("Pooja",1,"Rani",20.7,"Rupa","Shanu")
# print("length of tuple is:",len(tuple))

# 7 implement a program that converts a tuple to a list

# tuple=(1,2,3,4,5,6)
# print("tuple before converting to list:",tuple)

# 8 write a puthon function that finds the product of all elements in a tuple

# import math
# tuple=(10,20,30,56,90)
# print("the product of tuple is:",math.prod(tuple))

# 9 create a program that slices a tuple to extract a specific portion of it

# tuple=(10,30,4,5,6,78,9,10)
# print(tuple[1:2])

# 10 write a function that checks if all elements of a tuple are same

# tuple=(1,2,3,"Java","Python","C")
# def check_for_similarity(tuple):

# DICTIONARY QUESTIONS

# 1 write a python program to create a dictionary of a students names and their scores

# student={"name":"Pooja","Score":100,}
# print(student)

# 2 create a program to check if a key exists in a dictionary

# dict={"name":"Pooja","roll":20,"address":"Pune","mobno":9087654332}
# print(dict)
# if dict.get("name"):
#     print("Name:",dict["name"])
# else:
#     print("name not found")
# if dict.get("age"):
#     print("age:",dict["age"])
# else:
#     print("age not found")

# 3 write a function that returns the keys of dictionary as a list

# dict={"name":"Pooja","adress":"pune","marks":20, "age":23}
# print(dict.keys())

# 4 implement a program to find a values associated with a specific key in a dictionary

# dict={"name":"rani","age":"29","address":"bhor","district":"satara"}
# print(dict)
# print(dict["name"])
# print(dict["age"])

# 5 write a python function that adds a new key value pair to a dictionary 

# dict={"name":"rani","age":"29","address":"bhor","district":"satara"}
# print("before adding a new key valuen pair:" ,dict)
# dict["tal"]="bhor"
# print("After adding a new key value pair:" ,dict)

# 6 create a dictionary of a words and their meanings and write a program to find the meaning of words

# word={
#     "words":{
#         "1":"Python",
#         "2":"apple",
#         "3":"car",
#         "4":"pooja",
#         "5":"cow"
#     },
#     "meanings":{
#         "1":"a programming language",
#         "2":"a fruit",
#         "3":"a vehical",
#         "4":"a persons name",
#         "5":"an animal"
# }
# }
# print(word)

# 7 implement a program that removes the key from the dictionary

# drinks={1:"coffee",2:"fruity",3:"tea",4:"sprite",5:"sting"}
# print(drinks)
# del(drinks[1])
# print(drinks)

# 8 write a function to find the highest value in a dictionary

# num={1:20,2:4,3:89,4:100,5:45}
# print(num)
# def highest(num):
#     max_value=max(zip(num.values(),num.keys()))
#     print(max_value)
# nums=highest(num)

# 9 create a program that counts the frequency of words in a given sentence using dictionary

# string=input("Enter any string")
# list=[]
# list=string.split()
# word_frequency=[list.count(p) for p in list]
# print("the frequency of the words is.....")
# print(dict(zip(list,word_frequency)))

# 10 write a python function to merge two dictionaries





# SET QUESTIONS

# 1 write a pyhton program to create a two sets and find their union

# set1={1,2,3,4,5}
# set2={6,7,8,2,3}
# print(set1.union(set2))
# unionset=set1 | set2
# print(unionset)

# 2 create a program to find the intersection of two sets

# set1={1,2,3,4,5}
# set2={6,7,1,2,3}
# print(set1.intersection(set2))
# intersectionset=set1 & set2
# print(intersectionset)

# 3 create a program to find the symetric difference between the two sets

# set1={1,2,3,4,5}
# set2={6,7,8,2,3,4,5}
# print(set1.difference(set2))
# differenceset=set1 - set2
# print(set2.difference(set1))
# differenceset=set2 - set1
# print(differenceset)

# 4 write a function that checks if one set is a subset of another set

# set1={1,2,3,4,5}
# set2={5,4,1,2,3}
# def checksubset(set1,set2):
#     if set1.issubset(set2):
#         print("Yes set1 is a subset of set2")
#     else:
#         print("set1 is not a subset of set2")
# fun=checksubset(set1,set2)

# 5 implement a program to remove duplicates from the list using a set

# list=[1,2,3,4,2,3,6,7]
# print(list)
# print(set(list))

# 6 write a python function to add the elements in a set

# set={1,2,3,4,5,6,7}
# print(set)
# def addelement(set):
#     add=int(input("do you want to add elements in a set"))
#     set.add(add)
#     print(set)
# setadd=addelement(set)
    
# 7 implement a program that cecks if two sets are disjoint
# returns true if both the set contain unique elements

# set1={1,2,3,4}
# set2={5,6,7}
# print(set1.isdisjoint(set2))

# 8 write a function  to find the maximum element in a set of numbers

# set1={1,35,67,89,100}
# def max1(set1):
#     print(max(set1))
# maximum=max1(set1)

# 9 create a program that removes a specific element from a set

# set1={1,2,3,4,5,6}
# print(set1)
# set1.remove(3)
# print(set1)

# 10 write a python function that checks if two sets are equal

# set1={1,2,3,4,5,"ajit"}
# set2={1,2,4,3,5,"ajit"}
# def equal(set1,set2):
#     print(set1==set2)
# callequal=equal(set1,set2)