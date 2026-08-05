class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list) # frequency array : strs
        res = []

        for s in strs:
            a = [0] * 26
            for letter in s:
                a[ord(letter)-ord('a')] += 1
            freq[tuple(a)].append(s)
        
        for v in freq.values():
            res.append(v)
        return res

        
