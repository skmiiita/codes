def finitenary(hash):

    for key, value in hash.iteritems():
        print key,value


# Java Program to find four different elements a,b,c and d of
# array such that a+b = c+d

# function to find a, b, c, d such that
# (a + b) = (c + d)
def findPairs(arr, n):
    # Create an empty hashmap to store mapping
    # from sum to pair indexes
    Hash = {}
    count = 0
    # Traverse through all possible pairs of arr[]
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            # Sum already present in hash
            if sum in Hash.keys() and sorted(Hash[sum]) != sorted((arr[i], arr[j])):
                # print previous pair and current
                prev = Hash.get(sum)
                print (str(prev) + " and (%d, %d)"
                       % (arr[i], arr[j]))
                count += 1

            else:
                # sum is not in hash
                # store it and continue to next pair
                Hash[sum] = (arr[i], arr[j])
    if count > 0:
        return True
    return False
#def checkoccurence(p1,p2):

def sortbyfrequency(arr):
    dict = {}
    dict_occur = {}
    for i in range(0,len(arr)):
        if arr[i] not in dict:
            dict[arr[i]] = 1
            dict_occur[arr[i]] = i
        else:
            dict[arr[i]] +=1
    print dict_occur
    arr = sorted(enumerate(arr), key=lambda value: (dict[value],dict_occur[value]),reverse=True)

    print arr

# driver program
arr = [3, 4, 7, 1, 2, 9, 8, 1, 2, 3]
# arr = [1,3,6,7]
arr.sort()
print arr
n = len(arr)
print findPairs(arr, n)

# This code is contributed by Aditi Sharma

if __name__ == '__main__':
    a  = {'c': 'g', 'b': 'c', 'g': 'd', 'd': 'b'}
    finitenary(a)