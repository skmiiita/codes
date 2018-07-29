from Queue import *
class node :
    def __init__(self,data):
        """

        :rtype: object
        """
        self.data = data
        self.right = None
        self.left = None

def sumTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    lsum = sumTree(root.left)
    rsum = sumTree(root.right)

    sumt =  lsum + rsum
    if root.data != sumt:
        return False
    return  root.data

def sumTreeP(root):
    if root is None:
        return 0
    if root.left:
        ld = root.left.data
    if root.right:
        rd = root.right.data
    if rd + ld == root.data and sumTree(root.left) and sumTree(root.right):
        return 1
    else:
        return 0
def treeisperfect(self,root,Q):
        if root is None:
            return

        if Q.empty():
            Q.put(root)

        while not Q.empty():
            node = Q.get()
            print node.data
            if node.left:
                Q.put(node.left)
            if node.right:
                Q.put(node.right)

def kdistancefromleaf(root,k):
    if root is None:
        return 0
    if root.left is None and root.left is None:
        return 1


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print root.data
    printInorder(root.right)

if __name__ == '__main__':
    root = node(10)
    root.right = node(2)
    root.left = node(8)
    root.left.left = node(3)
    root.right.left = node(2)
    #root.right.right = node(5)
    root.left.right = node(50)
    #print sumTreeP(root)
    #printInorder(root)
    Q = Queue()