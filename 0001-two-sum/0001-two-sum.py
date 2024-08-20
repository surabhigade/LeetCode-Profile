class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      List_len = len(nums)
      for i in range(List_len):
        for j in range(i+1, List_len):
            if (nums[i] + nums[j] == target):
                return [i,j]

