#name  = input("enter your name:")
#i = 0
#temp_var = ""
#while i<len(name) : 
#    if name[i] not in temp_var:
#        temp_var += name[i]
#        print(f"{name[i]} : {name.count(name[i])}")
#    i += 1

def counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count

name=input("entere the name : ")
print(counter(name))