while True:
    try:
        age=int(input("enter your age : "))
    except ValueError:
        print("may be you entered string instead of number , ....try again")
    except:
        print("unexpected error")
    else:
        print(f'you entered {age}')
        break
    finally:
        print("it is finally block.....")
if(age>18):
    print("you can play this game")
else:
    print("you can not play")