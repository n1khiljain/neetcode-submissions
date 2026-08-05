class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letter, t_letter = {}, {}

        for i in range(len(s)):
            s_letter[s[i]] = s_letter.get(s[i],0) + 1
            t_letter[t[i]] = t_letter.get(t[i],0) + 1

        return s_letter == t_letter