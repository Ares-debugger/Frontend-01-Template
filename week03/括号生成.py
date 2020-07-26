class Solution(object):

    def _generate(self,left,right,n,s):
        '''
        :param left: 当前左括号个数
        :param right: 当前右括号个数
        :param n: 配额
        :param s: 当前的状态
        :return:
        '''
        if left == n and right == n:
            self.res.append(s)

        # 对下一层可能的状态节点施加影响
        if left < n:
            self._generate(left+1,right,n,s+'(')  # 加左括号造成的状态节点影响
        if left > right:
            self._generate(left,right+1,n,s+')') # 加右括号带来的状态节点影响

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        抽象为：有2n个格子，每个格子可以放左括号或者右括号
        有多少种可能性；先不考虑合不合法的问题
        假如3个的话，就是6层深度的递归
        """
        # 这里写递归的初始条件
        self.res = []
        self._generate(0,0,n,'')
        return self.res

solu = Solution()
print(solu.generateParenthesis(3))