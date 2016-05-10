// Problem 153

class Solution {
    public int findMin(int[] nums) {
        int len = nums.length;
        if (len == 1) {
            return nums[0];
        }
        int l = 0;
        int r = len - 1;
        int mid;
        while (l <= r) {
            mid = (l+r)/2;
            if (nums[mid] >= nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[r];
    }
}

class Test {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = new int[] {2,1};
        System.out.println(sol.findMin(nums));
    }
}
