class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_idx = {}

        for i, n in enumerate(nums):
            wanted = target - n
            if wanted in map_idx:
                if i != map_idx[wanted]:
                    return [map_idx[wanted], i]
            else:
                map_idx[n]= i
    