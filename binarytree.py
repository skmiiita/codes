class node :
    def __init__(self,data):
        """

        :rtype: object
        """
        self.data = data
        self.right = None
        self.left = None

class binaryTreeOps:

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
        elif left_max > max:
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
        if left_min < min:
            min = left_min
        return min
    def isbst(self,root):


if __name__=='__main__':
    root = node(15)
    root.right = node(7)
    root.left = node(8)
    root.right.left = node(7)
    obj = binaryTreeOps()
    #print (root.data)
    print (obj.min_value(root))