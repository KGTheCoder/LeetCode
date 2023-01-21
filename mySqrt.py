# import math 

class Solution:
  def mySqrt(self, x: int) -> int:
    # return int(math.sqrt(x))

    """
    index = 1
    while index * index <= x:
      index += 1
    return index - 1
    """

    if x == 0:
      return 0
    for i in range(1, x + 1):
      if i * i == x:
        return i
      elif i * i > x:
        return (i-1)




sol = Solution()
print(sol.mySqrt(8))