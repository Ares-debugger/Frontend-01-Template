class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # 这里为什么是mid+1呢？这是因为下标的问题了，mid+1才是要找的那个数据的位置
        # 数据切分的时候，[:x]和[x:]为了方便，x指的是“数量”
        # 但是下标取出的时候，x仍然是-1的，从下标改为数量需要加1
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # 这里面mid+1：就不影响了，实际上，二者拼接起来，也就是[:mid+1]+[mid+1:]才是完整的[:]
        return root


    def inorder(self,root):
        res = [] # 定义helper函数完全是为了把res放在外面，否则就要用到递归第四步的清理变量了
        def helper(root):
            if not root:return None
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        return res

solu = Solution()
root = solu.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(solu.inorder(root))