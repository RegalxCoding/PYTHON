import re

def validate_url(url):
    pattern=r'^(http|https)://[a-zA-Z0-9.-]\.[a-zA-Z]{2,}(/.*)?$'

    if re.match(pattern,url):
        return True
    else:
        return False

url=input("enter url:")
if validate_url(url):
    print("valid url")
else:
    print("invalid url")