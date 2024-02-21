import os
print(os.getcwd())
#os.chdir(r'D:')#to changecurrent directory
#os.mkdir("movies")#to make new directoryin current folder if it is already available than it will give error 
#for checking that directory exist or not in folder see below line code
print(os.path.exists("movies")) #it will return true or false based on existance of file
#best way to create file or silmplest way without getting error and don't create duplicate files
#open('file3.txt','a').close()
#os.mkdir(r'D:\movie1')#to make directory in not current directory 
print(os.listdir(r"D:\Movie"))  #to get all present directory in current directory