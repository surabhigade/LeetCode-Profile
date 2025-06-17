class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        output = [1 for i in range(n)]

        #1 pass one: left mult
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1] 

        #2 pass 2: right. multiplir
        for i in range(1, n):
            right[n-i-1] = right[n-i] * nums[n-i]

        #3 mul the two arrays
        for i in range(n):
            output[i] =  left[i] * right[i]
        
        return output