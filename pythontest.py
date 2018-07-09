import sys
import array
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
a=[1]

b = array.array('i',[5])
import collections
arr = [ 5,3, 3, 6, 6, 6, 5, 5, 8 ]
counter = collections.Counter(arr)
print counter
arr = sorted( arr, key=lambda x: (counter[x], x), reverse=True )
print arr