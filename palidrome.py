class Solution:
  def isPalindrome(self, x: int) -> bool:
    # return str(x[::1]) == str(x)
    if x < 0:
      return False
    
    return str(x) == str(x)[::-1]


solution = Solution()
print(solution.isPalindrome(121))