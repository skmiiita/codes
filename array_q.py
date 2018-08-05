class array_ops:
    array = []

    def __init__(self, arr):
        self.array = arr

    def triplet_sum(self, sum):
        self.array = sorted(self.array)
        print (self.array)
        for i in range(0, len(self.array)):
            j = i + 1
            k = len(self.array) - 1
            while (j < k):
                if self.array[i] + self.array[j] + self.array[k] == sum:
                    print  (self.array[i], self.array[j], self.array[k])
                    break
                elif self.array[i] + self.array[j] + self.array[k] > sum:
                    k = k - 1
                elif self.array[i] + self.array[j] + self.array[k] < sum:
                    j = j + 1

        return 1

    def countrotationcount(self, low, high):

        # {15, 18, 2, 3, 6, 12}
        # {7, 9, 11, 12, 5}
        # {1,2,3,4,5}
        # {2,3,4,5,1}
        mid = low + (high - low) / 2
        if (high - low) == 0:
            return 0
        if (high - low) == 1:
            if self.array[high] < self.array[low]:
                return 1
            else:
                return 0

        if self.array[mid] < self.array[mid + 1] and self.array[mid] < self.array[mid - 1]:
            return mid

        elif self.array[mid + 1] > self.array[mid] < self.array[mid] < self.array[mid - 1]:
            self.countrotationcount(mid + 1, high)
        elif self.array[mid] < self.array[mid + 1] and self.array[mid] < self.array[mid - 1]:
            pass

    def sort10array(self, arr):
        i = 0
        while (arr[i] == 0):
            i += 1
        j = len(arr) - 1

        while (arr[j] == 1):
            j -= 1
        print i, j
        while (i < j):
            if arr[i] == 1:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

            elif arr[i] == 0:
                i += 1
            elif arr[j] == 1:
                j -= 1
        return arr
        '''
        i=0
        j=len(arr)-1
        b_arr = [0]*len(arr)
        for index in range(0,len(arr)):
            if arr[index]==0:
                b_arr
                i+=1
            elif arr[index] ==1:
                b_arr[j] = 1
                j-=1
        return b_arr

        '''


def checkarrayelementsconsecutive(arr):
    if len(arr) is 0:
        return 0
    max_e = max(arr)
    min_e = min(arr)
    if max_e - min_e + 1 != len(arr):
        return 0
    status = 0
    print 'm'
    for index in range(0, len(arr)):
        if arr[abs(arr[index]) - min_e] >= 0:
            arr[abs(arr[index]) - min_e] = -arr[abs(arr[index]) - min_e]
            status = 1
        elif arr[abs(arr[index]) - min_e] < 0:
            return 0
        print arr
    if status == 1 and max_e - min_e + 1 == len(arr):
        return 1


def checkarrayelementsconsecutivedup(arr):
    if len(arr) is 0:
        return 0
    max_e = max(arr)
    min_e = min(arr)

    status = 0
    count = 0
    print 'm'
    for index in range(0, len(arr)):
        if arr[abs(arr[index]) - min_e] >= 0:
            arr[abs(arr[index]) - min_e] = -arr[abs(arr[index]) - min_e]
            status = 1
            count += 1
        elif arr[abs(arr[index]) - min_e] < 0:
            continue
        print arr
    if status == 1 and max_e - min_e + 1 == count:
        return 1
    else:
        return 0


def majorityelement(self, arr):
    majorc = self.majoritycandidate(arr)
    count = 0
    for index in range(0, len(arr)):
        if arr[index] == arr[majorc]:
            count += 1
    if count >= len(arr) / 2:
        return 1
    else:
        return 0


def majoritycandidate(self, arr):
    majorind = 0
    count = 1

    for index in range(1, len(arr)):
        if arr[majorind] == arr[index]:
            count += 1

        else:
            count -= 1
        if count == 0:
            count = 1
            majorind = index

    return majorind


def majorityelementhashing(self, arr):
    dict = {}
    for index in range(0, len(arr)):
        if arr[index] not in dict:
            dict[arr[index]] = 1
        else:
            dict[arr[index]] += 1
    print dict

    for key, value in dict.iteritems():
        if value >= len(arr) / 2:
            return key
        else:
            continue
    return 0


