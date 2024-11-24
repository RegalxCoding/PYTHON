S=[]

def isempty(S):
    if len(S)==0:
        return True
    else:
        return False
    
def push(S,item):
    S.append(item)

def pop(S):
     top=len(S)-1
     del S[top]

def peek(S):
    top=len(S)-1
    print(S[top])

def show(S):
    if isempty(S):
        print("Sorry no items in stack")
    else:
        top=len(S)-1
        print(S[top],"<======TOP")
        top=top-1
        while(top>=0):
            print(S[top])
            top=top-1
     
top=None
while True:
    print("!!!STACK DEMONSTRATION!!!")
    print("1.PUSH\n")
    print("2.POP\n")
    print("3.PEEK\n")
    print("4.SHOW STACK\n")
    print("0.EXIT\n")

    ch=int(input("enter your choice:"))
    if ch==1:
        val=int(input("enter item to push in stack:\n"))
        push(S,val)
    elif ch==2:
        if isempty(S):
            print("Stack is empty")
        else:
            print("\ndeleted item was:",S[-1],end='')
            pop(S)
    elif ch==3:
        if isempty(S):
            print("empty")
        else:
           print("peek value is:",end=' ')
           peek(S)
    elif ch==4:
        show(S)
    elif ch==0:
        print("Bye")
        break
        