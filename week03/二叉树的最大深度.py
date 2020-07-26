class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            # 动态更新左深度和右深度，然而在本层，又是固定的
            # 这就是当前层的逻辑，或者说很多时候，当前层的逻辑是被容纳进递归当中的
            # 例如这里，当前层的逻辑是“计算左右节点的深度并更新”，实际上这里是回溯更新的，而不是越来越小
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1 