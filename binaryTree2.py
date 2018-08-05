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

def printfullnodes(root):
    if root is None:
        return
    if root.left and root.right:
        print root.data
    printfullnodes(root.left)
    printfullnodes(root.right)

def checksumtree(root):
    if root is None:
        return True
    if not root.left and not root.right:
        return root.data

    if checksumtree(root.left) and checksumtree(root.right) and root.data == root.left.data + root.right.data :
        return True
    return False

if __name__ == '__main__':
    root = node(26)
    root.right = node(3)
    root.left = node(10)
    root.left.left = node(4)
    #root.right.left = node(7)
    root.right.right = node(3)
    root.left.right = node(6)
    #print sumTreeP(root)
    #printInorder(root)
    print checksumtree(root)