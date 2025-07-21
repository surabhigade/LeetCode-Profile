class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        for i in range(len(word1)):
            output += word1[i]
            if i < len(word2):
                output += word2[i]
        if len(word2) > len(word1):
                output += word2[len(word1)::]     
        return output
        