from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    for i in nums:
      if nums[i] + nums[i+1] == 9:
        return "yes"
    """

    # Brute force solution
    """
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]
    """

    # Optimized solution
    """
    numToIndex = {}
    for i in range(len(nums)):
      if target - nums[i] in numToIndex:
        return [numToIndex[target - nums[i]], i]
      numToIndex[nums[i]] = i
    return []
    """

    """
    d = {}

    for i, n in enumerate(nums):
      diff = target - n
      if diff not in d:
        d[n] = i
        print(d)
      else:
        return [d[diff], i]
    """

    

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))