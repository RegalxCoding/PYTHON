#dictonary 
# dict={'age':21, "class ":22}
# print(dict['age'])
# x=dict.keys()
# print(x)

student={'name':"Rushabh",'class':"FY MCA", 'elective':"WEB DEVELOPMENT"}
x=student.keys()
print(x)
#dict is mutable
#we can change values 
#update funciton

student.update({'elective':"JAVASCRIPT"})
print(student)

student['elective']="web dev"
print(student)

#delete the key and display the value
print(student.pop('class'))
print(student)