class StringQ:

    def reverseword(self,str):
        if str is None:
            return str
        str = str[::-1]

        str = str.split()
        print str
        strr = [x[::-1] for x in str]
        print strr
        str = " ".join(strr)

        print str

def checkpara(a,b):
    if a is '[' and b is ']':
        return True
    elif a is '{' and b is '}':
        return True
    elif a is '(' and b is ')':
        return True
    return False
def parathensesischecker(string):
    if string is None:
        return -1
    stack = []
    status = True
    for x in string:
        if x is '[' or x is '{' or x is '(':
            stack.append(x)
        elif x is ']' or x is '}' or x is ')':
            top = stack.pop()
            if checkpara(top,x):
                status = status and True
            else:
                return False
    if status and not stack:
        return True
    return False
def reversestring(string,start=0,end=0):
    if end==0:
        end = len(string)-1
    output = ""
    while end >=start:
        output = output+str(string[end])
        end-=1

    return output

def reverseeachwordinstring(string):
    if string is None:
        return None
    start = None
    output = ""
    for index in range(0,len(string)):
        if string[index] ==" " and start is None:
            continue
        if string[index]==" ":
            start = index+1
        print start
        if string[index] and (string[index+1] == '\n' or string[index+1]==" "):
            output +=reversestring(string,start,index)
    print output

def firstnonrepeatingcharacter(string):
    if string is None:
        return None

if __name__ == '__main__':
    # print parathensesischecker('[()]{}{[()()]()]')
    a = "dfsd fsf wwww"
    a=reverseeachwordinstring(a)
    print a





