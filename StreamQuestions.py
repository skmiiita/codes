def checkpallindromstring(string):
    left=""
    right=""
    i=0
    ispallindrom = 0
    oddchar=""
    while(i < len(string)):
        if i==0:
            left=left+string[i]
            ispallindrom = 1
        elif i==1:
            right = right + string[i]
            if string[0] == string[1]:
                ispallindrom = 1

        elif (i+1)%2==1:
            right = string[i]+right
            l = len(right)
            oddchar = right[l - 1]
            right = right[:l-1]

            if left==right:
                ispallindrom=1
        else:
             left = left + oddchar
             right = string[i]+right

             if left==right:
                 ispallindrom = 1
        #print left, right
        if ispallindrom:
            print "{} is pallindrome".format(string[:i+1])
        else:
            print "{} is not pallindrome".format(string[:i+1])

        i+=1
        ispallindrom = 0

checkpallindromstring("aabaacaabaa")



