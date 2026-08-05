class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1,len(numbers) 

        while i < j:
            if numbers[i-1] + numbers[j-1] == target:
                return [i,j]
            elif numbers[i-1] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1