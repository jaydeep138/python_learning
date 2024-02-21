from csv import writer
with open("f12.csv",'w',newline='') as f:
    f1=writer(f,delimiter='|')
    f1.writerow(['namme','lastname'])
    f1.writerow(['jaydeep','mulani'])
    f1.writerow(['xyz','abc'])
    f1.writerows([['hi','hello'],['welocme','goa','singham']])