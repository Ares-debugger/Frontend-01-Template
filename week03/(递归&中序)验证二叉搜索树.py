
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        设计一个递归函数，判断左右子树是不是在这个区间里面
        实际上也是不断变更这个状态参数
        应该是判断一个low和upper两个值
        """
        def helper(node,low=float('-inf'),upper=float('inf')):
            '''
            :param node: 当前节点
            :param low: 当前节点左右子树应该满足的最小值
            :param upper: 当前节点右子树应该满足的最大值
            :return:
            核心逻辑：每一个取出来的节点，都要在应有的范围之内，这就是处理当前层的逻辑
            下面，我只要对左右节点分别判断就行，交给计算机，不要去人肉！！
            自动的就把当前的节点认为是上下界就完事了
            '''
            if not node: return True
            if node:
                # process
                if node.val <= low or node.val >= upper:
                    return False
                # drill down
                if not helper(node.left,low,upper=node.val):
                    return False
                if not helper(node.right,low=node.val,upper=upper):
                    return False
                return True
        return helper(root)

    def isValidBST_inorder(self, root):
        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:return False
        return True


