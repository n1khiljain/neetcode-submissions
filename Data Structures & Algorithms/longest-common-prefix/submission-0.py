class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # longest prefix limited by shorted character
        shortest = min(strs, key=len)
        
        # want to compare against each character in shortest
        for i in range(len(shortest)):
            ch = shortest[i]
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]
        
        # if shortest is a prefix for everything
        return shortest