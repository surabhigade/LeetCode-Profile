class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setnums = set(nums)
        if len(nums) == len(setnums):
            return False
        else: return True
