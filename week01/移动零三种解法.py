class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        双指针,left始终指向下一个0，只赋值，必须考虑index=left=0的情况
        时间O(n) 空间O(1)
        """
        left = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[left] = nums[index]
                if index != left:
                    nums[index] = 0
                left += 1
        return nums

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        # 交换：无需考虑idx=zero_idx的情况
        # 时间O(n) 空间O(1) 
        """
        first_zero_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[first_zero_idx],nums[idx] = nums[idx],nums[first_zero_idx]
                first_zero_idx += 1
        return nums

    def moveZeroes3(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        # 新数组 时间O(n) 空间O(1)
        """
        b = []
        zero_count = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                zero_count += 1
            else:
                b.append(nums[index])
        for i in range(zero_count):
            b.append(0)
        return nums


solu = Solution()
print(solu.moveZeroes1([1,0,3,0,1]))