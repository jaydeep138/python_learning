#from csv import reader
#with open("f11.csv",'r') as f:
#    p=reader(f)
#    next(p)
#    for i in p:
#        print(i)
from csv import DictReader
with open("f11.csv",'r') as f:
    p=DictReader(f,delimiter='|')
    for i in p:
        print(i['name'])
        print(i['email'])