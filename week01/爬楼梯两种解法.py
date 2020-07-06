import math
class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        # 每次保持三个变量即可
        """
        f1,f2,f3 = 1,2,3
        if n < 3:return n
        for i in range(3,n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        # 数学 斐波那契通项公式
        """
        return 1/math.sqrt(5) * (((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)