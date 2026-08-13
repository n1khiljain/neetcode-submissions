class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        
        for i, val in enumerate(nums):
            difference = target - val
            if difference in a:
                return [min(i, a[difference]), max(i, a[difference])]
            else:
                a[val] = i