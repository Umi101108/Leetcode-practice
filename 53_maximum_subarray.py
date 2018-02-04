"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		curSum = maxSum = nums[0]
		for num in nums[1:]:
			curSum = max(num, curSum+num)
			maxSum = max(curSum, maxSum)
		return maxSum


nums = [6, -3, 3, 8, -4, 1, -9, 5]
so = Solution()
print so.maxSubArray(nums)
