"""
	Merge K Sorted Lists

	Merge k sorted linked lists and return it as one sorted list.
	Analyze and describe its complexity.

	https://leetcode.com/problems/merge-k-sorted-lists/


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        hp =[]
        for LN in lists:
        	if LN :
        		heapq.heappush(hp,(LN.val , LN))
        if hp:
        	item = heapq.heappop(hp)
        	curr.next = item[1]
        	curr = curr.next

        while hp:
        	if item[1].next:
        		item = heapq.heappushpop(hp,(item[1].next.val , item[1].next))
        	else:
        		item = heapq.heappop(hp)
        	curr.next = item[1]
        	curr = curr.next

        return head.next



