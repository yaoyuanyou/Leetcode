class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False

        i = 0
        j = 0
        prev = -1

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                prev = typed[j]
                i += 1
            elif typed[j] != prev:
                return False

            j += 1
        
        if (i == len(name) and j == len(typed)) or set(typed[j:]) == set(prev):
            return True

        return False
