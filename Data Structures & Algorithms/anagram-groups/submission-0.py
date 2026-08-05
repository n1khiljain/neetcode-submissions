class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord assigns int unicode value to characters
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1 #gets index of character by subtrcating ascii values

            res[tuple(count)].append(word)

        return list(res.values())




                
        
            


        
            
        


            
