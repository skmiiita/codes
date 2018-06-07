def tripletsumzero(arr):
    n = len(arr)
    if n<3:
        return None
    arr.sort()
    i=0
    j=1
    k=n-1
    while i<n:
        j=i+1
        while j<k and k>0:
            if arr[i]+arr[j]+arr[k] ==0:
                print arr[i], arr[j], arr[k]
                break
            elif arr[i]+arr[j]+arr[k] > 0:
                k = k-1
            else:
                j=j+1
        i+=1



tripletsumzero([1, -2, 1, 0, 5])
