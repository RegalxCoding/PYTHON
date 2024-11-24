#both the string size/length must be equal
#both the strings 
str1=input("enter string 1:")
str2=input("enter string 2:")
count=0
count1=0
found=0
nofound=0
print("String 1:",str1)
print("String 2:",str2)
for i in str1:
    count+=1
print("\nlength of string1:",count)
count1=0
for i in str2:
    count1+=1
print("\nlength of string 2:",count)

if count!=count1:
    print("string are of diff length, so they are not anagram")
else:
    str1_lst=list(str1)
    str2_lst=list(str2)

    for i in range(count-1):
        for j in range(count-i-1):
            if str1_lst[j]>str1_lst[j+1]:
                str1_lst[j],str1_lst[j+1]=str1_lst[j+1],str1_lst[j]
            if str2_lst[j]>str2_lst[j+1]:
                str2_lst[j],str2_lst[j+1]=str2_lst[j+1],str2_lst[j]

is_anagram=True
for i in range(count):
    if str1_lst[i]!=str2_lst[i]:
        is_anagram=False
        break

if is_anagram:
    print("The Strings are Anagrams")
else:
    print("String are not anagram")