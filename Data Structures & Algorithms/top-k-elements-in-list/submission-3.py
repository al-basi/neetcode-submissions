class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        if len(set_nums) <= k:
            return list(set_nums)

        freq = Counter(nums)
        res = sorted(freq, key=freq.get, reverse=True)[:k]
        
        return res
