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

        elif self.array[mid] < self.array[mid+1] and self.array[mid] > self.array[0] and self.array[mid] < self.array[mid-1]:
            self.countrotationcount(mid+1,high)
        elif self.array[mid] < self.array[mid+1] and self.array[mid] < self.array[mid-1]:
            pass


    def sort10array(self,arr):
        i = 0
        while(arr[i]==0):
            i+=1
        j = len(arr)-1

        while(arr[j]==1):
            j-=1
        print i,j
        while(i<j):
            if arr[i] == 1:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1

            elif arr[i]==0:
                i+=1
            elif arr[j] == 1:
                j-=1
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
    for index in range(0,len(arr)):
        if arr[abs(arr[index])-min_e]>=0:
            arr[abs(arr[index]) - min_e] = -arr[abs(arr[index])-min_e]
            status = 1
        elif arr[abs(arr[index])-min_e] < 0:
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
    for index in range(0,len(arr)):
        if arr[abs(arr[index])-min_e]>=0:
            arr[abs(arr[index]) - min_e] = -arr[abs(arr[index])-min_e]
            status = 1
            count +=1
        elif arr[abs(arr[index])-min_e] < 0:
            continue
        print arr
    if status == 1 and max_e - min_e + 1 == count:
        return 1
    else:
        return 0

    def majorityelement(self,arr):
        majorc = self.majoritycandidate(arr)
        count = 0
        for index in range(0,len(arr)):
            if arr[index] == arr[majorc]:
                count +=1
        if count >= len(arr)/2:
            return 1
        else:
            return 0
    def majoritycandidate(self,arr):
        majorind = 0
        count  = 1

        for index in range(1,len(arr)):
            if arr[majorind] == arr[index]:
                count += 1

            else:
                count -=1
            if count == 0:
                count = 1
                majorind = index

        return majorind
    def majorityelementhashing(self,arr):
        dict = {}
        for index in range(0,len(arr)):
            if arr[index] not in dict:
                dict[arr[index]]=1
            else:
                dict[arr[index]] += 1
        print dict

        for key,value in dict.iteritems():
            if value>=len(arr)/2:
                return key
            else:
                continue
        return 0


if __name__ == '__main__':
   a =  [5, 2, 3, 6,4, 4, 6, 6]
   print checkarrayelementsconsecutivedup(a)


