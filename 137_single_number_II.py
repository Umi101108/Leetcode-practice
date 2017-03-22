"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return (sum(set(nums))*3 - sum(nums) )/2



nums = [1,1,3,1,2,3,3]
so = Solution()
print so.singleNumber(nums)

