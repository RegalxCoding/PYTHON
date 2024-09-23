s1="MCA IS GOOD"
print(s1)
print(s1[2])
print(s1[7])
#slicing
#excluding 7 character
print(s1[0:7])
#negative slicing
print(s1[-1:])
print(s1[:5])

#dealing with alphastrophies
print("I am the best,'I can code well'")
#Raw string
print(r"My friend rohit is best")

#concating two string
str1="Rushabh"
str2=" Tak"
str3=str1+str2
print(str3)

str4=str3
print(str4)

#both are accesing same location
print(str4 is str3)

#length of string
print(len(str2))


str1+="student"
print(str1)