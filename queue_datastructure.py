import searchinsortedrotatedarray

class queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = capacity-1
        self.Queue = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size==0

    def isFull(self):
        return self.size==self.capacity

    def enQueue(self,data):
        if self.isFull():
            print "Queue Full"
            return 0
        self.rear = (self.rear+1) % self.capacity
        self.Queue[self.rear] = data
        self.size = self.size + 1

    def deQueue(self):
        if self.isEmpty():
            print "Queue Empty"
            return 0

        print "deQueued Element : ",self.Queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def searchInQueue(self,n):
        status = searchinsortedrotatedarray.search(self.Queue,self.front,self.rear,n)

        if status == -1:
            print "Element {} not found".format(n)
        else:
            print "Element {} found at position {}".format(n,status)
    def displayQueue(self):
        if self.isEmpty():
            print "Queue Empty"
            return 0
        for index in range(self.front, self.rear+1):
            print self.Queue[index]



if __name__ == '__main__':
    Q = queue(10)
    print Q.isEmpty()
    print Q.isFull()
    print Q.deQueue()
    Q.enQueue(5)
    Q.displayQueue()
    Q.searchInQueue(5)
    Q.deQueue()
    Q.displayQueue()