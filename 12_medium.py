class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"}
        
        res, indicator = "", 0
        for x in str(num)[::-1]:
            if x == "0":
                indicator += 1
                continue
            
            elif x not in ["4", "9"]:
                if x < "5":
                    res += int_to_roman[10 ** indicator] * int(x)
                elif x == "5":
                    res += int_to_roman[5 * 10 ** indicator]
                else:
                    res += int_to_roman[10 ** indicator] * (int(x) - 5)+ int_to_roman[5 * 10 ** indicator]
            
            elif x == "4":
                res += int_to_roman[5 * 10 ** indicator] + int_to_roman[10 ** indicator]
            else:
                res += int_to_roman[10 * 10 ** indicator] + int_to_roman[10 ** indicator]
            
            indicator += 1
            
        return res[::-1]
        
            

num = 2000
print(Solution().intToRoman(num))
