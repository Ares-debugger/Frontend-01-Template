class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        if root:
            queue.append(root)
        res = []
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue[0]
                queue.remove(node)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return [max(p) for p in res]