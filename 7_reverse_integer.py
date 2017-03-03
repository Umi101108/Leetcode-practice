"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtypr: int
		"""
		strx = str(x)
		if strx[0] =='-':
			if int(strx[1:][::-1]) > 2147483647:
				return 0
			return int('-' + strx[1:][::-1])
		else:
			if int(strx[::-1]) > 2147483647:
				return 0
			return int(strx[::-1])

x = -2147483648
so = Solution()
print so.reverse(x)