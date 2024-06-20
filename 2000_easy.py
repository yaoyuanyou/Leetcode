class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        if index == len(word) - 1:
            return word[::-1]
        return word[index::-1] + word[index + 1:]
