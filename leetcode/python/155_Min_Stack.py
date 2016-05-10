"""
    155. Min Stack

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        push(x) -- Push element x onto stack.
        pop() -- Removes the element on top of the stack.
        top() -- Get the top element.
        getMin() -- Retrieve the minimum element in the stack.

"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []
        self.tail = -1
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.tail == -1:
            self.min.append(x)

        else:
            if x <= self.min[-1]:
                self.min.append(x)

        if self.tail == self.length - 1:
            self.stack.append(x)
            self.length += 1
        else:
            self.stack[self.tail] = x
        self.tail += 1



    def pop(self):
        """
        :rtype: void
        """
        if self.tail >= 0:
            if self.stack[self.tail] == self.min[-1]:
                self.min.pop()
            self.tail -= 1
        if self.tail < self.length/2:
            self.length /= 2
            self.stack = self.stack[:self.length]



    def top(self):
        """
        :rtype: int
        """
        if self.tail == -1:
            return None
        return self.stack[self.tail]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        return None

sol = MinStack()
for i in range(10,-1,-1):
    sol.push(i)


print sol.getMin()
print sol.stack
sol.pop()
print sol.getMin()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
#sol.pop()
#sol.pop()
#sol.pop()

print sol.top()
print sol.stack
print sol.length
print sol.tail
