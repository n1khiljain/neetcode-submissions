import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort of frequencies
        # for [1,2,2,3,3,3]
        # [[], [1], [2], [3], [], [], []]
        heap = []
        freq = {}

        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        # order off of frequency, value
        for key, v in freq.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]
