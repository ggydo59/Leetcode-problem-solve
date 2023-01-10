class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        
        res = [i for i in s if i!= '']
        
        return len(res[-1])