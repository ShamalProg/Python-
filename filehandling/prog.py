# import re
# def checkmail():
#     mail=input("enter your mail")
#     pattern="([a-z\$%\d+]+@[a-z]+\.[a-z]+)"
#     data=re.findall(pattern,mail)
#     print(data)

def checkage():
    try:
        age=int(input("enter your age"))
        if age>=18:
            print("you are eligibale for vote")
        else:
           print("you are under age")
    except ValueError:
        print("you entered a alpha value")
    except UnicodeDecodeError:
        print("you entered a character")