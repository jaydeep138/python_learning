#we can create dictionaary in one line with key value pair
#square={1:1,2:4,3:9}
#how to create
#square={num:num**2 for num in range(1,11)}
#we can also use formated string method in this like
#square={f'square of {num} ':num**2 for num in range(1,11)}
#for loop for printing in new line
#for k,v in square.items():
#    print(f"{k}:{v}")

#for letter count in word
#name='jaydeep mulani'
#count_letter={char: name.count(char) for char in name}
#print(count_letter)



#dictionary comprehension with if else
#check even or odd number_____________
#numbers = {i : ('even' if i%2==0 else "odd") for i in range(1,11)}
#print(numbers)


# SET COMPREHENSION
#very less use in general life
#s={i for i in range(1,11)}
#print(s)

names=['jaydeep','mulani','abc','xyz','123']
s={name[0] for name in names}
print(s)