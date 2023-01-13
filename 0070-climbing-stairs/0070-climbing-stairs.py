class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [0]*n
        if n <= 2:
            return n
        
        d[0], d[1] = 1, 2
        
        for i in range(2, n):
            d[i] = d[i-2] + d[i-1]
        
        return d[n-1]