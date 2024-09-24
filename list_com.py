# list comprehnsion

# defination
# list comprehmsion is a compact way to create a list using   

#-----------------------------------------------------
#

#-----------------------------------
# using map function
# newl1=list(map( lambda x: x**2,l1))
# print("using convention method")   
# print(newl1)
#-------------------------------------
# simple code
# newl1=[]
# for i in l1:
#     newl1.append(i**2)
# print("using convention method")   
# print(newl1)

# -----------------------------
# syntax--
#[(elements/expresion/format) for elements in iterable_reference if conditon]
# ex no 1:-
# to fiind out the squrare of of element in another list
# l1=[22,44,55,66,77,88]
# square =[x**2 for x in l1]
# print(square)
# -----------------------------------------
# Ex no 2
# to fiind out the even element 
# l1=[22,44,55,66,77,88,7,3]
# even = [x for x in l1 if x % 2 == 0]
# odd = [x for x in l1 if x % 2 != 0]
# print(f"even numbers are :{even}")
# print(f"odd numbers are :{odd}")


# # ex no 3: to find (x,x**2) list from given list
# squwithnum= [(x,x**2) for  x in l1]
# print(squwithnum)
#-------------------------------------------------
# ex no.4
# count the frequency
# l2=[22,44,55,66,77,88,7,3,5,7,88,44]
# frequency=[]
# for i in l2:
#     count=l2.count(i)
#     frequency.append((i,count))
# print(frequency)
# # print(set(frequency))

# freq=list(set([(x, l2.count(x)) for x in l2]))
# print(freq)
# ex 5
# words=["apple","banana","cherry","date","mango"]
# lenofwords=[(word,len(word)) for word in words]
# print(lenofwords)
# 3=-----------------------------

# ex 6
# find out lenght>
words=["apple","banana","cherry","date","mango"]
mylist=[word for word in words if len(word)>5]
print(mylist)