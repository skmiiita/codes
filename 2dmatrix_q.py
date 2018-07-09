def transpose2dArray(arr,row,col):
    b_arr = [[0]*row for i in range(col)]

    for cindex in range(0,col):
        for rindex in range(0,row):
            b_arr[cindex][rindex] = arr[rindex][cindex]

    print(b_arr)

def find1sposition(arr,low,high):
    mid  = low +(high-low)/2
    if arr[0] == 1:
        return 0
    if mid > 0 and arr[mid] == 1 and arr[mid-1] == 0:
        return mid
    elif arr[mid] == 0:
        return find1sposition(arr,mid+1,high)
    else:
        return find1sposition(arr,0,mid-1)
    return -1
'''
def rowwithmax1(arr,row,col):
     pass
def booleanmatrix(arr,m,n):
    colflag = 0
    rowflag = 0
    for i in range(0,m):
        if arr[0][i]==1:
            rowflag=1
            break
    for i in range(0,n):
        if arr[i][0]==1:
            colflag = 1
            break
    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j] ==1:
                arr[0][j]=1
                break

'''

def printspiral(arr,m,n):
    k=0
    l=0
    i=j=0

    while k<m and l < n:
        for i in range(l,n):
            print arr[k][i]
        k+=1
        for i in range(k,m):
            print arr[i][n-1]
        n=n-1
        i=n-1
        if k<m:
            while(i>=l):
                print arr[m-1][i]
                i-=1
        m=m-1
        i=m-1
        if l<n:
            while (i>=k):
                print arr[i][l]
                i-=1
        l+=1

if __name__ == '__main__':
    arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    printspiral(arr,5,5)
    #transpose2dArray


