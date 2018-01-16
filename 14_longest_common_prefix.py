"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		def lcp(a, b):
			if len(a) > len(b):
				a, b = b, a
			for i in xrange(len(a)):
				if a[i] != b[i]:
					return a[:i]
			return a

		return reduce(lcp, strs) if strs else ""


strs = ['abs', 'abcdgrd', 'abcdefs']
so = Solution()
print so.longestCommonPrefix(strs)