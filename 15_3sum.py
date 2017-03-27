"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtypr: List[List[int]]
		"""
		# distinct_nums = sorted(list(nums))
		# if len(distinct_nums) < 3:
		# 	return []
		# result = []
		# for i in range(len(distinct_nums)):
		# 	for j in range(len(distinct_nums)-i):
		# 		if - distinct_nums[-j] - distinct_nums[i] in distinct_nums[i+1:-j]:
		# 			add = [distinct_nums[i], - distinct_nums[-j] - distinct_nums[i], distinct_nums[-j]]
		# 			if add not in result:
		# 				result.append(add)
		# return result

		res = []
		nums.sort()
		for i in xrange(len(nums)-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, len(nums)-1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if s < 0:
					l += 1
				elif s > 0:
					r -= 1
				else:
					res.append((nums[i], nums[l], nums[r]))
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
		return res





# nums = [1, 4, -4, 6, 0, 3, 7, 1]
# nums = [0, 0 ,0]
# nums = [-2, 0, 0, 2, 2, 4]
nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, -2, -1] 

so = Solution()
print so.threeSum(nums)