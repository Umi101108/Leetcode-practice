"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.
"""


class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		r = x
		while r*r > x:
			r = (x/r + r)/2
		return r

x = 5
so = Solution()
print so.mySqrt(x)