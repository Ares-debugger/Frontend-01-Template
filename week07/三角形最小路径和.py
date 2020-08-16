class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle # 初始化好了不用加
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j],dp[i+1][j+1])
        print(dp[0][0])
        return dp[0][0]

solu = Solution()
print(solu.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))