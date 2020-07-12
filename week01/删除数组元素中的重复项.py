class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        快慢双指针解法，一旦前后不一致了，我就把后面的移动到前面来
        最后我只要输出nums[0:left+1]即可，也就是慢指针需要的地方
        """
        left = 0 # left始终指向最后一个重复的数字
        for right in range(1,len(nums)):
            if nums[right] != nums[left]: # 出现新值
                left += 1 # 先让left移动到要填充的地方
                nums[left] = nums[right] # 再把新值赋值过来
        return nums[0:left+1]

solu = Solution()
print(solu.removeDuplicates([0,1,1,1,2,2,2,3]))
