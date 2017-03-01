



class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtypr: int
		"""
		start = 0
		maxlength = 0
		usedChar = {}

		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxlength = max(maxlength, i - start + 1)
			usedChar[s[i]] = i

			# print start, maxlength
			# print usedChar
		return maxlength


s = 'tmmzuxt'
# s = 'abcabcbb'
so = Solution()
print so.lengthOfLongestSubstring(s)
