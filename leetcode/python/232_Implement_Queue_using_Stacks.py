"""
	232. Implement Queue using Stacks

	Implement the following operations of a queue using stacks.

		push(x) -- Push element x to the back of queue.
		pop() -- Removes the element from in front of queue.
		peek() -- Get the front element.
		empty() -- Return whether the queue is empty.

	Notes:
	You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
	Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
	You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class LinkNode(object):
	def __init__(self, x):
		self.s1 = []
		self.s2 = []
		

class Queue(object):

    def __init__(self):

        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while self.s1:
        	self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
        	self.s1.append(self.s2.pop())
        
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
        	self.s1.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        res = self.s1.pop()
        self.s1.append(res)
        return res

    def empty(self):
        """
        :rtype: bool
        """
       	return len(self.s1) == 0

sol = Queue()
for i in range(10):
	sol.push(i)
print sol.empty()
print sol.s2
while not sol.empty():
	print sol.peek()
	sol.pop()
print sol.s1
print sol.s2
print sol.empty()
