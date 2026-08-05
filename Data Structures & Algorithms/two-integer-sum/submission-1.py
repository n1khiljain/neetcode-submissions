class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}

        for i in range(len(nums)):
            current = target - nums[i]
            if current in a:
                return [min(a[current], i), max(a[current], i)]
            a[nums[i]] = i



        
