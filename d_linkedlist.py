class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list_insert(self,data):
        node = Node(data)
        if self.head is None:
            #node = Node(data)
            self.head = node
            self.head.next = None
            self.head.prev = None
            #self.head.next = node
            return

        temp  = self.head
        while(temp.next is not None):
            temp = temp.next
        temp.next =node
        node.prev = temp

    def list_insert_front(self,data):
        node = Node(data)
        temp = self.head
        node.next = temp
        node.prev = None
        temp.next.prev = node
        self.head = node

    def print_list(self):
        temp = self.head
        while(temp is not None):
            print temp.data
            temp =temp.next

    def delete_front(self):
        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        del temp



if __name__ == '__main__':
        ll = LinkedList()
        ll.list_insert(5)
        ll.list_insert(6)
        ll.list_insert_front(4)
        ll.print_list()
        ll.delete_front()
        ll.print_list()
