class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(len(nums)-2):
            if nums[i+1] % 2 == 0:
                sum = nums[i]+nums[i+2]
                if(sum == (nums[i+1])//2):
                    count +=1
        return count

        