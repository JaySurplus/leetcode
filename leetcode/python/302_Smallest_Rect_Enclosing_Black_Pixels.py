"""
    302. Smallest Rectangle Enclosing Black Pixels

    An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

    For example, given the following image:

        [
          "0010",
          "0110",
          "0100"
        ]
    and x = 0, y = 2,
    Return 6.
"""

class Solution():
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def binary(l, r, check):
            while l < r:
                m = (l + r)/2
                if check(m):
                    r = m
                else:
                    l = m + 1
            return l

        top    = binary(0, x,           lambda x: '1' in image[x])
        buttom = binary(x, len(image),  lambda x: '0' in image[x])
        left   = binary(0, y,           lambda x: any(row[y] == '1' for row in image))
        right  = binary(y, len(image[0]), lambda x: all(row[y] == '0' for row in image))
        return (right - left) * (button - top)
