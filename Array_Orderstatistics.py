#https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
def maxsumnotwoadjacent(arr):
    n = len(arr)

    if n==1:
        return arr[0]
    if n==2:
        return (max(arr[0],arr[1]))

    inc = 0
    excl = 0

    for index in range(0,n):
        newinc = excl + arr[index]
        excl  = max(inc,excl)
        inc = newinc
    return max(inc,excl)


def maxdifflargeraftersmaller(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    if n == 2:
        if arr[1] > arr[0]:
            return arr[1]-arr[0]
        else:
            return -1
    maxdiff = 0
    minelement = arr[0]
    for i in range(0,n):
        diff = arr[i] - minelement
        if maxdiff < diff:
            maxdiff = diff
        if arr[i]<minelement:
            minelement = arr[i]
    return maxdiff


#print maxdifflargeraftersmaller([2,3,10,6,4,8,1,11,5,55,75])


"""
j-i max question 

LMIN and RMAX arrays are created. The basic approach is we have to find the leftmost element and rightmost element so that difference between them will be max.
"""

def windowswithsunsmallerthank(arr,k):
    end = 0
    sum = arr[0]
    start = 0
    ct = 0


    while(end < len(arr)):
        if sum <= k:
            end += 1
            ct +=end-start
            print end-start
            if end < len(arr):
                sum  = sum +arr[end]

        else:
            sum = sum - arr[start]
            start+=1
        #print start,end,sum
    return ct

#print windowswithsunsmallerthank([1],10)
print windowswithsunsmallerthank([1,11,2,3,15],10)

def flipzeroonebits(arr,k):
    start = 0
    end = 0
    index = 0
    n = len(arr)
    while index < n:
        if arr[index] == 1:
            end+=1
        elif arr[end] == 0:
            start = end
            end+=1
            if k>0:
                k=k-1

