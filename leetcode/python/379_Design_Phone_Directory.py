class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.numbers = [[0,maxNumbers-1]]
        self.assigned = {}
        self.released = {}


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.numbers:
            return -1

        res = self.numbers[0][0]
        self.assigned[res] = 0

        if res + 1 > self.numbers[0][1]:
            self.numbers.pop(0)
        else:
            self.numbers[0][0] += 1
        return res

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number not in self.assigned

    def release(self,number):


    def releaseII(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number not in self.assigned:
            return
        del self.assigned[number]
        if not self.numbers:
            self.numbers += [[number,number]]
        else:
            if number < self.numbers[0][0]:
                if number + 1 == self.numbers[0][0]:
                    self.numbers[0][0] = number
                else:
                    self.numbers = [[number,number]] + self.numbers
            elif number > self.numbers[-1][1]:
                if number - 1 == self.numbers[-1][1]:
                    self.numbers[-1][1] = number
                else:
                    self.numbers += [[number,number]]
            else:
                l, r = 0, len(self.numbers) - 1
                while l < r:
                    m = (l + r)/2
                    if self.numbers[m] < number and self.numbers[m+1] > number:
                        break
                    else:
                        if self.numbers[m+1] < number:
                            l = m
                        else:
                            r = m

                lp = self.numbers[:m+1]
                rp = self.numbers[m+1:]

                if number == lp[-1][1] + 1:
                    lp[-1][1] = number
                else:
                    lp += [[number,number]]

                if number == rp[0][0] - 1:
                    lp[-1][1] = rp[0][1]
                    rp = rp[1:]
                self.numbers = lp + rp
