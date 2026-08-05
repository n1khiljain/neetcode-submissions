class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i in range(len(nums)):
            if nums[i] in x:
                return [x[nums[i]], i]
            
            x[target-nums[i]] = i