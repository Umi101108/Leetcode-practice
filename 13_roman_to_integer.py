"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtypr: int
		"""
		roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
		result = 0
		for i in range(len(s)-1):
			if roman[s[i]] < roman[s[i+1]]:
				result -= roman[s[i]]
			else:
				result += roman[s[i]]

		return result + roman[s[-1]]


s = "DCXXI"
so = Solution()
print so.romanToInt(s)