"""
    170. Two Sum III - Data structure design

    Design and implement a TwoSum class. It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    For example,
        add(1); add(3); add(5);
        find(4) -> true
        find(7) -> false

"""

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.l = {}
        self.s = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.l:
            self.l[number] = 2
        else:
            self.l[number] = 1
        #print "Add",self.l

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if  value in self.s:
            return True

        for k in self.l:
            if value - k in self.l:
                if value - k == k and self.l[k] == 1:
                    continue
                self.s[value] = value - k
                return True
        return False



sol = TwoSum()
sol.add(1)
sol.add(1)

print sol.find(0)
print sol.find(1)
print sol.find(2)

sol.add(-1)
print sol.find(0)
print sol.find(1)
print sol.find(-2)
sol.add(-1)
print sol.find(-2)


