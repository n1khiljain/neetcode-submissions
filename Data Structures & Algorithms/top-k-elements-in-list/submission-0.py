class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # count of each num
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        for num, c in counts.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
        
        
