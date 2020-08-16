class Solution():
    def __init__(self,n):
        self.memo = [0 for i in range(n+1)]
        self.n = n
    def calFib(self,n):
        if n<=1:return n
        if self.memo[n] == 0: # 递归函数中的if，可以有效的剪枝
            self.memo[n] = self.calFib(n-1) + self.calFib(n-2)
        return self.memo[n]
    def calFib_1(self,n):
        if  n<=1 :return n
        a = [1 for i in range(n)]
        for i in range(2,n):
            a[i] = a[i-1]+a[i-2]
        return a[n-1]  # 45测试用例的时候超过
