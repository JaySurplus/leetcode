"""
	92. Reverse Linked List II

	Reverse a linked list from position m to n. Do it in-place and in one-pass.

	For example:
	Given 1->2->3->4->5->NULL, m = 2 and n = 4,

	return 1->4->3->2->5->NULL.

	Note:
	Given m, n satisfy the following condition:
	1 <= m <= n <= length of list.

	https://leetcode.com/problems/reverse-linked-list-ii/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        tempHead = ListNode(None)
        tempHead.next = head

        h1 = tempHead
   
        for  i in range( m-1):
        	h1 = h1.next        
        p = h1.next
        for i in range(n-m):
        	temp = h1.next
        	h1.next = p.next
        	p.next = p.next.next
        	h1.next.next = temp
        return tempHead.next



sol = Solution()
n1 = ListNode(1)
n11 = ListNode(1)
n2 = ListNode(2)
n22 = ListNode(2)
n3 = ListNode(3)
n33 = ListNode(3)
n4 = ListNode(4)
n44 = ListNode(4)
n5 = ListNode(5)
n55 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = sol.reverseBetween(n1,2,4)

while res:
	print res.val
	res = res.next