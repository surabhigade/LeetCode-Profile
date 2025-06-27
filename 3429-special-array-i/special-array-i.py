class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1, len(nums)):
            # Check if current and previous elements have the same parity
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True
        