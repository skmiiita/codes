class node :
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class bst_operations:
    def insert(self,root,newnode):
        if root is None:
            root = newnode
        else:
            if root.data < newnode.data:
                if root.right is None:
                    root.right = newnode
                else:
                    self.insert(root.right,newnode)
            else:
                if root.left is None:
                    root.left = newnode
                else:
                    self.insert(root.left,newnode)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.right)
        print root.data
        self.inorder(root.left)
    def greatersumtreeutil(self,root,summ):

        return self.greatersumtreeutil(root.right,summ)
        root.data = summ[0]
        summ[0] = summ[0] + root.data
        #print "sum = ", summ
        return self.greatersumtreeutil(root.left,summ)
    def greatersumtree(self, root):
        summ = []
        print root.data
        self.greatersumtreeutil(root,summ)
        #self.inorder(root)

if __name__=='__main__':
    r = node(50)
    bst = bst_operations()
    bst.insert(r, node(30))
    bst.insert(r, node(20))
    bst.insert(r, node(40))
    bst.insert(r, node(70))
    bst.insert(r, node(60))
    bst.insert(r, node(80))
    #bst.inorder(r)
    #bst.greatersumtreeutil(r,0)
    bst.greatersumtree(r)

