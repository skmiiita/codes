"""
ASCII_SIZE = 256


def getMaxOccuringChar(str):
    count = [0] * ASCII_SIZE

    max = -1
    c = ''

    for i in str:
        count[ord(i)] += 1;
        if count[ord(i)] > max:
            max = count[ord(i)]
    print max


    for i in range(0, ASCII_SIZE):
        if count[i] != 0 and max == count[i]:
            print chr(i)


def swap(a,b):
    a=a^b
    b=b^a
    a=a^b

    print a,b

# Driver program to test the above function
str = "sample string"
print "Max occurring character is " + getMaxOccuringChar(str)

swap(5,7)
print ord('a')

print float('inf')
"""

raw_input("enter")
