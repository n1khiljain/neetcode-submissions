class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = {}
        for x in nums:
            if x in current.keys():
                return True
            else:
                current[x] = 1
        return False