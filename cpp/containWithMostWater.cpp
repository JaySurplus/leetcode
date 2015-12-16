/*
"""
	Problem statement
		Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

		Note: You may not slant the container.

		Subscribe to see which companies asked this question

		
	https://leetcode.com/problems/container-with-most-water/
"""

*/

#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int right = height.size() -1;
        int left = 0;
        int result = 0 ;

        while (left < right) {
        	result = max(result,  min(height[right] , height[left]) * (right - left) );
			if (height[right] > height[left])
				left++;
			else
				right--;        	
        }

        return result;

    }
};