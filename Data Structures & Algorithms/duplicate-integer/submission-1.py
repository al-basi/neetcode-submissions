class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        val_idx = {} 
        
        for n in nums:
            if n in val_idx:
                return True 
            else:
                val_idx[n] = 1
        return False