"""
	142. Linked List Cycle II

	Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

	Note: Do not modify the linked list.

	
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

       

        slow = head
        fast = head

        while fast and fast.next :
        	slow = slow.next	
        	fast = fast.next.next
        	if fast == slow:
        		start = head
        		while start != slow:
        			start = start.next
        			slow = slow.next
        		return start
        return None

      

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)

L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L2

sol = Solution()
print sol.detectCycle(L1).val