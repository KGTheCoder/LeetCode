class Solution:
  def romanToInt(self, s: str) -> int:
    roman_num = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    number = 0

    # 4 and 9
    s = s.replace("IV", "IIII").replace("IX", "VIIII")

    # 40 and 90
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")

    # 400 and 900
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    for char in s:
      number += roman_num[char]
    return number 

sol = Solution()
print(sol.romanToInt("III"))