class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # searching for k
        # O(mlogn) -> binary search problem
        left, right = 1, max(piles) # range of k
        ans = right # answer starts at max

        while left <= right:
            k = (left + right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p) / k) 
            
            if hours <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1

        return ans




            





            

        
            

            