def checkfirstindexsortedarray(arr, start, end, x):
    while (start <= end):
        mid = start + (end - start) / 2
        if mid == 0 or arr[mid - 1] < x and arr[mid] == x:
            return mid
        elif arr[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def checklastindexsortedarray(arr, start, end, x):
    while (start <= end):
        mid = start + (end - start) / 2
        if mid == end - 1 or arr[mid + 1] > x and arr[mid] == x:
            return mid
        elif arr[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def checkoneelementrepeating(arr, start, end):
    arr_len = len(arr)
    while (start <= end):
        mid = start + (end - start) / 2
        if (mid == 0 and arr[mid + 1] > arr[mid]) or (mid == end - 1 and arr[mid - 1] < arr[mid]):
            return arr[mid]
        if arr[mid + 1] > arr[mid] > arr[mid - 1]:
            return arr[mid]
        if arr_len %2 ==1 and arr[mid-1] == arr[mid] and arr[mid] < arr[mid+1] :
            start = mid+1
        elif arr_len %2==1 and arr[mid-1] < arr[mid] and arr[mid]==arr[mid+1]:
            end = mid-1
    return -1


def countRotations(arr, low, high):
    # This condition is needed to
    # handle the case when array
    # is not rotated at all
    if (high < low):
        return 0

    # If there is only one
    # element left
    if (high == low):
        return low

    # Find mid
    # (low + high)/2
    mid = low + (high - low) / 2;
    mid = int(mid)

    # Check if element (mid+1) is
    # minimum element. Consider
    # the cases like {3, 4, 5, 1, 2}
    if (mid < high and arr[mid + 1] < arr[mid]):
        return (mid + 1)

    # Check if mid itself is
    # minimum element mid > low means thetre should be mid-1 element
    if (mid > low and arr[mid] < arr[mid - 1]):
        return mid

    # Decide whether we need to go
    # to left half or right half
    if (arr[high] > arr[mid]):
        return countRotations(arr, low, mid - 1);

    return countRotations(arr, mid + 1, high)

def firstrepeating(arr):
    dict = {}
    firstrep = 10000000000
    for index in range(0, len(arr)):
        if arr[index] not in dict:
            dict[arr[index]] = index
        else:
            if dict[arr[index]] < firstrep:
                firstrep = dict[arr[index]]
    return arr[firstrep]

def findbitomicpoint(arr,start,end):
    while start<=end:
        mid = start + (end-start)/2
        if start == end:
            return start
        if end ==start+1 and arr[start]>arr[end]:
            return start
        elif end ==start+1 and arr[start]<arr[end]:
            return end
        if arr[mid]>arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
        elif arr[mid + 1] > arr[mid] > arr[mid - 1]:
            start = mid+1
        elif arr[mid - 1]>arr[mid] > arr[mid + 1]:
            end = mid-1
    return -1


def sort012(arr):
    low = 0
    high = len(arr)-1
    mid  = 0
    for index in range(mid,len(arr)):
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
        elif arr[mid] == 1:
            mid+=1
    return arr

def findminoperationto(arr):
    result = 0
    n = len(arr)
    while True:
        zerocount = 0
        for index in range(0,len(arr)):
            if arr[index]%2==1:
                break
            elif arr[index]==0:
                zerocount +=1
        if zerocount == len(arr):
            return result
        print index
        if index == len(arr)-1:
            arr = [x/2 for x in arr]
            result +=1
        for jindex in range(index,len(arr)):
            if arr[jindex]%2==1:
                arr[jindex] -=1
                result+=1
        print arr
def find3high2low(arr):
    m1 = m2=m3=arr[0]
    l1 = l2 =100000000000000000000
    for i in range(0,len(arr)):
        if arr[i]>m1:
            m3=m2
            m2 = m1
            m1 = arr[i]
        if m1>arr[i]>m2:
            m3=m2
            m2 = arr[i]
        if  m2>arr[i]>m3:
            m3 = arr[i]
        if l1>arr[i]:
            l2=l1
            l1 = arr[i]
        if l2>arr[i]>l1:
            l2 = arr[i]
    return m1,m2,m3,l1,l2


def nextsmallestlarge(arr):
    arr = list(arr)
    i = len(arr) - 1
    min = arr[len(arr) - 1]
    mini = len(arr) - 1
    while i >= 0:

        if min > arr[i]:
            min = arr[i]
            mini = i

        if arr[i - 1] < arr[i]:
            break
        i -= 1

    if i == 0:
        return -1
    j = i - 1
    print i, j
    arr[j], arr[mini] = arr[mini], arr[j]
    print arr
    arr = arr[:i] + arr[i:][::-1]


    print arr
    return "".join(arr)


from sets import Set


def findLongestConseqSubseq(arr, n):
    s = Set()
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)
    print s
    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting
        # element of a sequence
        if (arr[i] - 1) not in s:

            # Then check for next elements in the
            # sequence
            j = arr[i]
            while (j in s):
                j += 1

            # update  optimal length if this length
            # is more
            ans = max(ans, j - arr[i])
    return ans

def stockbuysell(arr):
    n = len(arr)
    i=1
    max = 0
    min = 0
    maxdiff = 0

    while i < n:
        #print "min= ",min
        if arr[i]>arr[min]:
            maxdiff = arr[i]  - arr[min]
        else:
            #min = i

            if maxdiff > 0:
                print min, i-1
            min = i
            i=i+1
            maxdiff = 0
            continue
        if i == n - 1 and maxdiff <= 0:
            print -1
        elif i==n-1 and maxdiff > 0:
            print min, i
        i+=1
def checkpairdivisiblebyk(arr,k):
    if len(arr)%2==1:
        return False
    count  = len(arr)/2
    dict = {}
    for i in range(0,len(arr)):
        rem = arr[i]%k
        if rem in dict:
            dict[rem]+=1
        else:
            dict[rem] = 1
    for key,value in dict.iteritems():
        if value %2 ==1:
            if k-value in dict:
                count-=1
                dict[value]-=1
                dict[k-value]-=1

def kthfrom2sortedarrayUtil(arr1,arr2,low1,high1,low2,high2,k):

    mid1 = low1 + (high1-low1)/2
    mid2 = low2 + (high2-low2)/2

    if mid1+mid2 == k:
        return min(arr1[mid1],arr2[mid2])
    elif mid1+mid2<k:
        if arr1[mid1] > arr2[mid2]:
            kthfrom2sortedarrayUtil(arr1,arr2,low1,mid1,mid2,high2,k)
        else:

            kthfrom2sortedarrayUtil(arr1, arr2, low1, mid1, mid2, high2, k)
    else:
        if arr1[mid1] > arr2[mid2]:
            kthfrom2sortedarrayUtil(arr1,arr2,low1,mid1,mid2,high2,k)
        else:

            kthfrom2sortedarrayUtil(arr1, arr2, low1, mid1, mid2, high2, k)

def findpivot(arr,low,high):
    #if high > 0  and arr[high] < arr[high-1]:
        #return high

    mid = low + (high-low)/2
    print low, mid, high
    if high < low:
        return -1
    if high==low:
        return low
    if mid > 0  and mid < high and arr[mid-1] > arr[mid] < arr[mid+1]:
        return mid
    elif arr[high] < arr[mid]:
        return findpivot(arr,mid+1,high)
    else:
        return findpivot(arr,low,mid-1)

def searchinsortedrotatedarray(arr,k,low,high):
    mid = low + (high-low)/2
    print "low      high       mid"
    print low,      high,        mid
    if arr[mid] == k:
        print "mm"
        return mid
    elif arr[low]<=arr[mid]:
        print "m1"
        if k >= arr[low] and k <arr[mid]:
            return searchinsortedrotatedarray(arr,k,low,mid-1)
        else:
            return searchinsortedrotatedarray(arr,k,mid+1,high)
    else:
        print "m2"
        if k > arr[mid] and k <=arr[high]:
            return searchinsortedrotatedarray(arr, k,mid+1, high)
        else:
            return searchinsortedrotatedarray(arr, k, low, mid - 1)

def findsumpairsortedrotated(arr,k,low,high):
    return


def findPivotg(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return findPivotg(arr, low, mid - 1)
    return findPivotg(arr, mid + 1, high)
# Driver function
if __name__ == '__main__':
    a = [100, 180, 260, 310, 40, 535, 695]
    b = [100,90,80,70,100,120]
    c = [100,90,80,60,50,40]
    d = [5,4,3,2,1]
    arr = [5,6,7,8,9,10,1,2,3]
    print findpivot(d,0,4)

