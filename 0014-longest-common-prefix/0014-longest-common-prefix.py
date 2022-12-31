class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = min(strs, key=len)
        
        for string in strs:
             while len(prefix) > 0:
                    if string.startswith(prefix):
                        break
                    else:
                        prefix = prefix[:-1]
        return prefix
                     
        