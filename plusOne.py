from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    """
    n = len(digits)

    for i in range(n):
      idx = n - 1 - i
      if digits[idx] == 9:
        digits[idx] = 0
      else:
        digits[idx] += 1
        return digits
  
    return [1] + digits
    """

    """
    num = 0
    for i in range(len(digits)):
      num += digits[i] * pow(10, (len(digits)-1-i))
      print("num =", num)
    return [int(i) for i in str(num+1)]
    """

    


sol = Solution()
print(sol.plusOne([1, 2, 3]))