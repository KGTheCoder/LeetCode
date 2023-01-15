class Solution:
  def isPalindrome(self, x: int) -> bool:
    # return str(x[::1]) == str(x)

    """
    if x < 0:
      return False
    
    return str(x) == str(x)[::-1]
    """

    """
    if x < 0:
      return False
    
    inputNum = x
    newNum = 0

    while x > 0:
      newNum = newNum * 10 + x % 10
      x = x // 10
    return newNum == inputNum
    """

    if x < 0:
      return False

    a, b = x, 0

    while x:
      b *= 10
      b += x % 10
      x //= 10

    return a == b



solution = Solution()
print(solution.isPalindrome(121))