numbers=[1,2,3,4,5,6,7,8,9,10]
#def is_even(a):
#     return a % 2 == 0

#print(list(filter(is_even,numbers)))
#print(list(filter(lambda a : a%2==0,numbers)))

print([i for i in numbers if i%2==0])