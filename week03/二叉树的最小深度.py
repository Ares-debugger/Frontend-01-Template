class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root : return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        childDepth = min(leftDepth, rightDepth) if leftDepth and rightDepth else leftDepth or rightDepth
        return 1 + childDepth # 1表示的是根节点
        # 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 例如，[1,2]就是2，而不是1，因为到最近叶子节点的就是2个
