class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high, mid = 0, x, 0
        if x==0: return 0
        
        while low <= high:
            mid = (high+low) // 2
            
            if x < mid*mid: high = mid-1
            elif x == mid*mid: return mid
            else:
                root = mid
                low = mid+1
        
        return root