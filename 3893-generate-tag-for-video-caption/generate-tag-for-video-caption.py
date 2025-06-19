class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        res = caption.strip().split()  
        for i in range(len(res)):
            if not res[i]:  
                continue
            temp = res[i][0].lower() if i == 0 else res[i][0].upper()
            for j in range(1, len(res[i])):
                temp += res[i][j].lower()
            res[i] = temp
        return "#" + "".join(res)[:99]

        
        
            
            