class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IX": 9,
            "IV": 4,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        length = len(s)
        if length == 1:
            return hashmap[s]

        res, i= 0, 0 
        while i < length:
            if i + 1 < length and s[i] + s[i + 1] in hashmap:
                res += hashmap[s[i] + s[i + 1]]
                i += 2
            else:
                res += hashmap[s[i]]
                i += 1
        
        return res
