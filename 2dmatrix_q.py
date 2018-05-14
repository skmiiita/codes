def transpose2dArray(arr,row,col):
    b_arr = [[0]*row for i in range(col)]

    for cindex in range(0,col):
        for rindex in range(0,row):
            b_arr[cindex][rindex] = arr[rindex][cindex]

    print(b_arr)

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6]]
    transpose2dArray(arr,2,3)


