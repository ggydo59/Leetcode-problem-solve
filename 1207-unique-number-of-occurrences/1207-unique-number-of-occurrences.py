class Solution:
    def uniqueOccurrences(self, arr):
        
        new = list(set(arr))
        length = len(new)
        temp = [0] * length
        
        for num in arr:
            for i, value in enumerate(new):
                if value == num:
                    temp[i] += 1



        if len(temp) == len(list(set(temp))):
            return True
        else:
            return False