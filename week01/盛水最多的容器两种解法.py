class Solution(object):

    def _getArea(self,heights,left, right):
        return (right - left) * min(heights[left], heights[right])

    def maxArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        # 暴力破解，时间O(n^2),空间O(n)
        """

        max_A = 0
        for left in range(len(heights)):
            for right in range(left+1,len(heights)): # 保证不重复的技巧
                area = self._getArea(heights,left,right)
                max_A = max(max_A,area) # 要有个更新的步骤在里面
        return max_A

    def maxArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        # 双指针向中间收敛,每次移动小的
        """
        left = 0
        right = len(heights) - 1
        max_A = 0
        while(left < right):
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            area = self._getArea(heights,left,right)
            max_A = max(area,max_A)
        return max_A