class Solution(object):
    def levelOrder_BFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
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
        return res

    def levelOrder_DFS(self, root):
        '''
        :param root:
        :return:
        深度优先记录level信息
        '''
        if not root:return
        res = []
        def dfs(index,root):
            if len(res) < index:
                # 遍历的层数大于当前的长度了
                res.append([])
            res[index-1].append(root.val)
            if root.left:
                dfs(index+1,root.left)
            if root.right:
                dfs(index+1,root.right)
        dfs(1,root)
        return res