#with open("jd1.txt",'r+') as f:
#    f.write("hello i am jaydeep i am your father \n")
#with open("f1.txt",'r') as rf:
#    with open("f2.txt",'w') as wf:
#        wf.write(rf.read())
with open("f1.txt",'r') as rf:
    with open("f2.txt",'a') as wf:
        for line in rf.readlines():
            name,age=line.split(",")
            
            wf.write(f"{name} is {age} years old")

