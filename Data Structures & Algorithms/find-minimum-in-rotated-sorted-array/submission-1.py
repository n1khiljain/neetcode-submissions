class Solution:
    def findMin(self, nums: List[int]) -> int:
        # searching for minimum element 
        # binary search only works on sorted arrays

        # use binary search to find segment. element after is greater than elem before
        # min value is always left-most in normal sorted array
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]: #min value is to left
                r = m
            else:
                l = m + 1
        return nums[l]






            

            


        


