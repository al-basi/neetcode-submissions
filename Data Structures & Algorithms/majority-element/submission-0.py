class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
        return max(count, key=count.get)
