from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    count = 0
    nums = set(nums)
    for i in nums:
      count += 1
    return count

sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))