#def func(*args,reverse_str=False):
def func(*args,**kwargs):
    if  kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in args]
    else:
        return [i.title() for i in args]

print(func('jaydeep','mulani','abc','xyz',reverse_str=True))