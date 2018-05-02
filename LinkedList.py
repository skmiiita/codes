
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
        #middle = self.getMiddle()
        #self.head = middle
        self.reverse_list()
        #print list_orig.data
        current  = self.head
        status = 0
        #print temp.data, current.next.data
        while temp.next is not None:

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

        while next.next is not None:
            current = current.next
            next = current.next
            #print next.data, current.data
        return current


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
    third = Node(1)
    llist.head.next = second;
    second.next = third;
    #llist.head = llist.head.next

    #llist.reverse_list()
    llist.printList()
    print llist.checkpallindromicstring()


