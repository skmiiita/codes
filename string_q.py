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

if __name__ == '__main__':
    obj = StringQ()
    obj.reverseword("this that who")





