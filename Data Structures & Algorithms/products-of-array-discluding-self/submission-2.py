class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeros= 0

        for i, n in enumerate(nums):
            if n:
                total_product *= n
                continue
            zeros += 1

        if zeros > 1: return [0] * len(nums)
        
        res = []
        for i, n in enumerate(nums):
            if zeros: res.append(0 if n else total_product)
            else: res.append(total_product // n)
        return res
            
     

        
