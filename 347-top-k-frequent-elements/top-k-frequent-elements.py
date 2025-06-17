class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicti = {}
        output = []
        for i in range(len(nums)):
            if nums[i] not in dicti:
                dicti[nums[i]] = 1
            else:
                dicti[nums[i]] +=1
        count_sorted = sorted(dicti.items(), key= lambda x:-x[1])

        for num, count in count_sorted[:k]:
            output.append(num) 
        return output