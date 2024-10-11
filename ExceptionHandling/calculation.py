# def multiply(a,b):
#     return a*b


def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:   # if we write as e to these line it will print the which type of error is this
        print("invalid input you enter 0")
    except TypeError:           # this the one type of eror  there are only one try block but have many except blocks
        print("invalid input you enter non digit number")

