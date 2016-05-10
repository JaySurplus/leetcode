"""
    165. Compare Version Numbers

"""

import unittest

class Solution(object):
  def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split('.')
    v2 = version2.split('.')

    l1 = len(v1)
    l2 = len(v2)

    for i in range(max(l1,l2)):
        ver1 = int(v1[i]) if i < l1 else 0
        ver2 = int(v2[i]) if i < l2 else 0
        if ver1 < ver2:
            return -1
        elif ver1 > ver2:
            return 1
    return 0

class myTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        #self.sol.dispose()
        self.sol = None

    def test_case(self):
        self.assertEqual(self.sol.compareVersion("1","1") , 0)

    def test_caseII(self):
        self.assertEqual(self.sol.compareVersion("1.2","1.2.10") , -1)

if __name__ == "__main__":

    unittest.main()
