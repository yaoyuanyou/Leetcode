# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        interval = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            return interval + 1
        return interval
