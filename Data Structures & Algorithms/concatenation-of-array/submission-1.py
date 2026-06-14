class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        ans = [0] * num_len *2

        for i in range(num_len):
            ans[i] = nums[i]
            ans[i+num_len] = nums[i]
        return ans