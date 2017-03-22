"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""
class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dic = {}
		for num in nums:
			dic[num] = dic.get(num, 0) + 1
		for k, v in dic.items():
			if v == 1:
				return k
		

nums = [1,2,4,6,6,4,2,5,1]
so = Solution()
print so.singleNumber(nums)