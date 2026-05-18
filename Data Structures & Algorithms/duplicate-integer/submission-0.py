class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        val_idx = {} # key = value (nums), value = index
        
        for i, n in enumerate(nums):
            if n in val_idx:
                return True 
            else:
                val_idx[n] = i
        return False