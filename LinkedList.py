
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    
    def __init__(self):
        self.head = None
    def reverse_list(self):
        prev= None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
    def recursive_reverse(self):
        if self.head is None:
            return
        first = self.head
        rest = self.head.next
        if rest is None:
            return

    def checkpallindromicstring(self):
        list_orig = self.head
        temp = list_orig
        self.reverse_list()
        current  = self.head
        status = 0
        while temp:
            if temp.data == current.data:
                status = 1
            else:
                return 0
            temp = temp.next
            current = current.next
        return status

    def getMiddle(self):
        if self.head is None:
            return
        current  = self.head
        next = self.head
        ct = 1
        while current.next and current.next.next:
            current = current.next.next
            next = next.next
            ct = ct+1
            #print current.data
            #print next.data
        #print ct
        return next

    def checkpallindromiclist(self):
        list_orig = self.head
        middle = self.getMiddle()
        self.head = middle.next
        self.reverse_list()
        temp = self.head
        status = 0
        while(temp):
            if temp.data == list_orig.data:
                status = 1
            else:
                return 0
            temp = temp.next
            list_orig = list_orig.next
        print "status : ",status
        return status

def reverseList(head):
    if head is None:
        return
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

def printList(head):
    temp = head
    while(temp):
        print temp.data
        temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(3)
    sixth = Node(2)
    seven = Node(1)
    llist.head.next = second;
    second.next = third;
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven
    #llist.head = llist.head.next
    nlist = LinkedList()
    nlist.head = Node(1)
    nlist.head.next = Node(1)
    nlist.head.next.next = Node(1)
    nlist.head.next.next.next = Node(1)
    nlist.head.next.next.next.next = Node(1)
    #llist.reverse_list()
    #llist.printList()
    #print nlist.checkpallindromicstring()
    #print(nlist.getMiddle().data)
    print nlist.checkpallindromiclist()


