import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for x in freq:
            buckets[freq[x]].append(x)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res