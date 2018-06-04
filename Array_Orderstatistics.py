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


print maxdifflargeraftersmaller([2,3,10,6,4,8,1,11,5,55,75])


