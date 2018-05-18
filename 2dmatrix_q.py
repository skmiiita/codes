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
def rowwithmax1(arr,row,col):
     pass
if __name__ == '__main__':
    arr = [[0,0,1,1],[0,0,0,1],[1,1,1,1]]
    print find1sposition(arr[2],0,len(arr[2])-1)
    #transpose2dArray(arr,2,3)


