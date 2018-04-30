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
        self.inorder(root.left)
        print root.data
        self.inorder(root.right)


if __name__=='__main__':
    r = node(50)
    bst = bst_operations()
    bst.insert(r, node(30))
    bst.insert(r, node(20))
    bst.insert(r, node(40))
    bst.insert(r, node(70))
    bst.insert(r, node(60))
    bst.insert(r, node(80))

    bst.inorder(r)

