#create a list of squares from 1 to 11
#normal method
#squares=[]
#for i in range(1,11):
#    squares.append(i**2)
#print(squares)


#squares=[i**2 for i in range(1,11)]
#print(squares)
#we can think it like that i**2 where i in range 1 to 11


#negative = [-i for i in range(1,11)]
#print(negative)

#names=['jaydeep','mulani','abc','xyz']
#make a new list that will assign only first character of the list values
#name=[name[0] for name in names]
#print(name)

#excercise for reverse the values(names) of th list using function with list comprehension

#def rev(l):
#    name1=[name[::-1] for name in l]
#    return name1

#names=['jaydeep','mulani','abc','xyz']
#print(rev(names))

#numbers=[ i for i in range(1,11) if i%2 == 0]
#print(numbers)

#numbers=[i for i in range(1,11) if i%2 != 0]
#print(numbers)

#--------------------------------------------excercise------------------------------------

# take a input from user in form of list and find numbers from them and store them into new list with coversion in string form integer
#def num_finder(l):
#    return [str(i) for i in l if (type(i)==int or type(i)==float)]

#list1=['jd','mj',1,2,2.4,'true',4.5,6,-5]
#print(num_finder(list1))

#--------------------------------------------finish----------------------------------------------

# if else list comprehension
#num=[i for i in range(1,11)]
#new_list=[-i if (i%2!=0) else i*2 for i in num]
#print(new_list)



# NESTED list comprehension
numbers = [[i for i in range(1,4)] for i in range(1,5)]
print(numbers)