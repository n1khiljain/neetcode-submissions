class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for letter in s:
            if letter in s_letters.keys():
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1
        for letter in t:
            if letter in t_letters.keys():
                t_letters[letter] += 1
            else:
                t_letters[letter] = 1
        return s_letters == t_letters