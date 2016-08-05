"""
   380 Insert Delete GetRandom O(1)
"""
import random
class RandomizedSet(object):
    def __init__(self):
        self.val_ind = {}
        self.ind_val = []

    def insert(self, val):
        if val in self.val_ind :
            return False
        else:
            l = len(self.val_ind)

            self.val_ind[val] = l
            if l < len(self.ind_val):
                self.ind_val[l] = val
            else:
                self.ind_val.append(val)
            return True

    def remove(self, val):
        if val not in self.val_ind:
            return False
        else:
            ind = self.val_ind[val]
            newVal = self.ind_val[len(self.val_ind)-1]

            self.val_ind[newVal] = ind
            self.ind_val[ind] = newVal

            del self.val_ind[val]

            return True

    def getRandom(self):
        return self.ind_val[random.randrange(len(self.val_ind))]
