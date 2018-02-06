"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		r = []
		carry = 0
		a = map(lambda x: int(x), a)
		b = map(lambda x: int(x), b)
		print a, b
		while a!=[] or b!=[]:
			m = a.pop() if a!=[] else 0
			n = b.pop() if b!=[] else 0
			if m+n+carry == 3:
				r.append(1)
				carry = 1
			elif m+n+carry == 2:
				r.append(0)
				carry = 1
			elif m+n+carry == 1:
				r.append(1)
				carry = 0
			else:
				r.append(0)
				carry = 0
		r.append(1) if carry else r
		return  ''.join(map(lambda x: str(x), r[::-1]))


a = '11'
b = '1'
so = Solution()
print so.addBinary(a, b)
