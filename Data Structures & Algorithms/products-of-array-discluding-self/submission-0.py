class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # [1,2,4,6]    
        n = len(nums) # 4
        res = [0] * n
        pref = [0] * n # [0,0,0,0]
        suff = [0] * n # [0,0,0,0]

        pref[0] = suff[n-1] = 1 # [1,0,0,0], [0,0,0,1]

        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1] # [1,1,2,8]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1] # [48,24,6,1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

        
