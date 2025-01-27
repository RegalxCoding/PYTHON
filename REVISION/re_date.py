import re

def  validate_date(date):

    pattern=r'^\d{2}/\d{2}/\d{4}$'

    if re.match(pattern,date):
        return True
    else:
        return False

date=input("enter date:")
if validate_date(date):
    print("valid date")
else:
    print("invlaid date")