class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        res = []
        zeros = 0
        zero_index = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeros +=1
                zero_index = i
                continue
            total_product *= n
        
        if zeros > 1:
             res = [0] * len(nums)

        elif zeros == 1:
            for i, n in enumerate(nums):
                if i == zero_index:
                    res.append(total_product)
                    continue
                res.append(0)
        
        else:
            for n in nums:
                res.append(int(total_product/n))            

        return res

        
