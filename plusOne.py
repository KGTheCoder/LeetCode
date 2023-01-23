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

    """
    digits[-1] += 1
    for i in range(len(digits)-1, 0, -1):
      if digits[i] != 10:
        break
      digits[i] = 0
      digits[i-1] += 1

    if digits[0] == 10:
      digits[0] = 0
      return [1] + digits
    return digits
    """

    """
    a = ''.join(map(str, digits))
    b = int(a) + 1
    c = str(b)
    return list(map(int, c))
    """

    """
    if digits[-1] < 9:
      digits[-1] += 1
      return digits
    elif len(digits) == 1 and digits[0] == 9:
      return [1, 0]
    else:
      digits[-1] = 0
      digits[0:-1] = self.plusOne(digits[0:-1])
      return digits
    """

    """
    a = [str(i) for i in digits]
    a = ''.join(a)
    a = str(int(a) + 1)
    return [int(i) for i in a]
    """

    return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]



sol = Solution()
print(sol.plusOne([1, 2, 3]))