from csv import DictWriter
with open("f121.csv",'w',newline='') as f:
    f1=DictWriter(f,fieldnames=['name','lastname','age'])
    f1.writeheader()
    f1.writerow({'name':'jaydeep','lastname':'mulani','age':'20'})
    f1.writerow({'name':'abc','lastname':'xyz','age':'200'})
    f1.writerows([
        {'name':'a','lastname':'b','age':'23'},
        {'name':'c','lastname':'z','age':'34'}
    ])