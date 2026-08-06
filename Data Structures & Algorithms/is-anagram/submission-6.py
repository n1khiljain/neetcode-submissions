class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap -> char -> freq
        s_map = {}
        t_map = {}

        for letter in s:
            s_map[letter] = 1 + s_map.get(letter, 0)

        for letter in t:
            t_map[letter] = 1 + t_map.get(letter, 0)
            
        return s_map == t_map
        
