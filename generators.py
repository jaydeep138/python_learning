#l=[1,2,3]
#for i in l:
#    print(l)
#i=iter(l)
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
#for num in map(lambda a:a**2,l):
#    print(num)

#def num(a):
#    for i in range(1,a+1):
#        yield(i)

#number=num(10)
#for x in number:
#    print(x)

#for y in number:
#    print(y)

#___________________________excercise___________________________________

def num(a):
    for i in range(2,a+1,2):
            yield(i)
            # yield is used to create a generator the way it works is that it will return the value and then it will pause the function and then it will resume the function from the last value it returned it is used to save memory and time
            # it is used to create a sequence of values

numbers=num(10)
for i in numbers:
    print(i)