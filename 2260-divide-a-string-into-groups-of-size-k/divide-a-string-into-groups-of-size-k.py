class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """

        n = len(s)
        output = []
        for i in range(0, n, k):
            temp = s[i:i+k]
            if len(temp)<k:
                temp += fill* (k- len(temp))
            output.append(temp)

        return output