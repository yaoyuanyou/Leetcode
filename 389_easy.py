#Initial
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        dict_s = {}
        dict_t = {}

        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        for j in t:
            dict_t[j] = dict_t.get(j, 0) + 1
            if dict_t[j] > dict_s.get(j, 0):
                return j

              
#Count
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      for i in t:
        if t.count(i) != s.count(i):
          return i
