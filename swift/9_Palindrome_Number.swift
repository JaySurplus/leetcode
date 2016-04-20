class Solution{
	func isPalindrome(x:Int) -> Bool {
		if (x < 0) {
			return false
		}
		
		if (x < 10) {
			return true
		}
		
		if (x % 10 == 0) {
			return false
		}
		
		var y = 0
		var t = x
		while (t > y) {
			y = y * 10 + t % 10
		    t = t / 10
		}
		
		return t == y || t == y / 10
		
	}
}

let sol = Solution()
let res = sol.isPalindrome(121)
print(res)