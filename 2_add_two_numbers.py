"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1:ListNode
        :type l2:ListNode
        :rtype: ListNode
        """
        # carry = 0
        # root = n = ListNode(0)
        # while l1 or l2 or carry:
        #     v1 = v2 = 0
        #     if l1:
        #         v1 = l1.val
        #         l1 = l1.next
        #     if l2:
        #         v2 = l2.val
        #         l2 = l2.next
        #     carry, val = divmod(v1+v2+carry, 10)
        #     n.next = ListNode(val)
        #     n = n.next
        # return root.

        carry = 0
        v_sum = 0
        rlist = []
        while l1 != [] or l2 != [] or carry != 0 :
            v1 = l1[0] if l1!=[] else 0
            v2 = l2[0] if l2!=[] else 0
            v_sum = v1 + v2 + carry
            num = v_sum % 10
            rlist.append(num)
            carry = v_sum / 10


            l1 = l1[1:]
            l2 = l2[1:]

        return rlist

    def addTwoNumbers2(self, l1, l2):
        carry = 0
        head = node = ListNode('#')
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            l_sum = val1 + val2 + carry
            node.next = ListNode(l_sum%10)
            carry = l_sum/10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next
        return head.next


# l1 = [1,5,8]
# l2 = [2,8,7,9]
# so = Solution()
# print so.addTwoNumbers(l1, l2)

l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(8)
l2 = ListNode(2)
l2.next = ListNode(8)
l2.next.next = ListNode(7)
l2.next.next.next = ListNode(2)
so = Solution()
result = so.addTwoNumbers2(l1, l2)
while result != None:
    print result.val
    result = result.next

