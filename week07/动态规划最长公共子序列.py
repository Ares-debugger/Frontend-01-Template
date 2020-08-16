
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        m,n = len(text1),len(text2)
        dp = [[0]*(n+1) for _ in range(1+m)]
        for i in range(1,m+1):
            for j in range(1,1+n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]

solu = Solution()
print(solu.longestCommonSubsequence('abcde','ace'))
