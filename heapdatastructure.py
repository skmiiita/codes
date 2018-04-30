class heap_data :
    data_array = []

    def __init__(self, data):
            self.data_array = data

    def parent(self,index):
        return index/2

    def left(self,index):
        return 2*index+1
    def right(self,index):
        return 2*index+2

    def max_heapify(self,index):
        l = self.left(index)
        r = self.right(index)
        print (l,r)
        largest = index
        if l<=len(self.data_array) and self.data_array[index] < self.data_array[l]:
            largest = l
        else:
            largest = index

        if r<=len(self.data_array) and self.data_array[largest] < self.data_array[r]:
            largest = r
        print (largest)
        if largest != index:
            self.data_array[index], self.data_array[largest] = self.data_array[largest], self.data_array[index]
            self.max_heapify(largest)

    def buildHeap(self):

        length = len(self.data_array)
        print ("length= ",length)
        heapify_length = int (length/2)
        index = heapify_length
        while (index>0):
            self.max_heapify(index)
            index = index -1


if __name__ == '__main__':

    a = [4,5,2,3,1,7,8]
    obj = heap_data(a)

    #obj.max_heapify(1)
    obj.buildHeap()
    print (obj.data_array)