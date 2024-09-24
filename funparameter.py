# def add(a,b,c):     # fromal parameter
#     return a+b+c
# print(add(2,3,4))   # actual parameter


# def add(a,b,c=0):  # c=0 is declared as a default parameter/arguement
#     return a+b+c
# print(add(2,3))

# def add(a,b,c):
#     return a+b+c
# print(add(a=10,b=2,c=5))    # tareget parameters/values

# ------------args/arguement/declared using * and can be constructed as tuple

# def add(*digits):
#     print(digits)
#     sum=0
#     for i in digits:
#         sum=sum+i
#     print(sum)
# add(2,3,4,5,67,78)

#--------- kwargs declared using ** and can be constructed as dictionary

# def percentage(**marks):
#     total=0
#     for sub in marks:
#         total+=marks[sub]
#     print(f"total marks {total} outoff 600")
#     per=(total/600)*100
#     print(f"percentage :{round(per,2)}%")
# percentage(math=98,eng=80,science=87,physics=90,biology=89,chemistry=95)

#-------lambda function to reduce function code done in a one line

# def sqr(x):   # simple function without lambda
#     return x**2
# print(sqr(9))

#-------- same function using lambda function

# sqr=lambda x:x**2
# print(sqr(8))

#-------  check number is even or odd

# iseven=lambda x:f"{x} is even" if (x%2==0) else f"{x} is odd"
# print(iseven(8))

#-------- using simple function add

# def add(mylist):
#     return sum(mylist)
# print(add([1,2,3,4,5]))

#------- using lambda

# add=lambda mylist:sum(mylist)
# print(add([2,3,4]))