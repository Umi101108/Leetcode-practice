"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtypr: List[List[int]]
		"""
		distinct_nums = sorted(list(nums))
		if len(distinct_nums) < 3:
			return []
		result = []
		# for i in range(len(distinct_nums)-2):
		# 	for j in range(i+1, len(distinct_nums)-1):
		# 		if -(distinct_nums[i] + distinct_nums[j]) in distinct_nums[j+1:] and -(distinct_nums[i] + distinct_nums[j]) >= distinct_nums[j] :
		# 			add = [distinct_nums[i], distinct_nums[j], -(distinct_nums[i] + distinct_nums[j])]
		# 			if add not in result:
		# 				result.append(add)
		for i in range(len(distinct_nums)):
			for j in range(len(distinct_nums)-i):
				if - distinct_nums[-j] - distinct_nums[i] in distinct_nums[i+1:-j]:
					add = [distinct_nums[i], - distinct_nums[-j] - distinct_nums[i], distinct_nums[-j]]
					if add not in result:
						result.append(add)
		return result

# nums = [1, 4, -4, 6, 0, 3, 7, 1]
# nums = [0, 0 ,0]
# nums = [-2, 0, 0, 2, 2, 4]
nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, -2, -1] 

so = Solution()
print so.threeSum(nums)