class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == '1':
                    count+=1
                    self.mark(grid,i,j)
        return count

    def mark(self,grid,i,j):
        '''
        :param grid: 传进来的棋盘
        :param i: 遍历的i坐标
        :param j: 遍历的j坐标
        :return:
        '''
        # teminator 设置一些直接跳过的情况
        # 当前虽然不可能出现越界，但是递归会把i和j进行更新，变为i和j的l邻域，这就麻烦了
        # 理解这种执行完再回过来的递归顺序很重要
        if i<0 or j<0 or i>=self.height or j>=self.width or grid[i][j]=='0':
            return None
        else:
            # process
            grid[i][j] = '0'
            self.mark(grid,i-1,j)
            self.mark(grid,i+1,j)
            self.mark(grid,i,j-1)
            self.mark(grid,i,j+1)

solu = Solution()
grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
print(solu.numIslands(grid))