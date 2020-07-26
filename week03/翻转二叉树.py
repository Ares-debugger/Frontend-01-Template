class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        你已经打败了那个90%谷歌工程师都用的软件的开发者了
        递归就是深度优先的遍历方式，非常简单
        """
        # temerator: 如果节点已经遍历不到了
        if not root:
            return
        if root:
            # 交换左右节点
            root.left,root.right = root.right,root.left
            # drill down
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root # rtype

    def invertTree_stack(self,root):
        '''
        :param root:
        :return:
        队列对应的就是广度优先的搜索方式
        每次弹出的，都是待处理的值；动态更新的，也是待处理的值
        那么我要维护一个队列，每次让待处理的值弹出
        第一次肯定是弹出根节点，交换其左右节点
        好，如果当前节点的左子树不为空，放入队列等待
        当前节点的右子树不为空，放入队列等待
        这样实际上就是一个“广度的遍历”->放入了这一层所有待处理的点
        然后逐渐的pop出来即可
        '''
        if not root:return
        if root:
            queue = [root]
            while queue:
                temp = queue.pop(0)
                temp.left,temp.right = temp.right,temp.left
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            return root
