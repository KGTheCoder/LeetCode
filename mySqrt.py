# import math 

class Solution:
  def mySqrt(self, x: int) -> int:
    # return int(math.sqrt(x))
    index = 1
    while index * index <= x:
      index += 1
    return index - 1

sol = Solution()
print(sol.mySqrt(8))