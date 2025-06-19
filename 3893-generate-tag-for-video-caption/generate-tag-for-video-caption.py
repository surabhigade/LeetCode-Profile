class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        words = caption.split()
        if not words:
            return "#"
        output = ""
        for i in range(len(words)):
            if i == 0:
                output = "#" + words[i].lower()
            else:
                output += words[i].capitalize()

        return output[:100]
            
            