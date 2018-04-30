import sys
import traceback
import random
import time
def search(arr,low,high,n) :
    """

    :rtype: int
    """
    try:
        while(low<=high):
            mid = low + int((high-low)/2)
            if n == arr[mid]:
                return mid
            elif n < arr[mid]:
                high = mid-1
            else:
                low = mid+1
    except Exception:
        print(traceback.format_exc())
        return 0

def searchsortedrotatedarray(arr,low,high,n):
        try:
                while(left<=right):
                    mid = low + int((high - low) / 2)
                    if arr[mid] == n:
                            return mid
                    elif arr[mid] > n and arr[low] > n:
                        low = mid+1
                    elif arr[mid] > n and arr[low] < n:
                        low = mid+1
                    elif arr[mid]<n:
                        
if __name__ == "__main__":
        a = random.sample(range(1, 10000001), 10000000)
        a.sort()
        #print (a)
        start_time = time.time()
        b = search(a,0,len(a)-1,100)
        print (b)
        print("--- %s seconds ---" % (time.time() - start_time))

