"""
	Merge Two Sorted Lists
	Merge two sorted linked lists and return it as a new list. 
	The new list should be made by splicing together the nodes of the first two lists.

	https://leetcode.com/problems/merge-two-sorted-lists/


	Easy way is to maintain a new linked list. This would require extra space.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #head_1 = ListNode("temp")
       # head_2
        
       	if not l1:
       		return l2

       	if not l2:
       		return l1

        if l1.val <= l2.val:
        	head_1 = l1
        	head_2 = l2
        else:
        	head_1 = l2
        	head_2 = l1

        head_result = head_1

        while head_1.next and head_2:
        	if head_1.next.val > head_2.val:

        		#Rewire
        		temp = head_2.next
        		head_2.next = None

        		temp_2 = head_2
        		temp_2.next = head_1.next
        		head_1.next = temp_2

        		head_1 = head_1.next
        		head_2 = temp

        	else:
        		head_1 = head_1.next

        if not head_1.next:
        	head_1.next = head_2

       

        return head_result