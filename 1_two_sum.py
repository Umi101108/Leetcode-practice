# coding:utf8
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j] :
                    return [i, j]

    def twoSum2(self, nums, target):
        if len(nums)<=1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target-nums[i]] = i


nums = [20, 18, 12, 14]
target = 26
so = Solution()
print so.twoSum2(nums, target)
