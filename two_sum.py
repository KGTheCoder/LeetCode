from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in nums:
      if nums[i] + nums[i+1] == 9:
        return "yes"

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))