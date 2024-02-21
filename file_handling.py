f=open("jd.txt")
print(f.read())#readfile
print(f.tell())#to know cursor position
f.seek(0)#to set cursor at custom position
print(f.readline(),end='')#print single line at a time
print(f.readlines()) #read all lines in file but give all line in a single list and give this list as output with \n at end of every line 
print(f.name)#prints the name of file
print(f.closed)#returns true if your file is closed otherwise false is not closed
f.close()#to clode the file after use it because sometimes it is harmful for file during program if we do not close files
print(f.closed)
with open("jd.txt") as f:
    data=f.read()
    print(data)
