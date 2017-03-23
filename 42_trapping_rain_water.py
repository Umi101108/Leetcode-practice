"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		max_left = left = 0
		max_right = right = len(height)-1
		trap = 0

		while left <= right:
			if height[left] <= height[right]:
				if height[left] > height[max_left]:
					max_left = left
				else:
					trap += height[max_left] - height[left]
				left += 1
			else:
				if height[right] > height[max_right]:
					max_right = right
				else:
					trap += height[max_right] - height[right]
				right -= 1



		return trap


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [1,0,0,0,1]
s = Solution()
print s.trap(height)