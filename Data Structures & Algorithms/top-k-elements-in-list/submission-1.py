class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        counts = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # {1: 1, 2: 2, 3: 3}
        for key, value in freq.items():
            counts[value].append(key)
        # [[], [1], [2], [3], [], [], ...]

        res = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res





            
        
        
        
