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

    def roottoleafpath(self,root,array):
        if root is None:
            return 0
        #self.array_p.append(root.data)
        array.append(root.data)
        if  (root.left is None and root.right is None):
            print(array)
            #self.array_p=[]
        self.roottoleafpath(root.left,array)
        self.roottoleafpath(root.right,array)

if __name__=='__main__':
    root = node(5)
    root.right = node(7)
    root.left = node(8)
    root.left.left = node(9)
    root.right.left = node(3)
    arr = []
    obj = binaryTreeOps()
    print obj.roottoleafpath(root,arr)