class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if root:
                res.append(root.val)
                for child in root.children:
                    helper(child) # 直接这样写即可
        helper(root)
        return res

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if root:
                for child in root.children:
                    helper(child)
                res.append(root.val)
        helper(root)
        return res