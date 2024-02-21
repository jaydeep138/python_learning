#keyword arguements
#double star operator
# we can only pass key value pair in kwaargs
#def func(**kwargs):
#    for k,v in kwargs.items():
#        print(k,v)
#
#d={'name':'jaydeep','age':24,'l_name':'mulani'}
#func(**d)

def func(*args,**kwargs):
    print(args)
    print(kwargs)

func(1,2,3,4,name='jaydep',l_name='mulani')