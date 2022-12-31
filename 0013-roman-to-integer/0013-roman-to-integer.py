class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        except_dict = {"IV": 4, "IX" :9 , "XL" : 40, "XC" :90, "CD": 400, "CM" : 900}
        res = 0
        for num in except_dict.keys():
            if num in s:
                res += except_dict[num]
                s = s.replace(num,'')
        for num in s:
            res += num_dict[num]
            

        return res