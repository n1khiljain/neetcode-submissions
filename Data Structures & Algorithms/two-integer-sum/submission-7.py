class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in x:
                return [min(x[nums[i]], i), max(x[nums[i]], i)]
            else:
                x[difference] = i

