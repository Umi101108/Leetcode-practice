"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 
"""

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		# if not nums:
		# 	return 0
		# new_length = len(nums)
		# for i in range(len(nums)):
		# 	if nums[i] == val:
		# 		new_length -= 1

		# return new_length

		start, end = 0, len(nums)-1
		while start <= end:
			if nums[start] == val:
				nums[start], nums[end], end = nums[end], nums[start], end-1
			else:
				start += 1

		print nums
		return start

nums = [1,2,2,3,5,6,5,2]
val = 2
so = Solution()
print so.removeElement(nums, val)