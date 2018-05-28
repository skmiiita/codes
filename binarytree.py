#import numpy as np
import queue_datastructure
from Queue import *
class node :
    def __init__(self,data):
        """

        :rtype: object
        """
        self.data = data
        self.right = None
        self.left = None

class binaryTreeOps:
    array_p = []
    def ischecksum(self,root):
        left_data = 0
        right_data = 0
        if root is None or (root.left is None and root.right is None):
            return 1
        if root.right is not None:
            right_data = root.right.data
        if root.left is not None:
            left_data = root.left.data

        if (right_data + left_data == root.data and self.ischecksum(root.left) and self.ischecksum(root.right)):
            return 1
        else:
            return 0
    def max_value(self,root):
        if root is None:
            return 0
        max = root.data
        right_max = self.max_value(root.right)
        left_max = self.max_value(root.left)
        if right_max > max:
            max = right_max
        if left_max > max:
            max = left_max
        return max

    def min_value(self,root):
        if root is None:
            return 0
        min = root.data
        right_min = self.min_value(root.right)
        left_min = self.min_value(root.left)
        if right_min < min:
            min = right_min
        elif left_min < min:
            min = left_min
        return min

    def roottoleafsumpath(self,root,sum):
        if root is None:
            return 0
        sumpath = sum - root.data
        self.array_p.append(root.data)
        if sumpath == 0 and (root.left is None and root.right is None):
            print(self.array_p)
            self.array_p=[]
            return 1
        return (self.roottoleafsumpath(root.left, sumpath) or self.roottoleafsumpath(root.right, sumpath))

    def printPaths(self,root):
        arr = []
        self.roottoleafpath(root,arr,0)

    def roottoleafpath(self,root,arr,pathlen):
        if root is None:
            return 0
        arr.insert(pathlen,root.data)
        pathlen = pathlen + 1
        if  (root.left is None and root.right is None):
            self.printPathsLine(arr,pathlen)
        self.roottoleafpath(root.left,arr,pathlen)
        self.roottoleafpath(root.right,arr,pathlen)
    def printPathsLine(self,arr,pathlen):
        for index in range(0,pathlen):
            print arr[index]
        print "\n"
    def printroottoleafpaths_m(self,root,pathlen):
        if root is None:
            return 0
        self.array_p.insert(pathlen,root.data)
        pathlen = pathlen + 1
        if(root.left is None and root.right is None):
            for index in range(0, pathlen):
                print self.array_p[index]
            print "\n"
        self.printroottoleafpaths_m(root.left, pathlen)
        self.printroottoleafpaths_m(root.right, pathlen)

    def treeHeight(self,root):
        if root is None:
            return 0
        lh = 1 + self.treeHeight(root.left)
        rh = 1+ self.treeHeight(root.right)

        return max(lh,rh)

    def treeDiameter(self,root):
        if root is None:
            return 0
        lh = self.treeHeight(root.left)
        rh = self.treeHeight(root.right)
        ld = self.treeDiameter(root.left)
        rd = self.treeDiameter(root.right)

        return max(1+lh+rh ,max(self.treeDiameter(root.left), self.treeDiameter(root.right)))

    def treeDiameter_n(self,root,height):
        if root is None:
            height = 0
            return 0

        ld  = 1 + self.treeDiameter_n(root.left, height+1)
        rd = 1 + self.treeDiameter_n(root.right,height+1)

        return max(height,max(ld,rd))

    def findAncestor(self,root,n,M):
        if root is None:
            return 0
        if root.data  == n:
            return True
        if self.findAncestor(root.left,n,M) or self.findAncestor(root.right,n,M):
            print root.data
            M[root.data][root.data]=1
            #print M
            return True

        return False

    def levelorderTraversal(self,root,Q,q):
        if root is None:
            return

        if Q.empty():
            Q.put(root)
            q.put(root.data)

        while True:
            if Q.empty():
                return root
            node = Q.get()
            print node.data
            if node.left:
                Q.put(node.left)
                q.put(node.left.data)
            if node.right:
                Q.put(node.right)
                q.put(node.right.data)


    def printRightView(self,root,Q):
        if root is None:
            return
        if Q.empty():
            Q.put(root)

        while Q.empty() is not None:
            node = Q.get()
            print node.data

            if node.right:
                Q.put(node.right)

    def printsidenodes(self, root,Q,L):
        if root is None:
            return

        if len(L)==0:
            L.append(root.left)
        while len(L) is not 0:
            node = L.pop()
            print node.data

            if node.left:
                L.append(node.left)
        if Q.empty():
            Q.put(root)

        while Q.empty() is not None:
            node = Q.get()
            print node.data

            if node.right:
                Q.put(node.right)

    def childsumnode(self,root,Q):
        if root is None:
            return
        leftdata = 0
        rightdata = 0


        if Q.empty():
            Q.put(root)

        while True:
            if Q.empty():
                return root
            node = Q.get()
            #print node.data
            if node.left:
                Q.put(node.left)
                leftdata = node.left.data
            if node.right:
                Q.put(node.right)
                rightdata = node.right.data
            node.data = node.data + leftdata + rightdata
            leftdata = 0
            rightdata = 0

    def sumtree(self,root):
        if root is None:
            return
        leftdata = 0
        rightdata = 0
        self.sumtree(root.left)
        self.sumtree(root.right)
        if root.left:
            leftdata  = root.left.data
        if root.right:
            rightdata = root.right.data
        root.data = root.data + leftdata+rightdata
        return root


    def zigzagtraversal(self,root,s1,s2):
        level = 0

        if root is None:
            return None
        if not s1 and not s2:
            s1.append(root)
            level = 1
        # find replacement for infinite while
        while True:
            if not s1 and not s2:
                return root
            if level == 1:
                while s1:
                    node = s1.pop()
                    print node.data
                    if node.left:
                        s2.append(node.left)
                    if node.right:
                        s2.append(node.right)
                level = 0
            elif level == 0:

                while s2:
                    node = s2.pop()
                    print node.data
                    if node.right:
                        s1.append(node.right)
                    if node.left:
                        s1.append(node.left)

                level = 1
        return root

    def findLCAPath(self,root,ll,n):
        if root is None:
            return None
        ll.append(root.data)
        if root.data == n:
            return True


        if (self.findLCAPath(root.left,ll,n) or self.findLCAPath(root.right,ll,n)):
            return True
        ll.pop()
        return False

    def findLCA(self,root,n1,n2):
        if root is None:
            return None
        lpath = []
        rpath = []
        isfound1 = self.findLCAPath(root,lpath,n1)
        isfound2 = self.findLCAPath(root,rpath,n2)
        if not isfound1 or not isfound2:
            return False
        i,j=0,0
        while i<len(lpath) and j<len(rpath):
            if lpath[i] != rpath[j]:
                return lpath[i-1]
            i+=1
            j+=1
    def findlevelofanode(self,root,k,level):
        if root is None:
            return False
        if root.data == k:
            return level

        return self.findlevelofanode(root.left,k,level+1) or self.findlevelofanode(root.right,k,level+1)



if __name__=='__main__':
    root = node(5)
    root.right = node(7)
    root.left = node(8)
    root.left.left = node(9)
    root.right.left = node(3)
    root.right.right = node(12)
    root.left.left.right = node(10)
    root.left.left.left = node(11)

    arr = []
    obj = binaryTreeOps()
    #obj.printroottoleafpaths_m(root,0)
    height = 0
    #print obj.treeDiameter_n(root,height)
    M = [[0] * 12 for i in range(12)]
    #obj.findAncestor(root,10,M)
    #print(np.matrix(M))
    Q = Queue()
    q = Queue()
    s1 = []
    s2= []
    #obj.levelorderTraversal(root,Q,q)
    #obj.printsidenodes(root,Q,L)

    #root  = obj.sumtree(root)
    #obj.zigzagtraversal(root, s1, s2)
    level = 1
    print obj.findlevelofanode(root,9,level)

    print obj.findLCA(root,3,12)


