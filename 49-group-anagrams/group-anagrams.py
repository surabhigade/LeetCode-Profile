class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = defaultdict()
        for word in strs:
            key = "".join(sorted(word))
            if key not in mapping:
                mapping[key]= [word]
            else: mapping[key].append(word)
        
        return mapping.values()