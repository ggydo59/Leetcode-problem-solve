class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = ''
        for i in digits: temp += str(i)
        temp = int(temp) + 1
        
        return [int(i) for i in str(temp)]
        