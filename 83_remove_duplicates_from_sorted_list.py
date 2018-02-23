"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		h = head
		while head!=None and head.next!=None:
			if head.next.val == head.val:
				head.next = head.next.next
			else:
				head = head.next
		return h



a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(1)
so = Solution()
so.deleteDuplicates(a)