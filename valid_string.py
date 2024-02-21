class Jd:
    def __init__(self,str):
        self.str=str

    def isvalid(self):
        stack,pr=[],{'(':')','{':'}','[':']'}
        for i in self.str:
            if i in pr:
                stack.append(i)
            elif len(stack)==0 or pr[stack.pop()] != i:
                    return False
        return len(stack)==0

print(Jd("()()").isvalid())
print(Jd("(()[})").isvalid())
        