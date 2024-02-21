def digit_count(a):
    if a==0:
        return 0
    else:
      return 1+digit_count(int(a/10))

number=int(input("enter the number :"))
print(digit_count(number))