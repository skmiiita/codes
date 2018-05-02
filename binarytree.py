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
if __name__=='__main__':
    root = node(5)
    root.right = node(7)
    root.left = node(8)
    root.left.left = node(9)
    root.left.left.right = node(10)
    root.left.left.left = node(11)
    root.right.left = node(3)
    arr = []
    obj = binaryTreeOps()
    obj.printroottoleafpaths_m(root,0)