class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if s_list[i] not in hashmap.values():
                    hashmap[pattern[i]] = s_list[i]
                else:
                    return False
            elif hashmap[pattern[i]] != s_list[i]:
                return False
        return True
