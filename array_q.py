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

    def countrotationcount(self,low,high):

        # {15, 18, 2, 3, 6, 12}
        # {7, 9, 11, 12, 5}
        # {1,2,3,4,5}
        # {2,3,4,5,1}
        mid = low + (high-low)/2
        if (high-low)==0 :
            return 0
        if (high-low) == 1:
            if self.array[high] < self.array[low]:
                return 1
            else:
                return 0

        if self.array[mid] < self.array[mid+1] and self.array[mid] < self.array[mid-1]:
            return mid

        elif self.array[mid] < self.array[mid+1] and self.array[mid] > self.array[0]:
            self.countrotationcount(mid+1,high)
        elif self.array[mid] < self.array[mid+1] and self.array[mid] < self.array[mid-1]:



if __name__ == '__main__':
    arr = [4,1,2,7,8,9,6]
    obj = array_ops(arr)
    print (obj.triplet_sum(18))

