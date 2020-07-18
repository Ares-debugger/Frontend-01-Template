import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        实际上我要查找的是，a= trrget-b 故我只要判断a 在不在b: target-b 这个映射里
        """
        res = []
        tar_b_dic = {}
        for b in nums:
            tar_b_dic[b] = target - b
        for a in nums:
            if a in tar_b_dic.values():
                return [a,tar_b_dic[a]]
        return res

    def twoSum2(self, nums, target):
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target-nums[i]) is not None:
                return [hashset.get(target- nums[i]),i]
            hashset[nums[i]] = i


solu = Solution()
print(solu.twoSum([2,7,11,13],9))