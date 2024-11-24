class MYException(Exception):
    pass
def input_age():
    try:
        age=int(input("enter your age:"))
        
        if age<0:
            raise MYException("Age cannot be negative")
        else:
            print("your age is ",age)
    except MYException as e: #e is system generated object
        print(e)

input_age()

#deligation and containership
#pancard standards
#regular expessions
#one class contains instatnace of another class