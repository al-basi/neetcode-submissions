class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_idx = {} # value : index

        for i, n in enumerate(nums):
            wanted = target - n
            if wanted in val_idx and val_idx[wanted] != i:
                return [val_idx[wanted], i]
            else:
                val_idx[n]= i
        return [] # -> if no solution is found