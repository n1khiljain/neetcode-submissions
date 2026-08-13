import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for x in freq:
            buckets[freq[x]].append(x)
        
        ans = []
        i = len(buckets) - 1
        while len(ans) < k:
            if buckets[i] is not None:
                ans.extend(buckets[i])
            i -= 1
        return ans