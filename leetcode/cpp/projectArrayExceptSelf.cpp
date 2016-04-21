	/*
		Product of Array Except Self

		Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

		Solve it without division and in O(n).
		
		For example, given [1,2,3,4], return [24,12,8,6].
		
		Follow up:
		Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

		https://leetcode.com/problems/product-of-array-except-self/
	*/

#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
       	
       	int temp = 1;
       	vector<int> result(length);
     
 		result[0] = 1;
        for (int i = 1 ; i < length; i++){
        	temp = temp * nums[i-1];
        	result[i] = temp;
        }
        	

        temp = 1;
        for(int i = length -2 ; i >= 0 ; i--){
        	temp = temp*nums[i+1];
        	result[i] = result[i] * temp;
        };
        	


        return result;

    }
};		


int main(){
	Solution sol;
	vector<int> list = {1,2,3,4};
	cout << sol.productExceptSelf(list) << endl;
}