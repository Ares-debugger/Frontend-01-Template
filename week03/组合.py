class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        一个经验吧，无非是要存储当前的cur，和一个结果res
        组合问题，当中的层数是多少，是k
        什么时候返回，当cur的长度达到k的时候就要返回整个cur
        """
        res = []
        def _dfs(start,n,k,cur,res):
            if len(cur)==k:
                res.append(cur[:])
                return None
            for i in range(start,n+1):
                cur.append(i)
                _dfs(i+1,n,k,cur,res) # 把cur和结果带到下一层去
                cur.pop() # 清理当前的cur变量
        _dfs(1,n,k,[],res)
        return res

solu = Solution()
print(solu.combine(4,2))