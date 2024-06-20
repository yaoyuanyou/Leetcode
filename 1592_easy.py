class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = text.count(" ")
        words = text.split()
        if len(words) == 1:
            return words[0] + " " * count
        m, n = divmod(count, len(words) - 1)
        return (m * ' ').join(words) + " " * n
