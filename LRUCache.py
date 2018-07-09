import collections

class LRUCache :

    cachesize = None  # type: int

    def __init__(self,cachesize):
        self.cachesize = cachesize
        self.dq = collections.deque(maxlen=self.cachesize)

    def bringtotop(self,process):
        for index in range(0,self.cachesize):
            if process == self.dq[index]:
                break
        element = self.dq[index]
        self.dq.remove(element)
        self.dq.appendleft(element)


    def cacheprocessing(self,processlist):

        for index in range(0,len(processlist)):
            if processlist[index] in self.dq:
                self.bringtotop(processlist[index])

            elif processlist not in self.dq :
                self.dq.appendleft(processlist[index])


if __name__ == '__main__':
    obj = LRUCache(3)

    obj.cacheprocessing([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5])
    print obj.dq