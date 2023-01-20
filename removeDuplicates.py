from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    """
    count = 0
    nums = set(nums)
    for i in nums:
      count += 1
    return count
    """

    """
    nums[:] = sorted(set(nums))
    return len(nums)
    """

    """
    slow, fast = 0, 1
    while fast in range(len(nums)):
      if nums[slow] == nums[fast]:
        fast += 1
      else:
        nums[slow+1] = nums[fast]
        fast += 1
        slow += 1

    return slow + 1
    """

    """
    j = 0
    for i in range(1, len(nums)):
      if nums[j] != nums[i]:
        j += 1
        nums[j] = nums[i]

    return j + 1
    """

    """
    index = 1
    
    while index < len(nums):
      if nums[index] == nums[index-1]:
        nums.pop(index)
      else:
        index += 1
    return len(nums)
    """

    if len(nums) == 1:
      return 1

    x = nums[0]
    i = 0
    
    while i < len(nums)-1:
      if x == nums[1+i]:
        del nums[1+i]
      else:
        x = nums[1+i]
        i += 1

    return i + 1


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))