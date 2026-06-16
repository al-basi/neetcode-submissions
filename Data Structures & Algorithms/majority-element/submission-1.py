class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        majorty_point = len(nums) / 2
        for num in nums:
            count[num] += 1
            if count[num] > majorty_point:
                return num

