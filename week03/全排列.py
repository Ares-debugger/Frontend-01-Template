class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        总共有n个格子，也就是n层，现在要做到的是选
        实际上这里的start就是代码模板中的level
        """
        res = []
        def _dfs(nums,size,depth,cur,used,res):
            '''
            :param nums: 传入的数组
            :param size: 最大层数
            :param depth: 当前遍历的深度
            :param cur: 当前的结果值
            :param used: 已经使用过的数字
            :param res: 返回的结果
            :return:
            '''
            if len(cur)==size:
                res.append(cur[:])
                return None

            for i in range(size):
                if used[i] == False:
                    # 把使用状态更新，然后增加元素
                    used[i] = True
                    cur.append(nums[i])
                    # 下探
                    _dfs(nums,size,depth+1,cur,used,res)
                    # 撤销所有状态，完成回溯
                    used[i] = False
                    cur.pop()

        size = len(nums)
        used = [False for _ in range(size)]
        _dfs(nums,size,0,[],used,res)
        return res