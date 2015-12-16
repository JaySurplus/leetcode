/*"""
	Trapping Rain Water
	
	Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

	For example, 
	Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


	https://leetcode.com/submissions/detail/48204970/
"""
*/



#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
	int trap(vector<int>& height){
		int i = 0 ;
		int j = height.size() -1;
		int result = 0;
		int current_max = 0;

		while( i <= j ){
			current_max = max(current_max , min(height[i], height[j]));
			if (height[i] <= height[j]){
				result += current_max - height[i];
				i++ ;
			}
			else{
				result += current_max - height[j];
				j--;
			}
		};

		return result;

	};
};



int main(){
	Solution test ;
	vector<int> list = {0,1,0,2,1,0,1,3,2,1,2,1};

	cout << test.trap(list) << endl;
}
