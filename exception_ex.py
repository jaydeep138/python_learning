def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except:
        print("unexpected error")

print(div(4,0))