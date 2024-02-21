#it is use when there is no number of fixed number for paasing a value to the function
# we can pass as much as arguements as we want
# simple example
#def total(*args):
#    total1=0
#    for i in args:
#        total1+=i
#    return total1

#print(total(1,2,3,4,5,6,7,8,9,10))


# *args with normal parameters
#def mul(*args,num=4):
#    multiply=1
#    for i in args:
#        multiply*=i
#    return num*multiply

#print(mul(2,3,4))

# args as arguement
# if we want to pass the ist to the args then apply 8 BEFORE the list passing to the function to unpack the data of list
# we can also pass the tuple with *

#def mul(*args):
#    multiply=1
#    for i in args:
#        multiply*=i
#    return multiply

#num=[1,2,3,4]
#print(mul(*num))

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"
num=[1,2,3,4,5]
print(to_power(2,*num))