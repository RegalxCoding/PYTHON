#generator generates a sequence of values.
#it always be iterable 
#generates iterable sequence of values
#yield returns the values

def greet():
    yield 'Hello'
    yield 'Sanji'
g=greet()
for i in g:
    print(i)


def m(x,y):
    while x<=y:
        yield x
        x+=1

x=m(5,10)
for i in x:
    print(i)

    #return statment always terminate the block
    #yield never terminate
    
def m():
    yield "Good morning"
    yield "Zoro"
g=m()
print(next(g))
print(next(g))