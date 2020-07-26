class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n,0,[])
        return self._generate_result(n) # 输出棋盘

    def DFS(self,n,row,cur_state):
        '''
        :param n:
        :param row:
        :param cur_state:
        :return:
        '''
        if row >= n:
            # 行，所有行都完事了话，打印出cur_state
            self.result.append(cur_state)
            return

        # 在当前所有层遍历所有列，遍历列的时候把皇后放上去
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                # go die
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            self.DFS(n,row+1,cur_state+[col])

            # 当前层对全局变量的影响全部去掉，remove
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self,n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.'*i + 'Q' + '.'*(n-i-1))
        return [board[i:i+n] for i in range(0,len(board),n)]

solu = Solution()
print(solu.solveNQueens(8))