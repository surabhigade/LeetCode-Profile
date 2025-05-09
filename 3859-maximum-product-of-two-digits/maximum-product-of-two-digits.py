class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = str(n)
        p = len(number)
        digits = [0] * p
        for i in range(p):
            digits[i] =  int(str(number[i]))

        for i in range(p):
            for j in range(0, p-i-1):
                if digits[j] > digits[j+1]:
                    digits[j], digits[j+1] = digits[j+1], digits[j]
        max = digits[p-1]*digits[p-2]

        return max
            
            
        