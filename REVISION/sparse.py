row=int(input("enter no. of rows:"))
col=int(input("enter no. of cols:"))

arr=[]

for i in range(row):
    row_element=[]
    for j in range(col):
        element=int(input(f"enter element ({i},{j}):"))
        row_element.append(element)
    arr.append(row_element)

#display matrix
print("\nMATRIX\n")
for i in range(row):
    for j in range(col):
        print(arr[i][j],end="\t")
    print()

nz,z=0,0
for i in range(row):
    for j in range(col):
        if arr[i][j]!=0:
            nz+=1
        else:
            z+=1

if nz>z:
    print("\n MATRIX IS NOT A SPARSE MATRIX\n")
else:
    sm=[]
    for i in range(row):
        for j in range(col):
            if arr[i][j]!=0:
                sm.append([i,j,arr[i][j]])

#display sparse matrix
for row in sm:
    print(row[0],row[1],row[2],sep="\t")

