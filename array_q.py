class array_ops:
    array = []
    def __init__(self,arr):
        self.array = arr

    def triplet_sum(self,sum):
        self.array = sorted(self.array)
        print (self.array)
        for i in range(0,len(self.array)):
            j = i+1
            k = len(self.array) - 1
            while(j<k):
                if self.array[i]+self.array[j]+self.array[k] == sum:
                    print  (self.array[i],self.array[j],self.array[k])
                    break
                elif self.array[i]+self.array[j]+self.array[k]>sum:
                    k = k-1
                elif self.array[i]+self.array[j]+self.array[k]<sum:
                    j = j+1


        return 1


if __name__ == '__main__':
    arr = [4,1,2,7,8,9,6]
    obj = array_ops(arr)
    print (obj.triplet_sum(18))

